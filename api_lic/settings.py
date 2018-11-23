import os
from .__version__ import __version__
import configparser

API_INI = 'api.ini'

config = configparser.ConfigParser(interpolation=None)
config.read(API_INI)
_p_changed = False

def conf_get(name,default,sec='DEFAULT'):
    global _p_changed
    if not sec in config:
        config.add_section(sec)
        _p_changed = True
    if not name in config[sec]:
        config[sec][name]=default
        _p_changed = True
        return default
    else:
        return config[sec][name]

LOG_FILE = conf_get('LOG_FILE','lic.log')
LOG_LEVEL = conf_get('LOG_LEVEL','debug')
LOG_TO_CONSOLE = True if conf_get('LOG_TO_CONSOLE','True') == 'True' else False
LOG_FORMAT = conf_get('LOG_FORMAT', '%(asctime)s [%(levelname)s] \'%(message)s\' at %(filename)s: %(lineno)s')
ALLOW_ORIGINS = conf_get('ALLOW_ORIGIN', '*').split(' ')
ALLOW_ORIGIN = conf_get('ALLOW_ORIGIN', '*').split(' ')
API_TITLE = 'LICENSE API'
API_HOST = conf_get('API_HOST', 'localhost:8012')
API_SCHEME = conf_get('API_SCHEMA', 'http://')
API_BASE_PATH = conf_get('API_BASE_PATH', '/v1')
API_TEST_ROUTES = conf_get('API_TEST_ROUTES', 'False')
DB_CONN_STRING = conf_get('DB_CONN_STRING','')
DB_CONN_STRING_TEST = conf_get('DB_CONN_STRING_TEST', '')

CREATE_TABLES = True if conf_get('CREATE_TABLES', 'False') == 'True' else False

JWT_SIGNATURE = conf_get('JWT_SIGNATURE','')
JWT_TTL_DAYS = int(conf_get('JWT_TTL_DAYS', '1'))
JWT_REFRESH_THRESHOLD_DAYS = int(conf_get('JWT_REFRESH_THRESHOLD_DAYS', '7'))

DEFAULT_ITEMS_PER_PAGE = int(conf_get('DEFAULT_ITEMS_PER_PAGE', '30'))

AUTH_END_POINT = '/auth'

FAST_TESTING = True if conf_get('FAST_TESTING', 'False') == 'True' else False

VERSION = __version__


#MIDDLEWARE_CLASSES = ['falcon_rest.contrib.middleware']
#MIDDLEWARE = ['api_lic.middleware.Middleware']
#MIDDLEWARE = ['falcon_rest.contrib.middleware.Middleware']
#MIDDLEWARE = ['falcon_rest.contrib.rbac.RbacMiddleware']
MIDDLEWARE = ['api_lic.rbac.RbacMiddleware']
#AUTH_MODULE = 'falcon_rest.contrib.auth'
AUTH_MODULE = 'api_lic.auth'
AUTH_USER_MODEL = 'api_lic.model.User'
#PERMISSIONS_MODULE = 'api_lic.permissions'
TESTING_APP_CREATION_FUNC = 'api_lic.create_app'

COLLECT_ENTITIES = True

PATHS_NOT_NEEDED_AUTH = (
    '{}{}'.format(API_BASE_PATH, AUTH_END_POINT),
    '{}/user/auth'.format(API_BASE_PATH),
    '{}/registration/create'.format(API_BASE_PATH),
    '{}/auth/reset_email'.format(API_BASE_PATH),
    '{}/auth/reset_password'.format(API_BASE_PATH),
    '{}/product/public'.format(API_BASE_PATH),
    '{}/swagger.yaml'.format(API_BASE_PATH),
    '{}/swagger.json'.format(API_BASE_PATH)
)

ALWAYS_ALLOWED_AUTH_IPS = conf_get('ALWAYS_ALLOWED_AUTH_IPS', '127.0.0.1').split(' ')

GOOGLE_DRIVE =  {
'application_name':'api_lic',
'service_lifetime':'36000',
'credential_dir':'./',
'client_secret_file':'google-drive-client-secret.json'
}

FILES = {
    'upload_to': conf_get('FILES_UPLOAD_TO','files')
}
DONT_DELETE_DOWNLOAD_TOKEN = False

CELERY  = {
    'CELERY_BROKER_URL':conf_get('CELERY_BROKER_URL','redis://localhost:6379/0'),
    'CELERY_RESULT_BACKEND':conf_get('CELERY_RESULT_BACKEND','redis://localhost:6379/0'),
    'CELERYD_TASK_SOFT_TIME_LIMIT':conf_get('CELERYD_TASK_SOFT_TIME_LIMIT','300')
}

SENTRY_URL = conf_get('SENTRY_URL',None)

UI_BASE_URL = conf_get('UI_BASE_URL', 'http://localhost')
MAILING = {
    'host': conf_get('SMTP_HOST',''),
    'port': conf_get('SMTP_PORT',''),
    'username': conf_get('SMTP_USERNAME',''),
    'password': conf_get('SMTP_PASSWORD',''),
    'use_ssl': True if conf_get('SMTP_USE_SSL','') == 'True' else False,
    #'use_tls': True if conf_get('SMTP_USE_TLS') == 'True' else False
}

SENTRY_URL = conf_get('sentry_url','False')

if SENTRY_URL=='False':
    SENTRY_URL=None

ADMIN_UUID = conf_get('ADMIN_UUID','17209cf7-0274-4443-9db7-747db6d77e11')
ADMIN_EMAIL = conf_get('ADMIN_EMAIL','admin@example.com')
ADMIN_PWD = conf_get('ADMIN_PWD','17209cf7-0274-4443-9db7-747db6d77e11')
TEST_USER_UUID = conf_get('TEST_USER_UUID','17209cf7-0274-4443-9db7-747db6d77e12')
TEST_USER_EMAIL = conf_get('TEST_USER_EMAIL','test_user@example.com')

PAYPAL = {
    'client_id':conf_get('client_id','EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM','PAYPAL'),
    'client_secret':conf_get('client_secret','EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM','PAYPAL'),
    'mode':conf_get('mode','sandbox','PAYPAL')
}

STRIPE = {
    'api_key':conf_get('api_key','pk_test_0JEARRXZBg8F8kDxtFfWAjxy','STRIPE')
}

if _p_changed:
    with open(API_INI, 'w') as configfile:
        config.write(configfile)