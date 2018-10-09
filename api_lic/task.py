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
from .model import BaseModel, User, DID, ReceivedSms, Company, Recipient, Sms
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
    try:
        from api_lic.tasks.did_import_file import do_did_import_file
        sender.add_periodic_task(600.0, do_did_import_file)
    except Exception as e:
        log.error('cannot import do_import_file!{}'.format(str(e)))

    try:
        from api_lic.tasks.recipient_import_file import do_recipient_import_file
        sender.add_periodic_task(600.0, do_recipient_import_file)
    except Exception as e:
        log.error('cannot import do_import_file!{}'.format(str(e)))
    try:
        from api_lic.tasks.campaign import do_campaigns
        sender.add_periodic_task(120.0, do_campaigns)
    except Exception as e:
        log.error('cannot import do_import_file!{}'.format(str(e)))

from .utils.kannel import unprefix

@app.task(base=SqlAlchemyTask)
def process_sms(uuid):
    log.debug('process_sms({})'.format(uuid))
    obj = ReceivedSms.get(uuid)
    if obj:
        log.debug('process_sms({})'.format(uuid))
        user = User.filter(User.phone == unprefix(obj.receiver)).first()
        recipient_uuid = None
        if user and user.company:
            recipient = Recipient.filter(Recipient.phone_number == unprefix(obj.sender)).first()
            if recipient:
                recipient_uuid = recipient.recipient_uuid
            Sms(received_sms_uuid=obj.received_sms_uuid, user_id=user.user_id, company_uuid=user.company_uuid,
                recipient_uuid=recipient_uuid, text=obj.msgdata).save()

    else:
        log.warning('process_sms({}) not found'.format(uuid))
    log.debug('process_sms({}) success'.format(uuid))

@app.task(base=SqlAlchemyTask)
def route_sms(data):

    log.debug('route_sms({})'.format(data))

    if data:
        log.debug('route_sms({})'.format(data['id']))
        user = User.filter(User.phone == unprefix(data['sender'])).first()
        recipient_uuid = None
        if user and user.company:
            recipient = Recipient.filter(Recipient.phone_number == unprefix(data['receiver'])).first()
            if recipient:
                recipient_uuid = recipient.recipient_uuid
            Sms(sms_uuid=data['id'], user_id=user.user_id, company_uuid=user.company_uuid,
                recipient_uuid=recipient_uuid, text=data['msgdata'],meta_data=data['meta_data'] if 'meta_data' in data else None).save()

    else:
        log.warning('route_sms({}) not found'.format(data['id']))
    log.debug('process_sms({}) success'.format(data['id']))

@app.task(base=SqlAlchemyTask)
def receive_sms(data):

    log.debug('receive_sms({})'.format(data))

    if data:
        log.debug('receive_sms({})'.format(data['id']))
        user = User.filter(User.phone == unprefix(data['receiver'])).first()
        if user and user.company:
            recipient = Recipient.filter(Recipient.phone_number == unprefix(data['sender'])).first()
            if recipient:
                recipient_uuid = recipient.recipient_uuid
            else:
                recipient_uuid = None
            data['received_sms_uuid']=data['id']
            received_sms_uuid = ReceivedSms(**data).save()
            sms = Sms(received_sms_uuid=received_sms_uuid, user_id=user.user_id, company_uuid=user.company_uuid,
                recipient_uuid=recipient_uuid, text=data['msgdata'],meta_data=data['meta_data'] if 'meta_data' in data else None)
            sms.save()
            user.company.on_receive_sms(sms)

    else:
        log.warning('receive_sms({}) not found'.format(data['id']))
    log.debug('receive_sms({}) success'.format(data['id']))
