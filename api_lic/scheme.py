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
from .model import add_months
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
    phone = Str(required=True, allow_none=False, validate=[validate.Regexp(PHONE_REGEXP),
                                                           lambda value: _valid_unique('User', 'phone', value)])

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
        fields = ('email', 'passwd', 'first_name', 'last_name')


class UserInfoScheme(BaseModelScheme):
    first_name = Str(allow_none=True, required=False)
    last_name = Str(allow_none=True, required=False)
    passwd = Str(required=True)
    email = Email(validate=[validate.Email(error='Incorrect email address'),
                            lambda value: _valid_unique('User', 'email', value)])
    logo_file_uuid = FileSchemeField(model.FileModel, 'User', 'logo', required=False)
    alert_payment_received = Bool()
    alert_license_expired = Bool()
    alert_license_will_expired = Bool()
    alert_license_purchased = Bool()

    class Meta:
        model = model.User
        fields = ('passwd', 'email', 'alert_payment_received', 'alert_license_expired', 'alert_license_will_expired',
                  'alert_license_purchased', 'logo_file_uuid', 'first_name', 'last_name')


class UserInfoSchemeGet(UserInfoScheme):
    class Meta:
        model = model.User
        fields = ('user_uuid', 'user_type', 'last_login') + UserInfoScheme.Meta.fields


class UserInfoSchemeModify(BaseModelScheme):
    passwd = Str()
    email = Email()

    class Meta:
        model = model.User
        fields = ('passwd', 'email', 'logo_file_uuid', 'alert_payment_received', 'alert_license_expired',
                  'alert_license_will_expired',
                  'alert_license_purchased', 'first_name', 'last_name')


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
    email_cc = Emails(allow_none=True, required=False)
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

# +++ConfigPayment+++
class ConfigPaymentScheme(BaseModelScheme):
    id = Int()
    charge_type = Choice()
    stripe_email = Str(validate=[validate.Length(max=64)])
    stripe_skey = Str(validate=[validate.Length(max=64)])
    stripe_pkey = Str(validate=[validate.Length(max=64)])
    stripe_svc_charge = Float()
    stripe_test_mode = Bool()
    paypal_email = Str(validate=[validate.Length(max=64)])
    paypal_skey = Str(validate=[validate.Length(max=128)])
    paypal_pkey = Str(validate=[validate.Length(max=128)])
    paypal_svc_charge = Float()
    paypal_test_mode = Bool()
    confirm_enabled = Bool()
    email_confirm_to = Str(validate=[validate.Length(max=64)])
    notification_enabled = Bool()
    email_cc_to = Str(validate=[validate.Length(max=64)])

    class Meta:
        model = model.ConfigPayment
        fields = ('charge_type', 'stripe_email', 'stripe_skey',
                  'stripe_pkey', 'stripe_svc_charge', 'stripe_test_mode',
                  'paypal_email', 'paypal_skey', 'paypal_pkey', 'paypal_svc_charge', 'paypal_test_mode',
                  'confirm_enabled', 'email_confirm_to', 'notification_enabled', 'email_cc_to',)


class ConfigPaymentSchemeGet(ConfigPaymentScheme):
    class Meta:
        model = model.ConfigPayment
        fields = ('charge_type', 'stripe_email',  # 'stripe_skey',
                  'stripe_pkey', 'stripe_svc_charge', 'stripe_test_mode',
                  'paypal_email',  # 'paypal_skey',
                  'paypal_pkey', 'paypal_svc_charge', 'paypal_test_mode',
                  'confirm_enabled', 'email_confirm_to', 'notification_enabled', 'email_cc_to',)


class ConfigPaymentSchemeModify(ConfigPaymentScheme):
    pass


