from collections import OrderedDict

from falcon_rest.contrib.objects_history.object_revision import object_revision
from falcon_rest.conf import settings

import api_lic.views.public
import api_lic.views.user
from .settings import AUTH_END_POINT
from . import views
from . import auth
from . import file

_Auth = [
    dict(path=AUTH_END_POINT, method='post', resource=auth.auth_endpoints.Auth()),
    #dict(path=AUTH_END_POINT, method='post', resource=settings.get_auth_module().auth_endpoints.Auth()),
    #dict(path=AUTH_END_POINT, method='post', resource=settings.get_auth_module().auth_endpoints.Auth()),
    # settings.get_auth_module().auth_endpoints.Auth()),
    dict(path='/auth/check-password', method='post',
         resource=auth.auth_endpoints.PasswordCheck()),
    dict(path='/auth/check-token', method='post', resource=auth.auth_endpoints.TokenCheck()),
    dict(path='/auth/reset_email', method='post', resource=views.UserForgotPassword()),
    dict(path='/auth/reset_password/{token}', method='post', resource=views.UserResetPassword()),
    dict(path='/user', resource=views.UserCreate(), method='post'),
    dict(path='/user/{user_uuid}', resource=views.UserResource(), method='path'),
    dict(path='/user_by_email/{email}', resource=views.UserByEmailResource(), method='path'),
    dict(path='/user/list', resource=views.UserList(), method='get'),
    dict(path='/registration', resource=views.UserRegisterCreate(), method='post'),
    dict(path='/registration/confirm/{token}', resource=views.UserConfirmRegister(), method='post'),
]

_Admin = [
    dict(path='/plan', method='post', resource=views.PlanCreate()),
    dict(path='/plan/{plan_uuid}', method='path', resource=views.PlanResource()),
    dict(path='/notification', method='post', resource=views.NotificationCreate()),
    dict(path='/notification/{notification_uuid}', method='path', resource=views.NotificationResource()),

    dict(path='/package_lrn', method='post', resource=views.PackageLrnCreate()),
    dict(path='/package_lrn/{package_lrn_uuid}', method='path', resource=views.PackageLrnResource()),
    dict(path='/package_lrn/{package_lrn_uuid}/{user_uuid}', method='delete', resource=views.LicenseLrnAdminResource()),
    dict(path='/package_switch', method='post', resource=views.PackageSwitchCreate()),
    dict(path='/package_switch/{package_switch_uuid}', method='path', resource=views.PackageSwitchResource()),
    dict(path='/package_switch/{package_switch_uuid}/{user_uuid}', method='delete',
         resource=views.LicenseSwitchAdminResource()),
]
_Config = [
    dict(path='/config/payment', method='path', resource=views.ConfigPaymentResource()),
    dict(path='/email_template/{name}', method='path', resource=views.EmailTemplateResource()),
    dict(path='/email_template/list', method='get', resource=views.EmailTemplateList()),
]
_Public = [
    dict(path='/switch/list', method='get',resource=views.DnlLicenseInfoList() ),
    dict(path='/image', method='post', resource=views.SimpleFileCreate()),
    dict(path='/image/{file_name}', method='get', resource=views.SimpleFileGet()),
    dict(path='/file', method='post', resource=file.file_upload),
    dict(path='/file/download_link/{belongs_to_uuid}/{uuid}', method='get', resource=file.get_download_link),
    dict(path='/file/download/{download_token}', method='get', resource=file.file_download),
    dict(path='/file/{file_uuid}', method='get', resource=file.file_show),
    dict(path='/file/list', method='get', resource=file.ListFiles()),
    dict(path='/file/list_tmp', method='get', resource=file.ListTmpFiles()),
    dict(path='/package_lrn/list', method='get', resource=views.PackageLrnList()),
    dict(path='/package_switch/list', method='get', resource=views.PackageSwitchList()),
    dict(path='/package_switch_port/table', method='get', resource=views.PackageSwitchPortTableResource()),
    dict(path='/package_switch_minute/table', method='get', resource=views.PackageSwitchMinuteTableResource()),
]

_User = [
    dict(path='/home', resource=views.user.UserInfoResource(), method='path'),
    dict(path='/notification/list', method='get', resource=api_lic.views.user.NotificationList()),
    dict(path='/payment', method='post', resource=api_lic.views.user.PaymentCreate()),
    dict(path='/payment/{payment_uuid}', method='path', resource=api_lic.views.user.PaymentResource()),
    dict(path='/payment/list', method='get', resource=api_lic.views.user.PaymentList()),
    dict(path='/payment/paypal', method='post', resource=api_lic.views.user.PaypalWebhook()),
    dict(path='/payment/stripe', method='post', resource=api_lic.views.user.StripeWebhook()),
    dict(path='/license_lrn', method='post', resource=views.LicenseLrnCreate()),
    dict(path='/license_lrn/{license_lrn_uuid}', method='path', resource=views.LicenseLrnResource()),
    dict(path='/license_lrn/{license_lrn_uuid}/renew', method='path', resource=views.LicenseLrnRenewResource()),
    dict(path='/license_lrn/list', method='get', resource=views.LicenseLrnList()),
    dict(path='/license_switch', method='post', resource=views.LicenseSwitchCreate()),
    dict(path='/license_switch/{license_switch_uuid}', method='path', resource=views.LicenseSwitchResource()),
    dict(path='/license_switch/{license_switch_uuid}/renew', method='path',
         resource=views.LicenseSwitchRenewResource()),
    dict(path='/license_switch/list', method='get', resource=views.LicenseSwitchList()),
]

ROUTES = OrderedDict([
    ('Auth', dict(description='Authentication api', routes=_Auth)),
    ('Admin', dict(description='Admin api', routes=_Admin)),
    ('Config', dict(description='Config api', routes=_Config)),
    ('Public', dict(description='Public api', routes=_Public)),
    ('User', dict(description='User space api', routes=_User)),
])

