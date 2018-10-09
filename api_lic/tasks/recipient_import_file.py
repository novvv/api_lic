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
from sqlalchemy.sql import func, select, alias, case

import csv

from ..view import IntegrityError
from ..model import BaseModel, User, Recipient, RecipientImportTask, Country, Company
from ..task import app, log, db, SqlAlchemyTask
from .. import model
from .. import view


@app.task(base=SqlAlchemyTask)
def do_recipient_import_file():
    log.info('start do_recipient_import_file ')
    q = RecipientImportTask.filter(RecipientImportTask.status == 'initial').order_by(
        RecipientImportTask.created_on).first()
    if q:
        recipient_import_file.delay(q.uuid)
    log.info('finish do_recipient_import_file ')


import re

PHONE_REGEXP = r'^\+?[0-9]+$'


@app.task(base=SqlAlchemyTask, time_limit=288000, soft_time_limit=287400)
def recipient_import_file(id):
    log.info('start recipient_import_file {}'.format(id))
    tsk = RecipientImportTask.get(id)
    from falcon_rest import logger
    logger.log.setLevel(mlevel('ERROR'))
    log.setLevel(mlevel('ERROR'))
    if tsk and tsk.status == 'initial':
        tsk.status = 'busy'
        errors = []
        try:

            file = open(tsk.file_name)
            data = csv.DictReader(file)
            user_id = tsk.user_id
            user = None
            user_name = None
            if user_id:
                user = model.User.get(user_id)
                user_name = user.user_name
            i = 0
            sk_i = 0
            for row in data:
                num = row['phone_number'].strip().lower()
                num = re.sub(r'[() -]', '', num)
                row_errors = ''
                company_uuid = tsk.company_uuid
                i = i + 1
                if not re.match(PHONE_REGEXP, num):
                    sk_i = sk_i + 1
                    errors.append('row {}: skip bad number {}'.format(i, num))
                    continue
                first_name = ''
                last_name = ''
                if 'recipient_name' in row and not 'first_name' in row:
                    fl = row['recipient_name'].strip().split(' ')[0]
                    if len(fl)>0:
                        first_name = fl[0]
                    if len(fl) > 1:
                        last_name = fl[1]
                if 'first_name' in row:
                    first_name = row['first_name'].strip()
                if 'last_name' in row:
                    last_name = row['last_name'].strip()
                recipient_name = first_name + ' ' + last_name
                if recipient_name == ' ':
                    errors.append('row {}: skip missing recipient name'.format(i))
                    sk_i = sk_i + 1
                    continue

                address = None
                if 'address' in row:
                    address = row['address'].strip()

                if i % 500 == 0:
                    print('recipients imported {}'.format(i))
                    tsk.result = 'recipients imported {}'.format(i)
                    tsk.save()
                try:
                    cls = model.Recipient
                    recipient = cls.filter(and_(cls.company_uuid == company_uuid, or_(cls.phone_number == num,
                                                                                   cls.recipient_name == recipient_name))).first()
                    if recipient:
                        if tsk.duplicates_action == 'skip':
                            sk_i = sk_i + 1
                            errors.append(
                                'row {}: in file phone_number:{} recipient_name:{} skip duplicate phone_number:{} recipient_name:{}'.format(i, num,recipient_name,recipient.phone_number, recipient.recipient_name))
                            continue
                        else:
                            recipient.delete()

                    recipient = cls(phone_number=num, address=address, company_uuid=company_uuid,
                                  first_name=first_name, last_name=last_name
                                 )
                    user.session().add(recipient)
                except IntegrityError as e:
                    errors.append('row {}:{}'.format(i - 1, str(e)))
                    log.warning('error on import {} {}'.format(num, str(e)))
            tsk.finished_on = datetime.now(UTC)
            tsk.status = 'success'
            if errors:
                tsk.result = 'recipients imported {} of {}, recipients skiped {}\nIMPORT WARNINGS:\n{}'.\
                    format(i - sk_i, i, sk_i, '\n'.join(errors))
            else:
                tsk.result = 'recipients imported {} of {}, recipients skiped {}'.format(i - sk_i, i, sk_i)
            tsk.save()
        except Exception as e:
            tsk.finished_on = datetime.now(UTC)
            tsk.status = 'fail'
            tsk.result = 'Import failure: {}\n{}'.format(str(e)[0:500],
                                                         'IMPORT WARNINGS:\n'.join(errors))
            tsk.save()
            log.error('Import failure: {}'.format(str(e)))
    else:
        log.info('skip already running import_file {}'.format(id))
    logger.log.setLevel(mlevel(settings.LOG_LEVEL))
    log.setLevel(mlevel(settings.LOG_LEVEL))
    log.info('finish recipient_import_file {}'.format(id))