# ---ConfigPayment---


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
    license_lrn_uuid = Str(
        validate=[validate.Length(max=36), lambda value: _valid('LicenseLrn', 'license_lrn_uuid', value)])
    license_switch_uuid = Str(
        validate=[validate.Length(max=36), lambda value: _valid('LicenseSwitch', 'license_switch_uuid', value)])
    # switch_uuid = Str(validate=[validate.Length(max=64)])
    amount_lrn = Float()
    amount_switch = Float()
    paid_time = DateTime()
    type = Choice()

    class Meta:
        model = model.Payment
        fields = (
            'license_lrn_uuid', 'license_switch_uuid', 'amount_lrn', 'amount_switch', 'paid_time',
            'type')  # , 'switch_uuid')


class PaymentSchemeGet(PaymentScheme):
    description = Str()
    switch_package_name = Str()
    lrn_package_name = Str()
    user_email = Str()

    class Meta:
        model = model.Payment
        fields = (
            'payment_uuid', 'type', 'paid_time', 'user_uuid', 'license_lrn_uuid', 'license_switch_uuid', 'amount_lrn',
            'amount_switch', 'amount_total', 'switch_uuid', 'description', 'lrn_package_name', 'switch_package_name',
            'user_email'
        )
        search_fields = (
            'payment_uuid', 'type', 'period', 'user_uuid', 'license_lrn_uuid', 'license_switch_uuid', 'switch_uuid',
            'description', 'lrn_package_name', 'switch_package_name', 'user_email')
        query_fields = (
            'amount_lrn_gt', 'amount_lrn_lt', 'amount_switch_gt', 'amount_switch_lt', 'amount_total_gt',
            'amount_total_lt',
            'paid_time_gt', 'paid_time_lt',)


class PaymentSchemeModify(PaymentScheme):
    pass


# ---Payment---

# +++TransactionLog+++
class TransactionLogScheme(BaseModelScheme):
    transaction_log_uuid = Str(validate=[validate.Length(max=36)])
    transaction_time = DateTime()
    license_lrn_uuid = Str(validate=[validate.Length(max=36)])
    license_switch_uuid = Str(validate=[validate.Length(max=36)])
    type = Int()
    amount_total = Float()
    amount_lrn = Float()
    amount_switch = Float()
    transaction_id = Str(validate=[validate.Length(max=255)])
    transaction_type = Str(validate=[validate.Length(max=255)])
    from_ip = Str(validate=[validate.Length(max=36)])
    transaction_src = Dict()
    status = Int()
    result = Str()
    payment_uuid = Str(validate=[validate.Length(max=36)])

    class Meta:
        model = model.TransactionLog
        fields = ('transaction_time', 'license_lrn_uuid', 'license_switch_uuid', 'type', 'amount_total', 'amount_lrn',
                  'amount_switch', 'transaction_id', 'transaction_type', 'from_ip', 'transaction_src', 'status',
                  'result', 'payment_uuid',)


class TransactionLogSchemeGet(TransactionLogScheme):
    class Meta:
        model = model.TransactionLog
        fields = ('transaction_time', 'license_lrn_uuid', 'license_switch_uuid', 'type', 'amount_lrn', 'amount_switch',
                  'amount_total',
                  'transaction_id', 'transaction_type', 'from_ip', 'transaction_src', 'status', 'result',
                  'payment_uuid',)
        search_fields = ('license_lrn_uuid', 'license_switch_uuid', 'type', 'amount_lrn', 'amount_switch',
                         'transaction_id', 'transaction_type', 'from_ip', 'status', 'result',
                         'payment_uuid',)
        query_fields = ('transaction_time_gt', 'transaction_time_lt', 'amount_total_lt', 'amount_total_gt')


# +++Plan+++
class PlanScheme(BaseModelScheme):
    plan_uuid = Str(validate=[validate.Length(max=36)])
    type = Choice()
    plan = Float()

    class Meta:
        model = model.Plan
        fields = ('type', 'amount',)


class PlanSchemeGet(PlanScheme):
    class Meta:
        model = model.Plan
        fields = ('plan_uuid', 'type',)
        search_fields = ('plan_uuid', 'type',)
        query_fields = ('amount_gt', 'amount_lt',)


