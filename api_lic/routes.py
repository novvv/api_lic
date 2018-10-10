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
           {'path': '/user/list', 'resource': view.UserList(), 'method': 'get'},

           {'path': '/registration', 'resource': view.UserRegisterCreate(), 'method': 'post'},
           {'path': '/registration/confirm/{token}', 'resource': views.UserConfirmRegister(), 'method': 'post'},
          ]

    }),
('Admin', {
        'description': 'public info',
        'routes': [
        {'path': '/rate', 'method': 'post','resource': views.RateCreate()},
        {'path': '/rate/{rate_uuid}', 'method': 'path','resource': views.RateResource()},
        {'path': '/notification', 'method': 'post', 'resource': views.NotificationCreate()},
        {'path': '/notification/{notification_uuid}', 'method': 'path', 'resource': views.NotificationResource()},
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
            {'path': '/rate/list', 'method': 'get','resource': api_lic.views.public.RateList()},

          ]

    }),
    ('User', {
        'description': 'User space',
        'routes': [
            {'path': '/home', 'resource': views.user.UserInfoResource(), 'method': 'path'},

{'path': '/license', 'method': 'post', 'resource': api_lic.views.user.LicenseCreate()},
{'path': '/license/{license_uuid}', 'method': 'path', 'resource': api_lic.views.user.LicenseResource()},
{'path': '/license/list', 'method': 'get', 'resource': api_lic.views.user.LicenseList()},
{'path': '/license_period', 'method': 'post', 'resource': api_lic.views.user.LicensePeriodCreate()},
{'path': '/license_period/{license_period_uuid}', 'method': 'path', 'resource': api_lic.views.user.LicensePeriodResource()},
{'path': '/license_period/list', 'method': 'get', 'resource': api_lic.views.user.LicensePeriodList()},

{'path': '/notification/list', 'method': 'get', 'resource': api_lic.views.user.NotificationList()},
{'path': '/payment', 'method': 'post', 'resource': api_lic.views.user.PaymentCreate()},
{'path': '/payment/{payment_uuid}', 'method': 'path', 'resource': api_lic.views.user.PaymentResource()},
{'path': '/payment/list', 'method': 'get', 'resource': api_lic.views.user.PaymentList()},
{'path': '/payment/webhook', 'method': 'post', 'resource': api_lic.views.user.PaymentWebhook()},

        ]

    }),
])

if settings.API_TEST_ROUTES == 'True':
    ROUTES = TEST_ROUTES
else:
    ROUTES = PRODUCTION_ROUTES