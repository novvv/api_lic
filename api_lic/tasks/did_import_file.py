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
from sqlalchemy import (Column, desc, and_, text as text_, PrimaryKeyConstraint, inspect, Index, UniqueConstraint)
from sqlalchemy.sql import func, select, alias, case

import csv

from ..view import IntegrityError
from ..model import BaseModel, User, DID, DIDAssignLog, DidImportTask, Country, Company,AreaCode
from ..task import app, log, db, SqlAlchemyTask
from .. import model
from .. import view


@app.task(base=SqlAlchemyTask)
def do_did_import_file():
    log.info('start do_import_file ')
    q = DidImportTask.filter(DidImportTask.status == 'initial').order_by(DidImportTask.created_on).first()
    if q:
        did_import_file.delay(q.uuid)
    log.info('finish do_import_file ')


import re

PHONE_REGEXP = r'^\+?[0-9]+$'


@app.task(base=SqlAlchemyTask, time_limit=288000, soft_time_limit=287400)
def did_import_file(id):
    log.info('start import_file {}'.format(id))
    tsk = DidImportTask.get(id)
    from falcon_rest import logger
    logger.log.setLevel(mlevel('ERROR'))
    log.setLevel(mlevel('ERROR'))
    if tsk and tsk.status == 'initial':
        tsk.status = 'busy'
        errors = []
        try:

            file = open(tsk.file_name)
            data = csv.reader(file)
            user_id = tsk.user_id
            user = None
            user_name = None
            if user_id:
                user = model.User.get(user_id)
                user_name = user.user_name
            if tsk.vendor_uuid:
                vendor_uuid = tsk.vendor_uuid
            i = 0
            sk_i = 0
            for row in data:
                num = row[0].strip().lower()
                row_errors = ''
                company_uuid = None
                country_uuid = None
                vendor_uuid = None
                did_type = None
                if 'num' in num:
                    continue
                i = i + 1
                if not re.match(PHONE_REGEXP, num):
                    sk_i = sk_i + 1
                    errors.append('row {}: skip bad number {}'.format(i, num))
                    continue

                if len(row) > 1:
                    country_uuid = row[1].strip()
                    if not Country.get(country_uuid):
                        country = Country.filter(Country.name == country_uuid).first()
                        if country:
                            country_uuid = country.country_uuid
                        else:
                            country_uuid = None

                if not country_uuid:
                    if tsk.country_uuid:
                        country_uuid = tsk.country_uuid
                    else:
                        row_errors = row_errors + ' warning no country used default "1" '
                        if num[0:3] in AreaCode.CANADA:
                            country_uuid = '1-'
                        else:
                            country_uuid = '1'

                if len(row) > 2:
                    if 'toll' in row[2].lower():
                        did_type = 'Toll Free'
                    else:
                        did_type = 'Local'
                if not did_type:
                    if tsk.did_type:
                        did_type = tsk.did_type
                    else:
                        row_errors = row_errors + ' warning no type used default "Local" '
                        did_type = 'Local'

                if len(row) > 3:
                    company_uuid = row[3].strip()
                    if not Company.get(company_uuid):
                        company = Company.filter(Company.company_name == company_uuid).first()
                        if company:
                            company_uuid = company.company_uuid
                        else:
                            row_errors = row_errors + ' wrong company uuid or name {} '.format(row[3].strip())
                            company_uuid = None
                if not company_uuid:
                    if tsk.company_uuid:
                        company_uuid = tsk.company_uuid
                    else:
                        company_uuid = None
                        row_errors = row_errors + ' warning no company '
                        log.warning('company not found {}'.format(row[3].strip()))

                if tsk.from_number and tsk.to_number:
                    if num < tsk.from_number:
                        continue
                    if num > tsk.to_number:
                        continue
                if row_errors:
                    errors.append('row {}:{}'.format(i, row_errors))

                if i % 500 == 0:
                    print('numbers imported {}'.format(i))
                    tsk.result = 'numbers imported {}'.format(i)
                    tsk.save()
                try:
                    number = model.DID.filter(model.DID.number == num).first()
                    if number:
                        if tsk.duplicates_action == 'skip':
                            sk_i = sk_i + 1
                            continue
                        else:
                            DIDAssignLog(number=number.number, vendor_uuid=number.vendor_uuid,
                                         company_uuid=number.company_uuid,
                                         type=number.type, assigned_by=number.assigned_by,
                                         assigned_on=number.assigned_on,
                                         deleted_on=datetime.now(UTC),
                                         country_uuid=number.country_uuid
                                         ).save()
                            number.delete()

                    number = model.DID(number=num, vendor_uuid=vendor_uuid, company_uuid=company_uuid,
                                       type=did_type, created_by=user_name,
                                       assigned_by=user_name,
                                       assigned_on=datetime.now(UTC),
                                       country_uuid=country_uuid)
                    user.session().add(number)
                except IntegrityError as e:
                    errors.append('row {}:{}'.format(i - 1, str(e)))
                    log.warning('error on import {} {}'.format(num, str(e)))
            tsk.finished_on = datetime.now(UTC)
            tsk.status = 'success'
            if errors:
                tsk.result = 'numbers imported {} of {}, numbers skiped {}\n' \
                             'IMPORT WARNINGS:\n{}'.format(i - sk_i, i, sk_i, '\n'.join(errors))
            else:
                tsk.result = 'numbers imported {} of {}, numbers skiped {}'.format(i - sk_i, i, sk_i)
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
    log.info('finish import_file {}'.format(id))
