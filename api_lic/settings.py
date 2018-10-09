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

# from falcon_rest.conf import settings
REQUIRED_ENV_VARIABLES = ['LOG_FILE', 'LOG_LEVEL', 'API_BASE_PATH', 'DB_CONN_STRING', 'JWT_SIGNATURE',
'FALCON_SETTING_MODULE','LOG_TO_CONSOLE','ALLOW_ORIGIN','API_HOST','API_SCHEMA','API_BASE_PATH',
'CREATE_TABLES',
'JWT_TTL_DAYS','DEFAULT_ITEMS_PER_PAGE','ALWAYS_ALLOWED_AUTH_IPS','FILES_UPLOAD_TO','UI_BASE_URL',
'SMTP_HOST','SMTP_PORT','SMTP_USERNAME','SMTP_PASSWORD','SMTP_USE_TLS',]

for var in REQUIRED_ENV_VARIABLES:  # pragma: no cover
    if var not in os.environ:
        if var.lower() in config['DEFAULT']:
            os.environ[var]=config['DEFAULT'][var.lower()]
            continue
        err = '{} environment variable is not set, all required variables: {}'.format(var, REQUIRED_ENV_VARIABLES)
        #raise EnvironmentError(err)
        #_p_changed = True
        continue
    else:
        if not var.lower() in config['DEFAULT']:
            config['DEFAULT'][var.lower()] = os.environ[var]
            #_p_changed = True
        else:
            os.environ[var] = config['DEFAULT'][var.lower()]

LOG_FILE = os.environ.get('LOG_FILE','lic.log')
LOG_LEVEL = os.environ.get('LOG_LEVEL','debug')
LOG_TO_CONSOLE = True if os.environ.get('LOG_TO_CONSOLE') == 'True' else False
LOG_FORMAT = os.environ.get('LOG_FORMAT', '%(asctime)s [%(levelname)s] \'%(message)s\' at %(filename)s: %(lineno)s')
ALLOW_ORIGINS = os.environ.get('ALLOW_ORIGIN', '*').split(' ')
ALLOW_ORIGIN = os.environ.get('ALLOW_ORIGIN', '*').split(' ')
API_TITLE = 'LICENSE API'
API_HOST = os.environ.get('API_HOST', 'localhost:8012')
API_SCHEME = os.environ.get('API_SCHEMA', 'http://')
API_BASE_PATH = os.environ.get('API_BASE_PATH', '/v1')
API_TEST_ROUTES = os.environ.get('API_TEST_ROUTES', 'False')
DB_CONN_STRING = os.environ.get('DB_CONN_STRING')
DB_CONN_STRING_TEST = os.environ.get('DB_CONN_STRING_TEST', '')

CREATE_TABLES = True if os.environ.get('CREATE_TABLES', False) == 'True' else False

JWT_SIGNATURE = os.environ.get('JWT_SIGNATURE')
JWT_TTL_DAYS = int(os.environ.get('JWT_TTL_DAYS', 1))
JWT_REFRESH_THRESHOLD_DAYS = int(os.environ.get('JWT_REFRESH_THRESHOLD_DAYS', 7))

DEFAULT_ITEMS_PER_PAGE = int(os.environ.get('DEFAULT_ITEMS_PER_PAGE', 30))

AUTH_END_POINT = '/auth'

FAST_TESTING = True if os.environ.get('FAST_TESTING', False) == 'True' else False

VERSION = __version__


#MIDDLEWARE_CLASSES = ['falcon_rest.contrib.middleware']
#MIDDLEWARE = ['api_lic.middleware.Middleware']
#MIDDLEWARE = ['falcon_rest.contrib.middleware.Middleware']
#MIDDLEWARE = ['falcon_rest.contrib.rbac.RbacMiddleware']
MIDDLEWARE = ['api_lic.rbac.RbacMiddleware']
AUTH_MODULE = 'falcon_rest.contrib.auth'
#AUTH_MODULE = 'api_lic.auth'
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

ALWAYS_ALLOWED_AUTH_IPS = os.environ.get('ALWAYS_ALLOWED_AUTH_IPS', '127.0.0.1').split(' ')

GOOGLE_DRIVE =  {
'application_name':'api_lic',
'service_lifetime':'36000',
'credential_dir':'./',
'client_secret_file':'google-drive-client-secret.json'
}

FILES = {
    'upload_to': os.environ.get('FILES_UPLOAD_TO','files')
}
DONT_DELETE_DOWNLOAD_TOKEN = False

CELERY  = {
    'CELERY_BROKER_URL':os.environ.get('CELERY_BROKER_URL','redis://localhost:6379/0'),
    'CELERY_RESULT_BACKEND':os.environ.get('CELERY_RESULT_BACKEND','redis://localhost:6379/0'),
    'CELERYD_TASK_SOFT_TIME_LIMIT':os.environ.get('CELERYD_TASK_SOFT_TIME_LIMIT','300')
}

SENTRY_URL = os.environ.get('SENTRY_URL',None)#'https://64918317b78149898d5d4c6940354140:81a4c63217ed4171ac616e03922a135d@sentry.io/231210'

UI_BASE_URL = os.environ.get('UI_BASE_URL', 'http://localhost')
MAILING = {
    'host': os.environ.get('SMTP_HOST'),
    'port': os.environ.get('SMTP_PORT'),
    'username': os.environ.get('SMTP_USERNAME'),
    'password': os.environ.get('SMTP_PASSWORD'),
    'use_ssl': True if os.environ.get('SMTP_USE_SSL') == 'True' else False,
    #'use_tls': True if os.environ.get('SMTP_USE_TLS') == 'True' else False
}

KANNEL ={
    'send_url': conf_get('send_url','http://localhost:13013/cgi-bin/cgi-bin/sendsms','KANNEL'),
    'username': conf_get('username','denovo','KANNEL'),
    'password': conf_get('password','yoo5Iche','KANNEL'),
    'service': conf_get('service','denovo','KANNEL'),
}
SENTRY_URL = conf_get('sentry_url',
                      'http://333847b311294619934d0c770796ebc4:c675902daf5742c389e2d2e31e065f2c@sentry.denovolab.com:9000/2')

if SENTRY_URL=='False':
    SENTRY_URL=None

ADMIN_UUID = '17209cf7-0274-4443-9db7-747db6d77e11'
TEST_USER_UUID = '17209cf7-0274-4443-9db7-747db6d77e12'

if _p_changed:
    with open(API_INI, 'w') as configfile:
        config.write(configfile)