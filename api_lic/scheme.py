# from falcon_rest.db import fields, orm
# from falcon_rest import resources
import falcon_rest.schemes
from .base_model_scheme import BaseModelScheme
from falcon_rest.schemes import CHOICES_VALIDATION_ERR_MESSAGE
# from falcon_rest.db import Column
from falcon_rest.conf import settings
from falcon_rest.contrib.files import create_file_model_class, create_scheme
# from falcon_rest.contrib.files.endpoints import UploadFile, GetDownloadLink, DownloadFile, ShowFile
# from marshmallow_sqlalchemy import field_for, fields as sa
from falcon_rest.contrib.objects_history.object_revision.object_revision import ObjectRevisionSchemeGet

from sqlalchemy import inspect
from marshmallow import (
    Schema, pre_load, pre_dump, post_dump, post_load, validates_schema,
    validate, validates, fields, ValidationError
)
from marshmallow.fields import (
    Field, Raw, Nested, Dict, List, String, UUID, Number, Integer, Decimal, Boolean,
    FormattedString, Float, DateTime, LocalDateTime, Time, Date, TimeDelta, Url, URL,
    Email, Method, Function, Str, Bool, Int, Constant)
from falcon_rest.contrib.files.models import FileSchemeField, FileModelField
from .base_model import BaseModel
from . import model
from datetime import datetime
from dateutil.parser import parse as parse_datetime
from email.utils import parseaddr
from .fields import Choice

from falcon_rest.responses import UnauthenticatedErrorResponse, ForbiddenErrorResponse

IP_REGEXP_DOMAIN = "^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])" \
                   "(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$"
IP_REGEXP = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|localhost$"
DATE_REGEXP = r'^(0?[1-9]|1[012])/(0?[1-9]|[1-2][0-9]|3[01])/[12][09][0-9][0-9]$|' \
              r'^[12][09][0-9][0-9]-(0?[1-9]|1[012])-(0?[1-9]|[1-2][0-9]|3[01])$|' \
              r'^(0?[1-9]|1[012])-[12][09][0-9][0-9]-(0?[1-9]|[1-2][0-9]|3[01])$|' \
              r'^(0?[1-9]|1[012])/[12][09][0-9][0-9]/(0?[1-9]|[1-2][0-9]|3[01])$|' \
              r'^[12][09][0-9][0-9]/(0?[1-9]|1[012])/(0?[1-9]|[1-2][0-9]|3[01])$'
TIME_REGEXP = r'(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])'
TIMEZONE_REGEXP = r'^(?:Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])$'
PHONE_REGEXP = r'^\+?[0-9]+$'
DIGITS_REGEXP = r'^[0-9]+$'
PREFIX_REGEXP = r'^[0-9,#]*$'
NAME_REGEXP = "^(\w[ _\-]?)*\w$"
USERNAME_REGEXP = "^(\w[ _\-\.\@]?)*\w$"


def valid_date(d):
    try:
        if len(str(d)) != 10:
            raise ValidationError('Invalid date "{}" must be in format "YYYY-MM-DD"'.format(d))
        parse_datetime(str(d))
        return True
    except ValueError:
        raise ValidationError('Invalid date {}'.format(d))


def _emails_validate(value):
    lst = value.split(';')
    for addr in lst:
        if addr == '':
            continue
        name, email = parseaddr(addr)
        validate.Email(error='invalid emails')(email)


class Emails(String):
    def __init__(self, *args, **kwargs):
        String.__init__(self, *args, **kwargs)
        # Insert validation into self.validators so that multiple errors can be
        # stored.
        self.validators.insert(0, _emails_validate)

    def _validated(self, value):
        """Format the value or raise a :exc:`ValidationError` if an error occurs."""
        if value is None:
            return None
        _emails_validate(value)
        return value


def valid_dict(d):
    return validate.OneOf(choices=d.values(), labels=d.keys(), error=CHOICES_VALIDATION_ERR_MESSAGE)


