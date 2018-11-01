import sys
from decimal import Decimal
from datetime import date, datetime, timedelta
from dateutil.parser import parse as parse_datetime
import calendar
from time import mktime
import json
from urllib.parse import urlencode, unquote, quote_plus
import requests
from marshmallow import ValidationError
from pytz import UTC

from sqlalchemy import (
    Integer, SmallInteger, Float, Text, String, DateTime, Date, Time, Boolean, ForeignKey, BigInteger,
    Table, JSON
)
from sqlalchemy_utils import aggregated

from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import backref, foreign, relationship, synonym, column_property
from sqlalchemy.sql import func, select, case, cast, alias, literal
from sqlalchemy import (Column, desc, and_, or_, text as text_, PrimaryKeyConstraint, inspect, Sequence,
                        UniqueConstraint)
from sqlalchemy.orm.exc import NoResultFound

from .fields import ChoiceType, PrefixRange
from falcon_rest.contrib.objects_history.object_revision.object_revision import ObjectRevisionModel
from falcon_rest.db import errors
from falcon_rest.db.orm import generate_uuid_str
from falcon_rest.db.fields import (Numeric)
from falcon_rest.logger import log
from falcon_rest import helpers, resources
from falcon_rest.contrib.objects_history.auth_user import AuthUser
from traceback import format_exc
from .rbac.rbac_role import AdminRole, UserRole, ResellerRole, RbacUser, CompanyAdminRole, RbacRoleNoRole
from . import settings
from .base_model import BaseModel
from .utils.mailer import Mailer
from .file import ModelUsingFiles, FileModel, \
    relationship as file_relationship
from falcon_rest.contrib.files.models import FileModelField  # ,relationship as file_relationship
from falcon_rest.contrib.files.backends import GoogleDriveBackEnd, FileSystemBackEnd

# FILE_BACKEND = GoogleDriveBackEnd()
FILE_BACKEND = FileSystemBackEnd()


def settings_get_mailer():
    mailing_conf = settings.MAILING
    log.info('Mail settings {}'.format(str(mailing_conf)))
    return Mailer(**mailing_conf)


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def init_db():
    from falcon_rest.db import initialize_db
    from .settings import DB_CONN_STRING
    initialize_db(DB_CONN_STRING, BaseModel)


from falcon_rest.db import get_db


def get_metadata():
    return get_db().declarative_base.metadata


def q_str(q):
    return str(q.statement.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))


def rev(d):
    return dict((v, k) for k, v in d.items())


def _ref_id(cls_name, field, value):
    if type(value) == type(''):
        value = "'" + value + "'"
    mod = sys.modules['api_dnl.model']
    cls = mod.__dict__[cls_name]
    pk_field_name = cls.get_model_class_primary_key()
    pk_field = cls.get_field(pk_field_name)
    return cls.filter('field={}'.format(value)).one().get_field(pk_field_name)


import bcrypt


def get_hashed_password(plain_text_password):
    if not plain_text_password:
        import random
        plain_text_password = str(round(random.random() * 1000000000, 0))
    if isinstance(plain_text_password, type('')):
        plain_text_password = plain_text_password.encode()
    hash = bcrypt.hashpw(
        plain_text_password,
        bcrypt.gensalt()
    )
    if isinstance(hash, type(b'')):
        hash = hash.decode()
    return hash


