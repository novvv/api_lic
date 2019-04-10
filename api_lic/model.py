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
    Table, JSON,text,CHAR
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
    if type(sourcedate)==type(date):
        return date(year, month, day)
    else:
        return datetime(year, month, day,sourcedate.hour,sourcedate.minute,sourcedate.second,tzinfo=sourcedate.tzinfo)


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


def _apply_mail(self, template_name, var_name):
    template = EmailTemplate.get(template_name)
    if not template:
        return 'no such template'
    from_addr = template.email_from
    from_addr = settings.MAILING['username']
    try:
        mail = settings_get_mailer()
        mail.set_variables({var_name: self})
        mail.set_content(
            template.subject, template.content_text, template.content_html
        )
    except Exception as e:
        import traceback
        log.error('cannot render {}:{}:{}'.format(template.content_html,e,traceback.format_exc()))
        return 'Bad email template "{}" syntax. error {}'.format(template_name,str(e))
    email = None
    if hasattr(self, 'email') and hasattr(self, 'user_uuid'):
        email = self.email
        user_uuid = self.user_uuid
    if hasattr(self, 'user'):
        email = self.user.email
        user_uuid = self.user.user_uuid
    status = mail.send(from_addr, email, template.email_cc)
    EmailLog.log(user_uuid, template.name, mail.subject, from_addr, email, mail.get_content(),
                 status, template.email_cc)
    return status


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

    first_name = Column(String(32), nullable=True, index=True)
    last_name = Column(String(32), nullable=True, index=True)

    # alerts flags
    alert_payment_received = Column(Boolean(), server_default='true')
    alert_license_expired = Column(Boolean(), server_default='true')
    alert_license_will_expired = Column(Boolean(), server_default='true')
    alert_license_purchased = Column(Boolean(), server_default='true')

    user_id = synonym('user_uuid')
    name = synonym('email')
    user_name = synonym('email')
    is_confirmed = column_property(confirmed_on.isnot(None))

    full_name = column_property(func.concat(first_name, ' ', last_name))

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
        return _apply_mail(self, template_name, 'user')

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
                 'payment_received': 'Hi {{payment.user.name}} payment of {{payment.amount_total}} [{{payment.amount_lrn}}+{{payment.amount_switch}}] for licenses LRN:{{payment.license_lrn_uuid}},SWITCH:{{payment.license_switch_uuid}} was received '
                                     'on {{payment.paid_time}} from {{payment.type}} gateway',
                 'payment_failed': 'Hi {{user.name}},for some reasons payment of {{user.amount_total}} was failed to accept on your account'
                                     'on {{payment.paid_time}} from {{payment.type}} gateway. Probably payment description with licenses uuids is wrong',
                 'license_expired': 'Hi {{license.user.name}} your license {{license.license_uuid}} was expired on {{license.end_time}}',
                 'license_will_expired': 'Hi {{license.user.name}} your license {{license.license_uuid}} will expired on {{license.end_time}}',
                 'license_purchased': 'Hi {{license.user.name}} your license {{license.license_uuid}} purchased succesfulley ' \
                                      'actual period for license is {{license.end_time}} {{license.end_time}} '
                                      'License type is {{license.type}} {{license.sub_type}}. Bought package {{license.package.package_name}}'
                 }
    name = Column(String(64), primary_key=True)
    subject = Column(String(1024), nullable=False)
    email_from = Column(String(255), nullable=False)
    email_cc = Column(String(512), nullable=True)
    content_text = Column(Text(), nullable=True)
    content_html = Column(Text(), nullable=False)
    hint = Column(Text(), nullable=True)

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