def plain(data, key):
    if key in data:
        temp = data[key]
        del data[key]
        data.update(temp)
    return data


def _valid(cls_name, field, value, msg=''):
    cls = model.__dict__[cls_name]
    fld = getattr(cls, field)
    # if type(value) == type('') or (not getattr(value, 'urn', None) is None and 'uuid' in getattr(value, 'urn', None)):
    #    value = "'" + str(value) + "'"
    # if not cls.filter(model.text_('{}={}'.format(field, value))).first():
    if not cls.filter(fld == value).first():
        if msg:
            raise ValidationError(msg)
        else:
            raise ValidationError('{} {} is invalid (not exists)'.format(field, value))


def _valid_unique(cls_name, field, value, msg=''):
    cls = model.__dict__[cls_name]
    fld = getattr(cls, field)

    # if type(value) == type('') or (not getattr(value, 'urn', None) is None and 'uuid' in getattr(value, 'urn', None)):
    #    value = "'" + value + "'"
    if cls.filter(fld == value).first():
        if msg:
            raise ValidationError(msg)
        else:
            raise ValidationError('{} {} already exist (duplicate) '.format(field, value))


# +++ Revisions


class ObjectRevisionFilterSchemeGet(ObjectRevisionSchemeGet):
    class Meta:
        model = model.ObjectRevisionModel
        search_fields = ('user_id', 'entity_name', 'entity_pk', 'action', 'revision_number')
        query_fields = ('revision_time_gt', 'revision_time_lt')


class UserScheme(BaseModelScheme):
    passwd = Str()
    is_admin = Bool()
    is_active = Bool()
    email = Email(allow_none=True, validate=[validate.Email(error='Incorrect email address'),
                                             lambda value: _valid_unique('User', 'email', value)])
    logo_file_uuid = FileSchemeField(model.FileModel, 'User', 'logo', required=False)

    class Meta:
        model = model.User
        fields = ('passwd', 'is_admin', 'email', 'is_active')


class UserScheme(BaseModelScheme):
    user_id = Str()

    email = Email(required=True, allow_none=False, validate=[validate.Email(error='Incorrect email address'),
                                                             lambda value: _valid_unique('User', 'email', value)])
    password = Str(validate=[validate.Length(max=72)])
    is_admin = Bool()
    last_login = DateTime()
    is_active = Bool()
    created_on = DateTime()

    logo_file_uuid = FileSchemeField(model.FileModel, 'User', 'logo', required=False)
    logo = Nested('FileModelScheme', many=False)

    class Meta:
        model = model.User
        fields = ('email', 'passwd', 'is_admin', 'is_active', 'logo_file_uuid')


class UserSchemeGet(UserScheme):
    role_name = Str(validate=validate.OneOf(('admin', 'user')))

    class Meta:
        fields = ('user_uuid', 'created_on', 'last_login',
                  'role_name') + UserScheme.Meta.fields
        search_fields = ('user_uuid', 'role_name') + UserScheme.Meta.fields
        query_fields = ('last_login_gte', 'last_login_lt', 'created_on_gt', 'created_on_gt',)
        model = model.User


class UserSchemeModify(UserScheme):
    email = Email()
    user_name = Str()


class UserRegisterScheme(UserScheme):
    class Meta:
        model = model.User
        fields = ('email', 'passwd',)


class UserInfoScheme(BaseModelScheme):
    first_name = Str(allow_none=True, required=False)
    last_name = Str(allow_none=True, required=False)
    passwd = Str(required=True)
    email = Email(validate=[validate.Email(error='Incorrect email address'),
                            lambda value: _valid_unique('User', 'email', value)])
    logo_file_uuid = FileSchemeField(model.FileModel, 'User', 'logo', required=False)
    phone = Str(allow_none=True, required=False, validate=validate.Regexp(PHONE_REGEXP))

    class Meta:
        model = model.User
        fields = ('passwd', 'email')