class PlanSchemeModify(PlanScheme):
    pass


# ---Plan---

# +++PackageLrn+++
class PackageLrnScheme(BaseModelScheme):
    package_lrn_uuid = Str(validate=[validate.Length(max=36)])
    package_name = Str(validate=[validate.Length(max=64)])
    cps = Int()
    type = Choice()
    lrn_port = Int()
    dip_count = Int()
    amount = Int()
    enabled = Bool()
    create_on = DateTime()
    licenses = Nested('LicenseLrnScheme', many=True)

    class Meta:
        model = model.PackageLrn
        fields = ('package_name', 'cps', 'type', 'lrn_port', 'dip_count', 'amount', 'enabled',)


class PackageLrnSchemeGet(PackageLrnScheme):
    class Meta:
        model = model.PackageLrn
        fields = (
            'package_lrn_uuid', 'package_name', 'cps', 'type', 'lrn_port', 'dip_count', 'amount', 'enabled',
            'create_on')
        search_fields = (
            'package_lrn_uuid', 'package_name', 'cps', 'type', 'lrn_port', 'dip_count', 'amount', 'enabled')
        query_fields = ('create_on_gt', 'create_on_lt',)


class PackageLrnSchemeModify(PackageLrnScheme):
    pass


# ---PackageLrn---

# +++DnlLicenseInfo+++
class DnlLicenseInfoScheme(BaseModelScheme):
    id = Int()
    carrier_name = Str(validate=[validate.Length(max=100)])
    ss_type = Int()
    status = Int()
    ss_name = Str(validate=[validate.Length(max=100)])
    uuid = Str(validate=[validate.Length(max=128)])
    recv_ip = Str(validate=[validate.Length(max=16)])
    recv_port = Int()
    ss_bind_mac = Str(validate=[validate.Length(max=18)])
    ss_bind_ip = Str(validate=[validate.Length(max=16)])
    ss_bind_port = Int()
    max_cap = Int()
    max_cps = Int()
    start_time = DateTime()
    end_time = DateTime()
    expires = Int()
    update_time = DateTime()
    create_time = DateTime()
    create_user = Int()

    class Meta:
        model = model.DnlLicenseInfo
        fields = (
            'carrier_name', 'ss_type', 'status', 'ss_name', 'uuid', 'recv_ip', 'recv_port', 'ss_bind_mac', 'ss_bind_ip',
            'ss_bind_port', 'max_cap', 'max_cps', 'start_time', 'end_time', 'expires', 'update_time', 'create_time',
            'create_user',)


class DnlLicenseInfoSchemeGet(DnlLicenseInfoScheme):
    status = Boolean(attribute='bstatus')

    class Meta:
        model = model.DnlLicenseInfo
        fields = ('switch_uuid', 'switch_ip', 'port_limit', 'start_date', 'expire_date', 'plan_name',
                  # 'uuid',
                  'id',
                  'carrier_name', 'ss_type', 'status', 'ss_name', 'recv_port', 'ss_bind_mac',
                  'ss_bind_ip', 'ss_bind_port', 'max_cps', 'expires', 'create_user',)
        search_fields = (
            'switch_uuid', 'switch_ip', 'port_limit', 'start_date', 'expire_date', 'plan_name',
            'id', 'carrier_name', 'ss_type', 'status', 'ss_name', 'uuid', 'recv_ip', 'recv_port', 'ss_bind_mac',
            'ss_bind_ip', 'ss_bind_port', 'max_cap', 'max_cps', 'expires', 'create_user',)
        query_fields = (
            'start_date_gt', 'start_date_lt', 'expire_date_gt', 'expire_date_lt', 'update_time_gt', 'update_time_lt',
            'create_time_gt', 'create_time_lt',)


class DnlLicenseInfoSchemeModify(DnlLicenseInfoScheme):
    pass