class ConfigPayment(BaseModel):
    __tablename__ = 'config_payment'

    CHARGE_TYPE = {0: 'actual received', 1: 'credit total'}
    id = Column(Integer(), primary_key=True)
    charge_type = Column(ChoiceType(CHARGE_TYPE))
    stripe_email = Column(String(64))
    stripe_skey = Column(String(64))
    stripe_pkey = Column(String(64))
    stripe_svc_charge = Column(Integer())
    stripe_test_mode = Column(Boolean())

    paypal_email = Column(String(64))
    paypal_skey = Column(String(128))
    paypal_pkey = Column(String(128))
    paypal_svc_charge = Column(Numeric())
    paypal_test_mode = Column(Boolean())

    confirm_enabled = Column(Boolean())
    email_confirm_to = Column(String(64))
    notification_enabled = Column(Boolean())
    email_cc_to = Column(String(64))
    paypal_client_id = synonym('paypal_pkey')

    def init(self):
        pass

    def update_ini(self):
        pass


class Notification(BaseModel, ModelUsingFiles):
    __tablename__ = 'notification'

    notification_uuid = Column(String(36), primary_key=True, default=generate_uuid_str(),
                               server_default=func.uuid_generate_v4())
    user_uuid = Column(ForeignKey('user.user_uuid', ondelete='CASCADE'), nullable=True, index=True)

    subject = Column(String(64), nullable=False)
    content = Column(Text, nullable=False)
    created_on = Column(DateTime(True), nullable=False, server_default=func.now())
    user = relationship('User')


class Plan(BaseModel):
    __tablename__ = 'plan'
    TYPE = {1: 'switch pay per port', 2: 'switch pay per minute', 3: 'LRN pay per CPS', 4: 'LRN pay per DIP'}
    plan_uuid = Column(String(36), primary_key=True, default=generate_uuid_str(),
                       server_default=func.uuid_generate_v4())

    type = Column(ChoiceType(TYPE), default=1)
    amount = Column(Numeric, nullable=False, server_default='0')


class TransactionLog(BaseModel):
    __tablename__ = 'transaction_log'
    TYPE = {1: 'paypal', 2: 'stripe'}
    STATUS = {1: 'success', -1: 'fail'}
    transaction_log_uuid = Column(String(36), primary_key=True, default=generate_uuid_str(),
                          server_default=func.uuid_generate_v4())
    transaction_time = Column(DateTime(True), nullable=False, server_default=func.now())
    license_lrn_uuid = Column(String(36))
    license_switch_uuid = Column(String(36))
    type = Column(ChoiceType(TYPE), default=1)
    amount_total = Column(Numeric, nullable=False, server_default='0')
    amount_lrn = Column(Numeric, nullable=False, server_default='0')
    amount_switch = Column(Numeric, nullable=False, server_default='0')
    transaction_fee = Column(Numeric, nullable=False, server_default='0')
    transaction_id = Column(String(255))
    transaction_type = Column(String(255))
    from_ip = Column(String(36))
    transaction_src = Column(JSON())
    status = Column(ChoiceType(STATUS), default=-1)
    result = Column(Text())
    payment_uuid = Column(ForeignKey('payment.payment_uuid', ondelete='CASCADE'), index=True)


class Payment(BaseModel):
    __tablename__ = 'payment'
    TYPE = {1: 'paypal', 2: 'stripe'}
    payment_uuid = Column(String(36), primary_key=True, default=generate_uuid_str(),
                          server_default=func.uuid_generate_v4())
    user_uuid = Column(ForeignKey('user.user_uuid', ondelete='CASCADE'), index=True)
    license_lrn_uuid = Column(ForeignKey('license_lrn.license_lrn_uuid', ondelete='CASCADE'), nullable=True,
                              index=True)
    license_switch_uuid = Column(ForeignKey('license_switch.license_switch_uuid', ondelete='CASCADE'),
                                 nullable=True,
                                 index=True)
    switch_uuid = Column(String(64),index=True)
    amount_lrn = Column(Numeric, nullable=False, server_default='0')
    amount_switch = Column(Numeric, nullable=False, server_default='0')
    #amount_total = Column(Numeric, nullable=False, server_default='0')
    paid_time = Column(DateTime(True), nullable=False, server_default=func.now())
    type = Column(ChoiceType(TYPE), default=1)
    description = Column(Text)

    user = relationship('User')

    amount_total = column_property(amount_lrn.op('+')(amount_switch))
    user_email = column_property(select([User.email]).where(User.user_uuid == user_uuid).correlate_except(User))


    @property
    def license_uuid(self):
        if self.license_lrn_uuid:
            return self.license_lrn_uuid
        if self.license_switch_uuid:
            return self.license_switch_uuid
        return None

    @property
    def license(self):
        if self.license_lrn_uuid:
            return LicenseLrn.get(self.license_lrn_uuid)
        if self.license_switch_uuid:
            return LicenseSwitch.get(self.license_switch_uuid)
        return None

    def apply_mail(self, template_name):
        return _apply_mail(self, template_name, 'payment')