class User(BaseModel, AuthUser, RbacUser, ModelUsingFiles):
    __tablename__ = 'user'
    user_uuid = Column(String(36), primary_key=True, default=generate_uuid_str(),
                       server_default=func.uuid_generate_v4())
    # name = Column(String(64), index=True)
    email = Column(String(128), nullable=False, unique=True, index=True)
    password = Column(String(72))
    is_admin = Column(Boolean(), default=False)
    last_login = Column(DateTime(timezone=True))
    is_active = Column(Boolean(), default=False)
    confirmed_on = Column(DateTime(True))
    created_on = Column(DateTime(True), server_default=func.now())
    # addons

    logo_file_uuid = FileModelField(FileModel, nullable=True, backend=FILE_BACKEND)
    logo = file_relationship(FileModel, 'User', 'logo_file_uuid')

    user_id = synonym('user_uuid')
    name = synonym('email')
    user_name = synonym('email')
    is_confirmed = column_property(confirmed_on.isnot(None))

    @classmethod
    def init(cls):
        adm = cls.get(settings.ADMIN_UUID)
        if not adm:
            cls(user_uuid=settings.ADMIN_UUID, email=settings.ADMIN_EMAIL, passwd=settings.ADMIN_PWD,
                is_admin=True, is_active=True).save()
        test = cls.get(settings.TEST_USER_UUID)
        if not test:
            cls(user_uuid=settings.TEST_USER_UUID, email=settings.TEST_USER_EMAIL, passwd=settings.ADMIN_PWD,
                is_admin=False, is_active=True).save()

    @hybrid_property
    def passwd(self):
        return '********'  # self.password

    @passwd.setter
    def passwd(self, value):
        self.password = get_hashed_password(value)

    @classmethod
    def get_user_from_credentials(cls, credentials):
        try:
            return cls.filter(
                or_(User.name == credentials['email'], User.email == credentials['email'])).one()
        except:  # errors.NoResultFound:
            cls.query().session.rollback()
            return None

    def get_token_data(self):
        return dict(user_uuid=self.user_uuid)

    @classmethod
    def get_user_from_token_data(cls, token_data):
        if 'user_uuid' in token_data:
            return cls.filter(User.user_uuid == token_data['user_uuid']).first()
        return None

    @classmethod
    def get_user_by_id(cls, user_uuid):
        try:
            return cls.filter(User.user_uuid == user_uuid).one()
        except errors.NoResultFound:  # pragma: no cover
            return None

    def can_login(self, req, resp):
        if self.is_active:
            return True
        else:
            resources.BaseResource.set_response(
                resp, resources.responses.UnAuthorizedErrorResponse(
                    data=resources.errors.Error(
                        10000,
                        'You are not allowed to login. You must to finish confirm procedure or ask admin to activate account',
                        'account disabled'
                    )
                )
            )
            return False
        request_ip = helpers.get_request_ip(req)
        if request_ip in settings.ALWAYS_ALLOWED_AUTH_IPS:
            return True
        # try:
        #    UserAuthIp.filter(UserAuthIp.ip == request_ip, UserAuthIp.user_uuid == self.user_uuid).one()
        #    return True
        # except errors.NoResultFound:
        #    if not UserAuthIp.filter(UserAuthIp.user_uuid == self.user_uuid).count():
        #        return True
        resources.BaseResource.set_response(
            resp, resources.responses.UnAuthorizedErrorResponse(
                data=resources.errors.Error(
                    10000,
                    'You are not allowed to login from the IP {}'.format(request_ip),
                    'ip_not_allowed'
                )
            )
        )
        return False

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def can_restore(self, object_revision):
        return True

    def get_id(self):
        return self.user_uuid

    def user_type(self):
        return self.get_role().get_name()

    def get_role(self):
        if self.is_admin:
            return AdminRole
        else:
            return UserRole
        return RbacRoleNoRole

    def before_save(self):
        super().before_save()
        if (not self.name) and self.email:
            self.name = self.email
        if (not self.email) and self.name:
            self.email = self.name

    def apply_mail(self, template_name):
        template = EmailTemplate.get(template_name)
        if not template:
            return 'no such template'
        from_addr = template.email_from
        from_addr = settings.MAILING['username']
        try:
            mail = settings_get_mailer()
            mail.set_variables({'user': self})
            mail.set_content(
                template.subject, template.content_text, template.content_html
            )
        except Exception as e:
            log.error(e)
            return False

        status = mail.send(from_addr, self.email, template.email_cc)
        EmailLog.log(self.user_uuid, template.name, mail.subject, from_addr, self.email, mail.get_content(),
                     status, template.email_cc)
        return status

    @property
    def reset_password_url(self):
        if self.token:
            return '{}{}{}/auth/reset_password/{}'.format(settings.API_SCHEME, settings.API_HOST,
                                                          settings.API_BASE_PATH, self.token)
        return ''

    @property
    def confirm_url(self):
        if self.token:
            return '{}{}{}/registration/confirm/{}'.format(settings.API_SCHEME, settings.API_HOST,
                                                           settings.API_BASE_PATH, self.token)
        return ''

    @property
    def login_url(self):
        return '{}{}{}/auth/'.format(settings.API_SCHEME, settings.API_HOST, settings.API_BASE_PATH)