class UserInfoSchemeGet(UserInfoScheme):
    class Meta:
        model = model.User
        fields = ('user_uuid', 'user_type', 'last_login') + UserInfoScheme.Meta.fields


class UserInfoSchemeModify(BaseModelScheme):
    passwd = Str()
    email = Email()

    class Meta:
        model = model.User
        fields = ('passwd', 'email',)


class UserMinScheme(UserScheme):
    pass


class UserInnerScheme(UserScheme):
    pass


class UserResetPasswordLetterScheme(BaseModelScheme):
    email = Email()

    class Meta:
        model = model.User
        fields = ('email',)


class UserConfirmRegisterScheme(Schema):
    pass


class UserResetPasswordScheme(BaseModelScheme):
    passwd = Str()

    class Meta:
        model = model.User
        fields = ('passwd',)


# --- User


class EmailTemplateScheme(BaseModelScheme):
    name = Str(validate=validate.Regexp(NAME_REGEXP))
    subject = Str()
    email_from = Email()
    email_cc = Emails()
    content_text = Str()
    content_html = Str()
    hint = Str()

    class Meta:
        model = model.EmailTemplate
        fields = ('name', 'subject', 'email_from', 'email_cc', 'content_text', 'content_html', 'hint')


class EmailTemplateSchemeGet(EmailTemplateScheme):
    class Meta:
        model = model.EmailTemplate
        fields = ('name', 'subject', 'email_from', 'email_cc', 'content_text', 'content_html', 'hint')


### end ###

### begin ###
# +++License+++
class LicenseScheme(BaseModelScheme):
    license_uuid = Str(validate=[validate.Length(max=36)])
    rate_uuid = Str(validate=[validate.Length(max=36)])
    user_uuid = Str(validate=[validate.Length(max=36)])
    periods = Nested('LicensePeriodScheme', many=True)
    lrn = Nested('LicenseLrnScheme', many=False)
    switch = Nested('LicenseSwitchScheme', many=False)

    class Meta:
        model = model.License
        fields = ('rate_uuid', 'lrn', 'switch', 'periods')


class LicenseSchemeGet(LicenseScheme):
    periods = Nested('LicensePeriodSchemeGet', many=True)
    type = String()
    is_lrn_license = Bool()
    is_switch_license = Bool()

    class Meta:
        model = model.License
        fields = ('license_uuid', 'rate_uuid', 'periods', 'lrn', 'switch', 'periods', 'user_uuid', 'user_email', 'type',
                  'is_lrn_license', 'is_switch_license')
        search_fields = (
        'license_uuid', 'rate_uuid', 'user_uuid', 'user_email', 'type', 'is_lrn_license', 'is_switch_license')


class LicenseSchemeModify(LicenseScheme):
    pass


# ---License---
# +++LicenseLrn+++
class LicenseLrnScheme(BaseModelScheme):
    license_uuid = Str(validate=[validate.Length(max=36)])
    cps = Int()
    type = Choice()
    license = Nested('LicenseScheme', many=False)

    class Meta:
        model = model.LicenseLrn
        fields = ('cps', 'type')


class LicenseLrnSchemeGet(LicenseLrnScheme):
    class Meta:
        model = model.LicenseLrn
        fields = ('license_uuid', 'cps', 'license', 'type')
        search_fields = ('license_uuid', 'cps', 'license', 'type')


class LicenseLrnSchemeModify(LicenseLrnScheme):
    pass


# ---LicenseLrn---
# +++LicensePeriod+++
class LicensePeriodScheme(BaseModelScheme):
    license_period_uuid = Str(validate=[validate.Length(max=36)])
    license_uuid = Str(validate=[validate.Length(max=36)])

    start_time = DateTime()
    end_time = DateTime()
    cost = Float()
    license = Nested('LicenseScheme', many=False)
    payment = Nested('PaymentScheme', many=False)

    class Meta:
        model = model.LicensePeriod
        fields = ('start_time', 'end_time')


