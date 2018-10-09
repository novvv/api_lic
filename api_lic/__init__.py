import os
os.environ['FALCON_SETTING_MODULE']='api_lic.settings'
os.environ['DB_CONN_STRING']='postgresql://webbackend@localhost:5432/lic'
#from falcon_rest import conf
from .__version__ import __version__
from . import settings
from . actions import user
from . base_model import BaseModel
# +++ sentry integration
if settings.SENTRY_URL:
    import raven
    import logging
    sentry = raven.Client(settings.SENTRY_URL)
    from raven.handlers.logging import SentryHandler
    # Manually specify a client
    handler = SentryHandler(sentry)
    handler.setLevel(logging.ERROR)
    from raven.conf import setup_logging
    setup_logging(handler)
# --- sentry integration


def create_app():
    from . import settings
    from falcon_rest.logger import log
    from .file import FileModel
    from .actions import user

    from .base_model import BaseModel

    from falcon_rest.app import create
    from .swagger import init_swagger
    from .routes import ROUTES
    # noinspection PyUnresolvedReferences
    from .actions import user
    from .rbac import rbac_acl
    from .model import User,EmailTemplate

    EmailTemplate.init()
    User.init()
    app = create(ROUTES, init_swagger(), name='api_lic')
    log.info('App starting')
    if settings.SENTRY_URL:
        sentry.captureMessage('start api_lic on {}'.format(settings.API_HOST))
    #app.celery = celery
    return app