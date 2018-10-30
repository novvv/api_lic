from collections import OrderedDict

from  falcon_rest.contrib.objects_history.object_revision import object_revision
from falcon_rest.conf import settings

import api_lic.views.public
import api_lic.views.user
from . settings import AUTH_END_POINT
from . import views
from . import view
from . import auth
from . import file
TEST_ROUTES = OrderedDict([
    ('Test', {
        'description': 'This is a set of test functions',
        'routes': [
            {'path': AUTH_END_POINT, 'method': 'post', 'resource': auth.auth_endpoints.Auth()},
        ]
        }
     )
    ])
PRODUCTION_ROUTES = OrderedDict([
    ('Auth', {
        'description': 'Authentication functions',
        'routes': [
            {'path': '/auth', 'method': 'post','resource': auth.auth_endpoints.Auth()},#settings.get_auth_module().auth_endpoints.Auth()},
            {'path': '/auth/check-password', 'method': 'post',
                    'resource': settings.get_auth_module().auth_endpoints.PasswordCheck()},
            {'path': '/auth/check-token', 'method': 'post',
                  'resource': settings.get_auth_module().auth_endpoints.TokenCheck() },
           {'path': '/auth/reset_email', 'method': 'post','resource': views.UserForgotPassword()},
           {'path': '/auth/reset_password/{token}', 'method': 'post','resource': views.UserResetPassword()},
           {'path': '/user', 'resource': view.UserCreate(), 'method': 'post'},
           {'path': '/user/{user_uuid}', 'resource': view.UserResource(), 'method': 'path'},
           {'path': '/user_by_email/{email}', 'resource': view.UserByEmailResource(), 'method': 'path'},
           {'path': '/user/list', 'resource': view.UserList(), 'method': 'get'},

           {'path': '/registration', 'resource': view.UserRegisterCreate(), 'method': 'post'},
           {'path': '/registration/confirm/{token}', 'resource': views.UserConfirmRegister(), 'method': 'post'},
          ]

    }),
('Admin', {
        'description': 'public info',
        'routes': [
            {'path': '/plan', 'method': 'post','resource': views.PlanCreate()},
            {'path': '/plan/{plan_uuid}', 'method': 'path','resource': views.PlanResource()},
            {'path': '/notification', 'method': 'post', 'resource': views.NotificationCreate()},
            {'path': '/notification/{notification_uuid}', 'method': 'path', 'resource': views.NotificationResource()},
            {'path': '/email_template/{name}', 'method': 'path','resource': views.EmailTemplateResource()},
            {'path': '/email_template/list', 'method': 'get','resource': views.EmailTemplateList()},
            {'path': '/package_lrn', 'method': 'post','resource': views.PackageLrnCreate()},
            {'path': '/package_lrn/{package_lrn_uuid}', 'method': 'path','resource': views.PackageLrnResource()},
            {'path': '/package_lrn/{package_lrn_uuid}/{user_uuid}', 'method': 'delete','resource': views.LicenseLrnAdminResource()},
            {'path': '/switch', 'method': 'post','resource': views.SwitchCreate()},
            {'path': '/switch/{switch_uuid}', 'method': 'path','resource': views.SwitchResource()},
            {'path': '/switch/list', 'method': 'get','resource': views.SwitchList()},
            {'path': '/package_switch', 'method': 'post','resource': views.PackageSwitchCreate()},
            {'path': '/package_switch/{package_switch_uuid}', 'method': 'path','resource': views.PackageSwitchResource()},
            {'path': '/package_switch/{package_switch_uuid}/{user_uuid}', 'method': 'delete','resource': views.LicenseSwitchAdminResource()},
        ]}
 ),
    ('Public', {
        'description': 'public info',
        'routes': [
            {'path': '/image', 'method': 'post','resource': views.SimpleFileCreate()},
            {'path': '/image/{file_name}', 'method': 'get','resource': views.SimpleFileGet()},
            {'path': '/file', 'method': 'post', 'resource': file.file_upload},
            {'path': '/file/download_link/{belongs_to_uuid}/{uuid}', 'method': 'get', 'resource': file.get_download_link},
            {'path': '/file/download/{download_token}', 'method': 'get', 'resource': file.file_download},
            {'path': '/file/{file_uuid}', 'method': 'get', 'resource': file.file_show},
            {'path': '/file/list', 'method': 'get', 'resource': file.ListFiles()},
            {'path': '/file/list_tmp', 'method': 'get', 'resource': file.ListTmpFiles()},
            {'path': '/package_lrn/list', 'method': 'get', 'resource': views.PackageLrnList()},
            {'path': '/package_switch/list', 'method': 'get','resource': views.PackageSwitchList()},
          ]

    }),
    ('User', {
        'description': 'User space',
        'routes': [
            {'path': '/home', 'resource': views.user.UserInfoResource(), 'method': 'path'},

            {'path': '/notification/list', 'method': 'get', 'resource': api_lic.views.user.NotificationList()},
            {'path': '/payment', 'method': 'post', 'resource': api_lic.views.user.PaymentCreate()},
            {'path': '/payment/{payment_uuid}', 'method': 'path', 'resource': api_lic.views.user.PaymentResource()},
            {'path': '/payment/list', 'method': 'get', 'resource': api_lic.views.user.PaymentList()},
            {'path': '/payment/paypal', 'method': 'post', 'resource': api_lic.views.user.PaypalWebhook()},
            {'path': '/payment/stripe', 'method': 'post', 'resource': api_lic.views.user.StripeWebhook()},

            {'path': '/license_lrn', 'method': 'post', 'resource': views.LicenseLrnCreate()},
            {'path': '/license_lrn/{license_lrn_uuid}', 'method': 'path', 'resource': views.LicenseLrnResource()},
            {'path': '/license_lrn/list', 'method': 'get', 'resource': views.LicenseLrnList()},

            {'path': '/license_switch', 'method': 'post', 'resource': views.LicenseSwitchCreate()},
            {'path': '/license_switch/{license_switch_uuid}', 'method': 'path', 'resource': views.LicenseSwitchResource()},
            {'path': '/license_switch/list', 'method': 'get', 'resource': views.LicenseSwitchList()},


        ]

    }),
])

if settings.API_TEST_ROUTES == 'True':
    ROUTES = TEST_ROUTES
else:
    ROUTES = PRODUCTION_ROUTES