# ---DnlLicenseInfo---

# +++PackageSwitch+++
class PackageSwitchScheme(BaseModelScheme):
    package_switch_uuid = Str(validate=[validate.Length(max=36)])
    package_name = Str(validate=[validate.Length(max=64)])
    type = Choice()
    sub_type = Choice()
    switch_port = Int()
    minute_count = Int()
    amount = Int()
    enabled = Bool()
    start_date = DateTime()
    expire_date = DateTime()
    licenses = Nested('LicenseSwitchScheme', many=True)

    class Meta:
        model = model.PackageSwitch
        fields = ('package_name', 'type', 'sub_type', 'switch_uuid', 'switch_port', 'minute_count', 'amount', 'enabled',
                  'start_date', 'expire_date')


class PackageSwitchSchemeGet(PackageSwitchScheme):
    create_on = DateTime()

    class Meta:
        model = model.PackageSwitch
        fields = (
            'package_switch_uuid', 'package_name', 'type', 'sub_type', 'switch_port', 'minute_count',
            'amount', 'enabled', 'start_date', 'expire_date', 'create_on')
        search_fields = (
            'package_switch_uuid', 'package_name', 'type', 'sub_type', 'switch_port', 'minute_count',
            'amount', 'enabled')
        query_fields = (
            'start_date_gt', 'start_date_lt', 'expire_date_gt', 'expire_date_lt', 'create_on_gt', 'create_on_lt',)


class PackageSwitchSchemeModify(PackageSwitchScheme):
    pass


class PackageSwitchPortScheme(BaseModelScheme):
    package_switch_uuid = Str(validate=[validate.Length(max=36)])
    package_name = Str(validate=[validate.Length(max=64)])
    amount = Int()
    rate_per_port = Float()
    enabled = Bool()

    class Meta:
        model = model.PackageSwitch
        fields = ('package_switch_uuid', 'package_name', 'amount', 'rate_per_port', 'enabled',)


class PackageSwitchMinuteScheme(BaseModelScheme):
    package_switch_uuid = Str(validate=[validate.Length(max=36)])
    package_name = Str(validate=[validate.Length(max=64)])
    amount = Int()
    enabled = Bool()
    rate_per_minute = Float()

    class Meta:
        model = model.PackageSwitch
        fields = ('package_switch_uuid', 'package_name', 'amount', 'enabled', 'rate_per_minute')


class PackageSwitchPortTableInnerScheme(Schema):
    switch_port = Int()
    hosted_switch = Nested('PackageSwitchPortScheme')
    on_premise = Nested('PackageSwitchPortScheme')
    one_time = Nested('PackageSwitchPortScheme')


class PackageSwitchPortTableScheme(Schema):
    items = Nested('PackageSwitchPortTableInnerScheme', many=True)


class PackageSwitchMinuteTableInnerScheme(Schema):
    minute_count = Int()
    hosted_switch = Nested('PackageSwitchMinuteScheme')
    on_premise = Nested('PackageSwitchMinuteScheme')


class PackageSwitchMinuteTableScheme(Schema):
    items = Nested('PackageSwitchMinuteTableInnerScheme', many=True)


# ---PackageSwitch---
# +++LicenseLrn+++
class LicenseLrnScheme(BaseModelScheme):
    user_email = Str(validate=[validate.Length(max=128)])
    cps = Int()
    type = Int()
    ip = Str(required=True, allow_none=False, validate=[validate.Length(max=16), validate.Regexp(IP_REGEXP)])
    lrn_port = Int()
    dip_count = Int()
    amount = Int()
    license_lrn_uuid = Str(validate=[validate.Length(max=36)])
    package_lrn_uuid = Str(
        validate=[validate.Length(max=36), lambda value: _valid('PackageLrn', 'package_lrn_uuid', value)])
    user_uuid = Str(validate=[validate.Length(max=36)])
    start_time = DateTime()
    end_time = DateTime()
    duration = Choice()
    ordered_amount = Int()
    cost = Float()
    package = Nested('PackageLrnScheme', many=False)
    enabled = Bool()

    class Meta:
        model = model.LicenseLrn
        fields = ('package_lrn_uuid', 'ip', 'start_time', 'duration')