class PackageLrn(BaseModel):
    __tablename__ = 'package_lrn'
    TYPE = {3: 'LRN pay per CPS', 4: 'LRN pay per DIP'}
    package_lrn_uuid = Column \
        (String(36), primary_key=True, default=generate_uuid_str(),
         server_default=func.uuid_generate_v4())
    package_name = Column(String(64), unique=True)
    cps = Column(Integer())
    type = Column(ChoiceType(TYPE), default=3)
    lrn_port = Column(Integer())
    dip_count = Column(Integer())
    amount = Column(Integer())
    enabled = Column(Boolean, default=True)
    licenses = relationship('LicenseLrn', uselist=True, back_populates='package')
    create_on = Column(DateTime(True), nullable=True,server_default=func.now())


class LicenseLrn(BaseModel):
    __tablename__ = 'license_lrn'
    __table_args__ = (
        UniqueConstraint('package_lrn_uuid', 'user_uuid', name='uq_license_lrn_package_lrn_uuid_user_uuid'),
    )
    DURATION ={1:'1 month',3:'3 months',6:'6 months',12:'12 months'}
    license_lrn_uuid = Column \
        (String(36), primary_key=True, default=generate_uuid_str(),
         server_default=func.uuid_generate_v4())
    package_lrn_uuid = Column(ForeignKey('package_lrn.package_lrn_uuid', ondelete='CASCADE'), index=True)
    user_uuid = Column(ForeignKey('user.user_uuid', ondelete='CASCADE'), index=True)
    ip = Column(String(16), nullable=False, index=True)
    start_time = Column(DateTime(True), nullable=False, server_default=func.now())
    end_time = Column(DateTime(True), nullable=True)
    ordered_amount = Column(Integer)
    cost = Column(Numeric, nullable=False, server_default='0')
    is_enabled = Column(Boolean, default=True)
    duration = Column(ChoiceType(DURATION),server_default='1')

    package = relationship('PackageLrn', uselist=False, back_populates='licenses')
    user = relationship('User')

    user_email = column_property(
        select([User.email]).where(user_uuid == User.user_uuid).correlate_except(User))
    cps = column_property(
        select([PackageLrn.cps]).where(package_lrn_uuid == PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))
    type = column_property(
        select([PackageLrn.type]).where(package_lrn_uuid == PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))
    lrn_port = column_property(
        select([PackageLrn.lrn_port]).where(package_lrn_uuid == PackageLrn.package_lrn_uuid).correlate_except(
            PackageLrn))
    dip_count = column_property(
        select([PackageLrn.dip_count]).where(package_lrn_uuid == PackageLrn.package_lrn_uuid).correlate_except(
            PackageLrn))
    amount = column_property(
        select([PackageLrn.amount]).where(package_lrn_uuid == PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))
    enabled = column_property(select([and_(PackageLrn.enabled, is_enabled, end_time > func.now())]).where(
        package_lrn_uuid == PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))
    package_name = column_property(
        select([PackageLrn.package_name]).where(package_lrn_uuid == PackageLrn.package_lrn_uuid).correlate_except(PackageLrn))

    def renew(self):
        months = self.dur_months
        self.start_time = add_months(self.start_time, months)
        self.end_time = add_months(self.end_time, months)


    def apply_mail(self, template_name):
        return _apply_mail(self, template_name, 'license')

    @property
    def dur_months(self):
        return rev(self.DURATION)[self.duration]


    def add_history(self,gw):
        lic = self
        mcls = LrnPermissionUpdateHistory
        lic_user = lic.user
        return mcls(switch_ip=lic.ip, permit_cps=1000, client_name=lic_user.name,
                             operator=gw)

