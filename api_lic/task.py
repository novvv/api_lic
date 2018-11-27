import celery
from api_lic import settings
from datetime import datetime, timedelta
from time import sleep
from pytz import UTC
import io, csv, gzip, zipfile
import xlwt
import json
# from api_lic.utils.imp_exp import (csv2xls,dict_to_csv)
from celery import Celery, group
from celery.app.log import get_logger, mlevel
from celery.signals import task_prerun, task_postrun
from celery.schedules import crontab
from falcon_rest.db import initialize_db
from .model import BaseModel, User, LicenseSwitch, LicenseLrn, Payment
from .model import PrimaryKeyConstraint, func, and_, or_
from sqlalchemy.orm import aliased, make_transient, foreign
from .settings import DB_CONN_STRING, CREATE_TABLES, LOG_LEVEL, SENTRY_URL

# +++ sentry integration
if SENTRY_URL:
    import raven
    import logging

    sentry = raven.Client(SENTRY_URL)
    from raven.handlers.logging import SentryHandler

    # Manually specify a client
    handler = SentryHandler(sentry)
    handler.setLevel(logging.ERROR)
    from raven.conf import setup_logging

    setup_logging(handler)
# --- sentry integration

db = initialize_db(DB_CONN_STRING, BaseModel)
print(DB_CONN_STRING)
from api_lic import model


class SqlAlchemyTask(celery.Task):
    """An abstract Celery Task that ensures that the connection the the
    database is closed on task completion"""
    abstract = True

    def xx_after_return(self, status, retval, task_id, args, kwargs, einfo):
        try:
            db.session.commit()
        except:
            try:
                db.session.rollback()
            except:
                pass
        finally:
            db.session.remove()


app = Celery('task', broker=settings.CELERY['CELERY_BROKER_URL'])
app.conf.update(settings.CELERY)
app.conf.update(CELERY_ENABLE_UTC=True, )
global log
log = get_logger('task')
log.setLevel(mlevel(LOG_LEVEL))

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


@task_prerun.connect
def task_prerun(*args, **kwargs):
    db.engine.dispose()


@task_postrun.connect
def close_session(*args, **kwargs):
    # Flask SQLAlchemy will automatically create new sessions for you from
    # a scoped session factory, given that we are maintaining the same app
    # context, this ensures tasks have a fresh session (e.g. session errors
    # won't propagate across tasks)
    db.session.remove()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # try:
    #     from api_lic.tasks.did_import_file import do_did_import_file
    #     sender.add_periodic_task(600.0, do_did_import_file)
    # except Exception as e:
    #     log.error('cannot import do_import_file!{}'.format(str(e)))
    sender.add_periodic_task(crontab(minute='59', hour='23'), do_lincese_expiration_remind)


@app.task(base=SqlAlchemyTask)
def do_lincese_expiration_remind():
    log.debug('do_lincese_expiration_remind')
    now = datetime.utcnow().date()
    now_7 = (datetime.utcnow() - timedelta(days=7)).date()
    i = 0
    for lic in LicenseLrn.filter(func.date_trunc('day',LicenseLrn.end_time) == now).all():
        if lic.user.alert_license_expired:
            lic.apply_mail('license_expired')
            i += 1
    for lic in LicenseLrn.filter(func.date_trunc('day',LicenseLrn.end_time) == now_7).all():
        if lic.user.alert_license_will_expired:
            lic.apply_mail('license_will_expired')
            i += 1
    for lic in LicenseSwitch.filter(func.date_trunc('day',LicenseLrn.end_time) == now).all():
        if lic.user.alert_license_expired:
            lic.apply_mail('license_expired')
            i += 1
    for lic in LicenseSwitch.filter(func.date_trunc('day',LicenseLrn.end_time) == now_7).all():
        if lic.user.alert_license_will_expired:
            lic.apply_mail('license_will_expired')
            i += 1

    log.debug('do_lincese_expiration_remind success, Sen {} messages'.format(i))