User.role_name = column_property(case([(User.is_admin, 'admin')], else_='user'))


class EmailLog(BaseModel):
    __tablename__ = 'email_log'
    id = Column(Integer(), primary_key=True)
    sender_id = Column(String(36))
    name = Column(String(64), nullable=False, index=True)
    subject = Column(String(1024), nullable=False)
    email_from = Column(String(255), nullable=False)
    email_to = Column(String(255), nullable=False)
    email_cc = Column(String(512))
    content_text = Column(Text(), nullable=False)
    status = Column(String(512))

    @staticmethod
    def log(sender_id, name, subject, email_from, email_to, content_text, status, email_cc=None):
        status_text = str(status)
        rec = EmailLog(sender_id=sender_id, name=name, subject=subject, email_from=email_from, email_to=email_to,
                       content_text=content_text, status=status_text, email_cc=email_cc)
        rec.save()


class EmailTemplate(BaseModel):
    __tablename__ = 'email_template'

    TEMPLATES = {'retrieve_password': 'Hi {{user.name}} your reset password url is {{user.reset_password_url}}',
                 'registration': 'Hi {{user.name}} your confirm registration url is {{user.token}}',
                 'welcome': 'WELCOME {{user.name}} ,your login url is {{user.login_url}}',
                 }
    name = Column(String(64), primary_key=True)
    subject = Column(String(1024), nullable=False)
    email_from = Column(String(255), nullable=False)
    email_cc = Column(String(512))
    content_text = Column(Text(), nullable=False)
    content_html = Column(Text())
    hint = Column(Text(), nullable=False)

    @classmethod
    def init(cls):

        for name, content in cls.TEMPLATES.items():
            if not type(name) == type('') or '.' in name:
                continue
            q = EmailTemplate.filter(EmailTemplate.name == name).first()
            if q:
                continue
            try:
                templ = EmailTemplate(name=name, subject=name, hint=name, email_from='nobody@example.com',
                                      content_text='n/a', content_html=content)
                templ.save()
            except:
                pass
        for tpl in EmailTemplate.query().all():
            if tpl.name not in cls.TEMPLATES:
                log.warning('Purge email template {}'.format(tpl.name))
                tpl.delete()


### other models

class Notification(BaseModel, ModelUsingFiles):
    __tablename__ = 'notification'

    notification_uuid = Column(String(36), primary_key=True, default=generate_uuid_str(),
                               server_default=func.uuid_generate_v4())
    user_uuid = Column(ForeignKey('user.user_uuid', ondelete='CASCADE'), nullable=True, index=True)

    subject = Column(String(64), nullable=False)
    content = Column(Text, nullable=False)
    created_on = Column(DateTime(True), nullable=False, server_default=func.now())


class Plan(BaseModel):
    __tablename__ = 'plan'
    TYPE = {1: 'switch pay per port', 2: 'switch pay per minute', 3: 'LRN pay per CPS', 4: 'LRN pay per DIP'}
    plan_uuid = Column(String(36), primary_key=True, default=generate_uuid_str(),
                       server_default=func.uuid_generate_v4())

    type = Column(ChoiceType(TYPE), default=1)
    amount = Column(Numeric, nullable=False, server_default='0')