Payment.lrn_package_name = column_property(
        select([LicenseLrn.package_name]).where(Payment.license_lrn_uuid == LicenseLrn.license_lrn_uuid).correlate_except(LicenseLrn))

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
    #packages = relationship('PackageSwitch', uselist=True, back_populates='switch')


class PackageSwitch(BaseModel):
    __tablename__ = 'package_switch'
    TYPE = {1: 'switch pay per port', 2: 'switch pay per minute'}
    SUB_TYPE = {1: 'hosted_switch', 2: 'on_premise', 3: 'one_time'}
    package_switch_uuid = Column \
        (String(36), primary_key=True, default=generate_uuid_str(),
         server_default=func.uuid_generate_v4())

    package_name = Column(String(64), unique=True)

    type = Column(ChoiceType(TYPE), default=1)
    sub_type = Column(ChoiceType(SUB_TYPE), nullable=True)
    #switch_uuid = Column(String(128),index=True)
        #Column(ForeignKey('switch.switch_uuid', ondelete='CASCADE'), index=True)
    switch_port = Column(Integer())
    minute_count = Column(Integer())
    amount = Column(Integer())
    enabled = Column(Boolean, default=True)
    start_date = Column(DateTime(True), nullable=False, server_default=func.now())
    expire_date = Column(DateTime(True), nullable=True)
    create_on = Column(DateTime(True), nullable=True, server_default=func.now())

    licenses = relationship('LicenseSwitch', uselist=True, back_populates='package')
    #switch = relationship('Switch', uselist=False, back_populates='packages')
    rate_per_port = column_property(case([(switch_port > 0, cast(amount, Float).op('/')(switch_port))], else_=None))
    rate_per_minute = column_property(case([(minute_count > 0, cast(amount, Float).op('/')(minute_count))], else_=None))



