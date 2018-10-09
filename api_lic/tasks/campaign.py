import celery
from api_lic import settings
from datetime import datetime, timedelta
from pytz import UTC
from time import mktime
import io, csv, gzip, zipfile
import xlwt
import json
import traceback
from celery import Celery

from celery.app.log import get_logger, mlevel
from celery.schedules import crontab
from falcon_rest.db import initialize_db
from sqlalchemy import (
    Integer, SmallInteger, Float, Text, String, DateTime, Date, Time, Boolean, ForeignKey, BigInteger,
    Table
)
from sqlalchemy import (Column, desc, and_, or_, text as text_, PrimaryKeyConstraint, inspect, Index, UniqueConstraint)
from sqlalchemy.sql import func, select, alias, case, cast

import csv

from ..view import IntegrityError
from ..model import BaseModel, User, DID, DIDAssignLog, DidImportTask, Country, Company, Campaign, CampaignTime, Sms, \
    SuppressedNumber, Recipient
from ..task import app, log, db, SqlAlchemyTask
from .. import model
from .. import view


@app.task(base=SqlAlchemyTask)
def do_campaigns():
    log.debug('start do_campaigns ')
    now = datetime.now(UTC)
    t = str(now.time())
    day = now.weekday() + 1
    all = Campaign.filter(
        and_(
            or_(Campaign.status == 'waiting',
                and_(Campaign.status == 'hold', cast(Campaign.last_start_time, Date) < now.date())),
            or_(Campaign.start_date.is_(None), Campaign.start_date <= now.date()),
            CampaignTime.campaign_uuid == Campaign.campaign_uuid, CampaignTime.start_time <= t,
            CampaignTime.end_time > t, CampaignTime.day == day)).all()
    for q in all:
        log.debug('do_campaigns: schedule campaign {}'.format(q.campaign_uuid))
        campaign.delay(q.campaign_uuid)
    if len(all) == 0:
        log.debug('do_campaigns: nothing to do')
    log.debug('finish do_campaigns ')


import re

PHONE_REGEXP = r'^\+?[0-9]+$'


@app.task(base=SqlAlchemyTask, time_limit=288000, soft_time_limit=287400)
def campaign(id, forced=False):
    log.info('start campaign {}'.format(id))
    tsk = Campaign.get(id)
    from falcon_rest import logger
    from time import sleep
    logger.log.setLevel(mlevel('ERROR'))
    log.setLevel(mlevel('ERROR'))
    i = 0
    skip = 0
    suppress = 0
    paused = 0
    total_cost = 0
    total_count = 0
    now = datetime.now(UTC)
    if tsk and (
            forced or tsk.status == 'waiting' or (tsk.status == 'hold' and tsk.last_start_time.date() < now.date())):
        tsk.status = 'running'
        tsk.last_start_time = datetime.now(UTC)
        tsk.save()
        errors = []
        t = str(now.time())
        day = now.weekday() + 1
        try:
            tsk_time = CampaignTime.filter(CampaignTime.campaign_uuid == tsk.campaign_uuid,
                                           CampaignTime.day == day).first()
            if not tsk_time:
                raise Exception('camaign time not exist')
            hhmm = str(tsk_time.end_time).split(':')
            stop_time = now.replace(hour=int(hhmm[0]), minute=int(hhmm[1]))
            total_count = len(tsk.recipients)
            for recipient_uuid in tsk.recipients:
                i = i + 1
                try:
                    recipient = Recipient.get(recipient_uuid)
                    if recipient:
                        q = SuppressedNumber.filter(and_(SuppressedNumber.company_uuid == tsk.company_uuid, text_(
                            "number @> '{}'".format(recipient.phone_number)))).first()
                        if q:
                            suppress = suppress + 1
                            continue
                    sms = Sms(company_uuid=tsk.company_uuid,
                              recipient_uuid=recipient_uuid, campaign_uuid=tsk.campaign_uuid,
                              text=tsk.text)
                    sms.save()
                    total_cost = total_cost + sms.reseller_rate
                    now = datetime.now(UTC)
                    msec = (now - tsk.last_start_time).seconds * 1000000 + (now - tsk.last_start_time).microseconds
                    if msec == 0:
                        continue
                    if i * 1000000.0 / float(msec) > tsk.sms_per_sec:
                        paused = paused + 1
                        sleep(1.0 / float(tsk.sms_per_sec))
                    if not forced and now > stop_time:
                        raise Exception('campaign timeout! was sent to not all recipients')
                    if i % 10 == 0:
                        q = Campaign.filter(Campaign.campaign_uuid == tsk.campaign_uuid)
                        q.update(dict(total_count=total_count, total_cost=total_cost, messages_count=i,
                                      sent_count=i - skip - suppress,
                                      error_count=skip, suppressed_count=suppress), synchronize_session='fetch')
                        Campaign.session().commit()

                        tsk = Campaign.get(id)
                        if tsk.status == 'hold':
                            errors.append('campaign was stopped by admin')
                            break

                except Exception as e:
                    errors.append('recipient {} error was:{}'.format(recipient_uuid, e))
                    skip = skip + 1

            tsk.finish_time = datetime.now(UTC)

            if len(errors):
                tsk.result = 'send {} sms \nWARNINGS:{}'.format(i, '\n'.join(errors))
            else:
                tsk.result = 'send {} sms'.format(i)
            if i - skip - suppress:
                tsk.status = 'hold'
            else:
                tsk.status = 'finished'
                tsk.result = 'send 0 sms. stop campaign permanently\nWARNINGS:{}'.format('\n'.join(errors))
            tsk.total_count = total_count
            tsk.total_cost = total_cost
            tsk.messages_count = i,
            tsk.sent_count = i - skip - suppress,
            tsk.error_count = skip
            tsk.suppressed_count = suppress
            tsk.save()
            log.debug('campaign {} {} warnings: {}'.format(id, tsk.campaign_name, ','.join(errors)))
        except Exception as e:
            tsk.finish_time = datetime.now(UTC)
            tsk.status = 'fail'
            tsk.result = 'campaign failure: {}\nWARNINGS:{}'.format(str(e), '\n'.join(errors))
            tsk.save()
            log.error(
                'campaign {} {} failure: {}\n WARNINGS:{}'.format(id, tsk.campaign_name, str(e), ','.join(errors)))
    logger.log.setLevel(mlevel(settings.LOG_LEVEL))
    log.setLevel(mlevel(settings.LOG_LEVEL))
    log.info(
        'finish campaign {} {} sent {} sms, skip {} sms,suppress {} sms, paused {} times'.format(id, tsk.campaign_name,
                                                                                                 i - skip - suppress,
                                                                                                 skip, suppress,
                                                                                                 paused))