class Payment(BaseModel):
    __tablename__ = 'payment'
    TYPE = {1: 'paypal', 2: 'strip'}
    payment_uuid = Column(String(36), primary_key=True, default=generate_uuid_str(),
                          server_default=func.uuid_generate_v4())
    user_uuid = Column(ForeignKey('user.user_uuid', ondelete='CASCADE'), index=True)
    license_lrn_uuid = Column(ForeignKey('license_lrn.license_lrn_uuid', ondelete='CASCADE'), nullable=True,
                                 index=True)
    license_switch_uuid = Column(ForeignKey('license_switch.license_switch_uuid', ondelete='CASCADE'),
                                   nullable=True,
                                   index=True)
    amount = Column(Numeric, nullable=False, server_default='0')
    paid_time = Column(DateTime(True), nullable=False, server_default=func.now())
    type = Column(ChoiceType(TYPE), default=1)
    description=Column(Text)




class PackageLrn(BaseModel):
    __tablename__ = 'package_lrn'
    TYPE = {3: 'LRN pay per CPS', 4: 'LRN pay per DIP'}
    package_lrn_uuid = Column \
        (String(36), primary_key=True, default=generate_uuid_str(),
         server_default=func.uuid_generate_v4())
    package_name = Column(String(64),unique=True)
    cps = Column(Integer())
    type = Column(ChoiceType(TYPE), default=3)
    lrn_port = Column(Integer())
    dip_count = Column(Integer())
    amount = Column(Integer())
    enabled = Column(Boolean,default=True)
    licenses = relationship('LicenseLrn', uselist=True, back_populates='package')


class LicenseLrn(BaseModel):
    __tablename__ = 'license_lrn'
    __table_args__ = (UniqueConstraint('package_lrn_uuid', 'user_uuid', name='uq_license_lrn_package_lrn_uuid_user_uuid'),
                      )
    license_lrn_uuid = Column \
        (String(36), primary_key=True, default=generate_uuid_str(),
         server_default=func.uuid_generate_v4())
    package_lrn_uuid = Column(ForeignKey('package_lrn.package_lrn_uuid', ondelete='CASCADE'), index=True)
    user_uuid = Column(ForeignKey('user.user_uuid', ondelete='CASCADE'), index=True)
    ip = Column(String(16), nullable=False,index=True)
    start_time = Column(DateTime(True), nullable=False, server_default=func.now())
    end_time = Column(DateTime(True), nullable=True)
    ordered_amount = Column(Integer)
    cost = Column(Numeric, nullable=False, server_default='0')

    package = relationship('PackageLrn', uselist=False, back_populates='licenses')
    
    user_email = column_property(
        select([User.email]).where(user_uuid == User.user_uuid).correlate_except(User))
    cps = column_property(select([PackageLrn.cps]).where(package_lrn_uuid==PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))
    type = column_property(select([PackageLrn.type]).where(package_lrn_uuid==PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))
    lrn_port = column_property(select([PackageLrn.lrn_port]).where(package_lrn_uuid==PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))
    dip_count = column_property(select([PackageLrn.dip_count]).where(package_lrn_uuid==PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))
    amount = column_property(select([PackageLrn.amount]).where(package_lrn_uuid==PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))
    

class Switch(BaseModel):
    __tablename__ = 'switch'
    switch_uuid = Column \
        (String(36), primary_key=True, default=generate_uuid_str(),
         server_default=func.uuid_generate_v4())
    switch_ip = Column(String(16))
    enabled = Column(Boolean, default=True)
    current_port_count = Column(Integer())
    minute_remaining = Column(Integer())
    expired_on = Column(DateTime(True), nullable=True)
    email = Column(String(256))
    packages = relationship('PackageSwitch', uselist=True, back_populates='switch')