class LicenseLrnSchemeGet(LicenseLrnScheme):
    class Meta:
        model = model.LicenseLrn
        fields = ('user_email', 'cps', 'type', 'ip', 'lrn_port', 'dip_count', 'amount', 'license_lrn_uuid',
                  'package_lrn_uuid', 'user_uuid', 'package', 'start_time', 'end_time', 'enabled', 'duration')
        search_fields = ('user_email', 'cps', 'type', 'ip', 'lrn_port', 'dip_count', 'amount', 'license_lrn_uuid',
                         'package_lrn_uuid', 'user_uuid', 'ordered_amount', 'enabled', 'duration')
        query_fields = ('start_time_gt', 'start_time_lt', 'end_time_gt', 'end_time_lt', 'cost_gt', 'cost_lt',)


class LicenseLrnSchemeModify(LicenseLrnScheme):
    ip = Str(validate=[validate.Length(max=16), validate.Regexp(IP_REGEXP)])
    enabled = Bool(attribute='is_enabled')

    class Meta:
        model = model.LicenseLrn
        fields = ('package_lrn_uuid', 'ip', 'enabled', 'end_time')


# ---LicenseLrn---
# +++LicenseSwitch+++
class LicenseSwitchScheme(BaseModelScheme):
    user_email = Str(validate=[validate.Length(max=128)])
    type = Int()
    ip = Str(required=True, allow_none=False, validate=[validate.Length(max=16), validate.Regexp(IP_REGEXP)])
    switch_port = Int()
    minute_count = Int()
    amount = Int()
    license_switch_uuid = Str(validate=[validate.Length(max=36)])
    package_switch_uuid = Str(
        validate=[validate.Length(max=36), lambda value: _valid('PackageSwitch', 'package_switch_uuid', value)])
    user_uuid = Str(validate=[validate.Length(max=36), lambda value: _valid('User', 'user_uuid', value)])
    start_time = DateTime()
    end_time = DateTime()
    duration = Choice()
    ordered_amount = Int()
    cost = Float()
    package = Nested('PackageSwitchScheme', many=False)
    enabled = Bool()
    switch_uuid = Str(validate=[validate.Length(max=64), lambda value: _valid('DnlLicenseInfo', 'uuid', value)])
    class Meta:
        model = model.LicenseSwitch
        fields = ('package_switch_uuid', 'ip', 'start_time', 'duration','switch_uuid')


class LicenseSwitchSchemeGet(LicenseSwitchScheme):
    class Meta:
        model = model.LicenseSwitch
        fields = ('user_email', 'type', 'ip', 'switch_port', 'minute_count', 'amount', 'license_switch_uuid',
                  'package_switch_uuid', 'user_uuid', 'ordered_amount', 'package', 'enabled', 'start_time', 'end_time',
                  'duration','switch_uuid')
        search_fields = (
            'user_email', 'type', 'ip', 'switch_port', 'minute_count', 'amount', 'license_switch_uuid',
            'package_switch_uuid', 'user_uuid', 'ordered_amount', 'package', 'enabled', 'duration','switch_uuid')
        query_fields = ('start_time_gt', 'start_time_lt', 'end_time_gt', 'end_time_lt', 'cost_gt', 'cost_lt',)


class LicenseSwitchSchemeModify(LicenseSwitchScheme):
    ip = Str(validate=[validate.Length(max=16), validate.Regexp(IP_REGEXP)])
    enabled = Bool(attribute='is_enabled')

    class Meta:
        model = model.LicenseSwitch
        fields = ('package_switch_uuid', 'ip', 'enabled', 'end_time')


# ---LicenseSwitch---


### end ###