class LicensePeriodSchemeGet(LicensePeriodScheme):
    class Meta:
        model = model.LicensePeriod
        fields = ('license_period_uuid', 'license_uuid', 'user_uuid') + LicensePeriodScheme.Meta.fields
        search_fields = ('license_period_uuid', 'license_uuid', 'user_uuid')
        query_fields = ('start_time_gt', 'start_time_lt', 'end_time_gt', 'end_time_lt', 'cost_gt', 'cost_lt',)


class LicensePeriodSchemeModify(LicensePeriodScheme):
    pass


# ---LicensePeriod---
# +++LicenseSwitch+++
class LicenseSwitchScheme(BaseModelScheme):
    license_uuid = Str(validate=[validate.Length(max=36)])
    ip = Str(validate=[validate.Length(max=16)])
    type = Choice()
    license = Nested('LicenseScheme', many=False)

    class Meta:
        model = model.LicenseSwitch
        fields = ('ip', 'type')


class LicenseSwitchSchemeGet(LicenseSwitchScheme):
    class Meta:
        model = model.LicenseSwitch
        fields = ('license_uuid', 'ip', 'license', 'type')
        search_fields = ('license_uuid', 'ip', 'license', 'type')


class LicenseSwitchSchemeModify(LicenseSwitchScheme):
    pass


# ---LicenseSwitch---
# +++Notification+++
class NotificationScheme(BaseModelScheme):
    notification_uuid = Str(validate=[validate.Length(max=36)])
    user_uuid = Str(validate=[validate.Length(max=36)])
    subject = Str(validate=[validate.Length(max=64)])
    content = Str()
    created_on = DateTime()

    class Meta:
        model = model.Notification
        fields = ('user_uuid', 'subject', 'content', 'created_on',)


class NotificationSchemeGet(NotificationScheme):
    class Meta:
        model = model.Notification
        fields = ('notification_uuid', 'user_uuid', 'subject', 'content',)
        search_fields = ('notification_uuid', 'user_uuid', 'subject', 'content',)
        query_fields = ('created_on_gt', 'created_on_lt',)


class NotificationSchemeModify(NotificationScheme):
    pass


# ---Notification---
# +++Payment+++
class PaymentScheme(BaseModelScheme):
    payment_uuid = Str(validate=[validate.Length(max=36)])
    license_period_uuid = Str(validate=[validate.Length(max=36)])
    amount = Float()
    paid_time = DateTime()
    type = Choice()
    period = Nested('LicensePeriodScheme', many=False)

    class Meta:
        model = model.Payment
        fields = ('license_period_uuid', 'amount', 'paid_time', 'type',)


class PaymentSchemeGet(PaymentScheme):
    class Meta:
        model = model.Payment
        fields = ('payment_uuid', 'license_period_uuid', 'type', 'period', 'user_uuid')
        search_fields = ('payment_uuid', 'license_period_uuid', 'type', 'period', 'user_uuid')
        query_fields = ('amount_gt', 'amount_lt', 'paid_time_gt', 'paid_time_lt',)


class PaymentSchemeModify(PaymentScheme):
    pass


# ---Payment---
# +++Rate+++
class RateScheme(BaseModelScheme):
    rate_uuid = Str(validate=[validate.Length(max=36)])
    type = Choice()
    rate = Float()

    class Meta:
        model = model.Rate
        fields = ('type', 'rate',)


class RateSchemeGet(RateScheme):
    class Meta:
        model = model.Rate
        fields = ('rate_uuid', 'type',)
        search_fields = ('rate_uuid', 'type',)
        query_fields = ('rate_gt', 'rate_lt',)


class RateSchemeModify(RateScheme):
    pass
# ---Rate---
### end ###