class PackageSwitch(BaseModel):
    __tablename__ = 'package_switch'
    TYPE = {1: 'switch pay per port', 2: 'switch pay per minute'}

    package_switch_uuid = Column \
        (String(36), primary_key=True, default=generate_uuid_str(),
         server_default=func.uuid_generate_v4())

    package_name = Column(String(64),unique=True)

    type = Column(ChoiceType(TYPE), default=1)
    switch_uuid = Column(ForeignKey('switch.switch_uuid', ondelete='CASCADE'), index=True)
    switch_port = Column(Integer())
    minute_count = Column(Integer())
    amount = Column(Integer())
    enabled = Column(Boolean,default=True)
    licenses = relationship('LicenseSwitch', uselist=True, back_populates='package')
    switch = relationship('Switch', uselist=False, back_populates='packages')


class LicenseSwitch(BaseModel):
    __tablename__ = 'license_switch'
    __table_args__ = (UniqueConstraint('package_switch_uuid','user_uuid',name='uq_license_switch_package_switch_uuid_user_uuid'),
                      )
    license_switch_uuid = Column \
        (String(36), primary_key=True, default=generate_uuid_str(),
         server_default=func.uuid_generate_v4())
    package_switch_uuid = Column(ForeignKey('package_switch.package_switch_uuid', ondelete='CASCADE'), index=True)
    ip = Column(String(16), nullable=False,index=True)
    user_uuid = Column(ForeignKey('user.user_uuid', ondelete='CASCADE'), index=True)
    start_time = Column(DateTime(True), nullable=False, server_default=func.now())
    end_time = Column(DateTime(True), nullable=True)
    ordered_amount = Column(Integer)
    cost = Column(Numeric, nullable=False, server_default='0')
    package = relationship('PackageSwitch', uselist=False, back_populates='licenses')

    user_email = column_property(
        select([User.email]).where(user_uuid == User.user_uuid).correlate_except(User))

    type = column_property(
        select([PackageSwitch.type]).where(package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(PackageSwitch))
    switch_uuid = column_property(
        select([PackageSwitch.switch_uuid]).where(package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(PackageSwitch))

    switch_port = column_property(
        select([PackageSwitch.switch_port]).where(package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(
            PackageSwitch))
    minute_count = column_property(
        select([PackageSwitch.minute_count]).where(package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(
            PackageSwitch))
    amount = column_property(
        select([PackageSwitch.amount]).where(package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(PackageSwitch))


class LicenseUpdateHistory(BaseModel):
    __tablename__ = 'license_update_history'
    ACTION = {0: 'Increase/Modify the license', 1: 'Set to expired'}
    STATUS = {0: 'Initial', 1: 'Update completed', 2: 'Update failed'}
    id = Column(Integer, primary_key=True)
    uuid = Column(String(100), index=True)
    license_channel = Column(Integer)
    license_cps = Column(Integer)
    license_day = Column(Integer)
    client_name = Column(String(100))
    remarks = Column(String(100))
    action = Column(SmallInteger, nullable=False, server_default='0')
    status_1 = Column(SmallInteger, index=True, nullable=False, server_default='0')
    status_2 = Column(SmallInteger, index=True, nullable=False, server_default='0')
    progress = Column(String(200))
    operator = Column(String(50))
    create_on = Column(DateTime(True), nullable=False, server_default=func.now())
    remain = Column(String)


class LrnPermissionUpdateHistory(BaseModel):
    __tablename__ = 'lrn_permission_update_history'
    ACTION = {0: 'Increase/Modify the license', 1: 'Forbidden'}
    STATUS = {0: 'Initial', 1: 'Update completed', 2: 'Update failed'}
    id = Column(Integer, primary_key=True)
    switch_ip = Column(String(16))
    permit_cps = Column(Integer)
    client_name = Column(String(100))
    remarks = Column(String(200))
    action = Column(SmallInteger, nullable=False, server_default='0')
    status_1 = Column(SmallInteger, index=True, nullable=False, server_default='0')
    progress = Column(String(200), index=True, nullable=False, server_default='0')
    operator = Column(String(50))
    create_on = Column(DateTime(True), nullable=False, server_default=func.now())
    remain = Column(String)