class LicenseSwitch(BaseModel):
    __tablename__ = 'license_switch'
    __table_args__ = (
        UniqueConstraint('package_switch_uuid', 'user_uuid', name='uq_license_switch_package_switch_uuid_user_uuid'),
    )
    DURATION = {1: '1 month', 3: '3 months', 6: '6 months', 12: '12 months'}
    license_switch_uuid = Column \
        (String(36), primary_key=True, default=generate_uuid_str(),
         server_default=func.uuid_generate_v4())
    package_switch_uuid = Column(ForeignKey('package_switch.package_switch_uuid', ondelete='CASCADE'), index=True)
    ip = Column(String(16), nullable=False, index=True)
    user_uuid = Column(ForeignKey('user.user_uuid', ondelete='CASCADE'), index=True)
    start_time = Column(DateTime(True), nullable=False, server_default=func.now())
    end_time = Column(DateTime(True), nullable=True)
    ordered_amount = Column(Integer)
    cost = Column(Numeric, nullable=False, server_default='0')
    is_enabled = Column(Boolean, default=True)
    duration = Column(ChoiceType(DURATION), server_default='1')


    #switch_uuid = Column(ForeignKey('dnl_license_info.uuid', ondelete='CASCADE'), index=True)

    package = relationship('PackageSwitch', uselist=False, back_populates='licenses')
    user = relationship('User')

    user_email = column_property(
        select([User.email]).where(user_uuid == User.user_uuid).correlate_except(User))

    enabled = column_property(select([and_(PackageSwitch.enabled, is_enabled, end_time > func.now())]).where(
        package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(PackageSwitch))

    type = column_property(
        select([PackageSwitch.type]).where(package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(
            PackageSwitch))

    switch_uuid = Column(String(128), index=True)
    # switch_uuid = column_property(
    #     select([PackageSwitch.switch_uuid]).where(
    #         package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(PackageSwitch))

    switch_port = column_property(
        select([PackageSwitch.switch_port]).where(
            package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(
            PackageSwitch))
    minute_count = column_property(
        select([PackageSwitch.minute_count]).where(
            package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(
            PackageSwitch))
    amount = column_property(
        select([PackageSwitch.amount]).where(package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(
            PackageSwitch))
    package_name =column_property(
        select([PackageSwitch.package_name]).where(package_switch_uuid == PackageSwitch.package_switch_uuid).correlate_except(
            PackageSwitch))
    @property
    def dur_months(self):
        return rev(self.DURATION)[self.duration]

    def renew(self):
        months=self.dur_months
        self.start_time = add_months(self.start_time, months)
        self.end_time = add_months(self.end_time, months)

    def apply_mail(self, template_name):
        return _apply_mail(self, template_name, 'license')

    def add_history(self,gw):
        lic = self
        lic_user = lic.user
        icls = DnlLicenseInfo
        inq = icls.filter(icls.uuid == lic.switch_uuid).first()
        hist = None
        if inq:
            if lic.end_time:
                days = (lic.end_time - lic.start_time).days
            else:
                days = 89
            if lic.package.type == 'switch pay per port':
                mcls = LicenseUpdateHistory
                # mcls(uuid=lic.switch_uuid,license_channel=lic.amount,license_cps=inq.max_cps).save()
                hist = mcls(uuid=lic.switch_uuid, license_channel=lic.amount,
                            license_cps=inq.max_cps,
                            license_day=days, client_name=lic_user.name, operator=gw)
            if lic.package.type == 'switch pay per minute':
                mcls = LicenseUpdateHistory
                hist = mcls(uuid=lic.switch_uuid, license_channel=lic.amount,
                            license_cps=inq.max_cps,
                            license_day=days, client_name=lic_user.name, operator=gw)
        return hist


Payment.switch_package_name = column_property(
        select([LicenseSwitch.package_name]).where(Payment.license_switch_uuid == LicenseSwitch.license_switch_uuid).correlate_except(LicenseSwitch))

TransactionLog.license_lrn_plan_name = column_property(select([LicenseLrn.package_name]).where(TransactionLog.license_lrn_uuid==LicenseLrn.license_lrn_uuid).correlate_except(LicenseLrn))
TransactionLog.license_switch_plan_name = column_property(select([LicenseSwitch.package_name]).where(TransactionLog.license_switch_uuid==LicenseSwitch.license_switch_uuid).correlate_except(LicenseSwitch))

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


class DnlLicenseInfo(BaseModel):
    __tablename__ = 'dnl_license_info'

    id = Column(Integer, primary_key=True)#, server_default=text("nextval('dnl_license_info_id_seq'::regclass)"))
    carrier_name = Column(String(100), index=True)
    ss_type = Column(SmallInteger, nullable=False, index=True, server_default=text("0"))
    status = Column(SmallInteger, nullable=False, server_default=text("1"))
    ss_name = Column(String(100), nullable=False, index=True)
    uuid = Column(String(128), nullable=False, index=True)
    recv_ip = Column(String(16), nullable=False)
    recv_port = Column(Integer)
    ss_bind_mac = Column(String(18), nullable=False, index=True)
    ss_bind_ip = Column(String(16), nullable=False)
    ss_bind_port = Column(Integer)
    max_cap = Column(Integer, nullable=False, server_default=text("500"))
    max_cps = Column(Integer, nullable=False, server_default=text("100"))
    start_time = Column(DateTime(True), server_default=text("('now'::text)::date"))
    end_time = Column(DateTime(True), server_default=text("(('now'::text)::date + '3650 days'::interval)"))
    expires = Column(Integer, server_default=text("3650"))
    update_time = Column(DateTime(True))
    create_time = Column(DateTime(True) ,server_default=func.now())
    create_user = Column(SmallInteger, nullable=False, server_default=text("0"))

    # switch_uuid = column_property(uuid)
    # switch_ip = column_property(recv_ip)
    # port_limit = column_property(max_cap)
    # start_date = column_property(start_time)
    # expire_date  = column_property(end_time)
    switch_uuid = synonym('uuid')
    switch_ip = synonym('recv_ip')
    port_limit = synonym('max_cap')
    start_date = synonym('start_time')
    expire_date  = synonym('end_time')
    bstatus = column_property(status==1)
    plan_name = column_property(select([LicenseSwitch.package_name]).where(LicenseSwitch.switch_uuid==uuid).limit(1))




class DnlLcenseInfoRecord(BaseModel):
    __tablename__ = 'dnl_license_info_record'
    record_id=Column(Integer, nullable=False,primary_key=True)#, server_default=text("nextval('dnl_license_info_record_record_id_seq'::regclass)"))
    id=Column(Integer)
    carrier_name=Column(String(100))
    ss_type=Column(SmallInteger)
    status=Column(SmallInteger)
    ss_name=Column(String(100))
    uuid=Column(String(128))
    recv_ip=Column(String(16))
    recv_port=Column(Integer)
    ss_bind_mac=Column(String(18))
    ss_bind_ip=Column(String(16))
    ss_bind_port=Column(Integer)
    max_cap=Column(Integer)
    max_cps=Column(Integer)
    start_time=Column(DateTime(True))
    end_time=Column(DateTime(True))
    expires=Column(Integer)
    update_time=Column(DateTime(True))
    create_time=Column(DateTime(True))
    create_user=Column(SmallInteger)
    time=Column(Numeric)
    flag=Column(CHAR(1))


LicenseSwitch.switch_ip = column_property(select([DnlLicenseInfo.recv_ip]).where(LicenseSwitch.switch_uuid==DnlLicenseInfo.uuid).correlate_except(DnlLicenseInfo))


class DnlLicenseLog(BaseModel):
    __tablename__ = 'dnl_license_log'

    id = Column(Integer, primary_key=True)#, server_default=text("nextval('dnl_license_log_id_seq'::regclass)"))
    uuid = Column(String(128), nullable=False, index=True)
    recv_ip = Column(String(16), nullable=False, index=True)
    recv_port = Column(Integer)
    cap = Column(Integer, nullable=False, server_default=text("0"))
    cps = Column(Integer, nullable=False, server_default=text("0"))
    start_time = Column(DateTime(True))
    end_time = Column(DateTime(True))
    sip_addr = Column(String(256))
    status = Column(SmallInteger, nullable=False, server_default=text("0"))
    create_time = Column(DateTime(True), server_default=func.now())


class DnlPreLicensingInfo(BaseModel):
    __tablename__ = 'dnl_pre_licensing_info'

    id = Column(Integer, primary_key=True)#, server_default=text("nextval('dnl_pre_licensing_info_id_seq'::regclass)"))
    ip = Column(String(16), nullable=False)
    cap = Column(Integer, nullable=False, server_default=text("0"))
    cps = Column(Integer, nullable=False, server_default=text("0"))
    expires = Column(Integer)
    create_time = Column(DateTime(True),server_default=func.now())


class DnlPreLicensingInfoRecord(BaseModel):
    __tablename__ = 'dnl_pre_licensing_info_record'
    record_id=Column(Integer, nullable=False, primary_key=True)#server_default=text("nextval('dnl_pre_licensing_info_record_record_id_seq'::regclass)"))
    id=Column(Integer)
    ip=Column(String(16))
    cap=Column(Integer)
    cps=Column(Integer)
    expires=Column(Integer)
    create_time=Column(DateTime(True),server_default=func.now())
    time=Column(Numeric)
    flag=Column(CHAR(1))

class SwitchDaily(BaseModel):
    __tablename__ = 'switch_daily'
    id = Column(Integer, primary_key=True)
    client_id=Column(String(36), index=True)
    from_ip=Column(String(30), nullable=False, index=True)
    from_port=Column(Integer)
    max_cps=Column(Integer)
    max_cap=Column(Integer)
    call_duration=Column(Integer)
    detail=Column(String(1024))
    sip_addr=Column(String(250))
    start_date=Column(DateTime(True))
    report_date=Column(String(16), index=True)
    create_time=Column(DateTime(True), server_default=func.now())