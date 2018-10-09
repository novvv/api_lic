# from falcon_rest.db import fields, orm , get_db
import csv
import falcon
import io
import json
import mimetypes
from datetime import datetime
from time import mktime
import traceback
from dateutil.parser import parse as parse_datetime
from pytz import UTC
from urllib.parse import parse_qsl, urlencode
# from falcon_rest.db import Column
# from falcon_rest.conf import settings
# from falcon_rest.contrib.files import create_file_model_class, create_scheme
# from falcon_rest.contrib.files.endpoints import UploadFile, GetDownloadLink, DownloadFile, ShowFile
# from marshmallow_sqlalchemy import field_for, fields as sa
from sqlalchemy import (desc)
from sqlalchemy import text as text_, and_, or_
from sqlalchemy.sql import func, select

# from api_dnl.base_model import DnlApiBaseModel
# from api_dnl.model import rev

from falcon_rest import schemes, resources, responses
from falcon_rest.db.errors import IntegrityError, FkConstraintViolation
from falcon_rest.helpers import check_permission
from falcon_rest.logger import log
from falcon_rest.resources.base_resource import OperationalError
from falcon_rest.resources.resources import swagger, ResourcesBaseClass, DEFAULT_SECURITY, ATTRIBUTE_ERROR_RE
from falcon_rest.responses import errors
# from .tasks import *
from api_lic import model
from api_lic.resources.resources import List
from api_lic.views.admin import RateSchemeGet
from ..scheme import *
from ..scheme import _valid
from ..resources.resources import Create, Resource, List, CustomAction, CustomGetAction, CustomPostAction, \
    generate_uuid_str, SuccessResponseJustOk201


class SimpleFileCreate(resources.BaseResource):
    model_class = model.User
    entity = 'SimpleFile'
    method = 'post'
    body_parameters = ()
    additional_responses = ()
    path_parameters = ()
    security = (DEFAULT_SECURITY)

    def get_security(self, **kwargs):
        return self.security

    def get_spec(self):
        additional_responses = (
                                   responses.OperationErrorResponse(data=errors.CommonErrors.PermissionError,
                                                                    description='Can\'t create file'),
                               ) + self.additional_responses

        ext_body_parameters = (
            {
                'name': 'file',
                'in': 'formData',
                'description': 'File to upload',
                'required': True,
                'type': 'file'
            },

        )

        return swagger.specify.get_spec(
            method='post', description='Creates new {}'.format(self.entity.lower()),
            consumes=['multipart/form-data'],
            path_parameters=self.path_parameters,
            responses=(
                          responses.ObjectCreatedResponse(),
                          # self.scheme_class.get_object_created_response(entity=self.entity),#,scheme=ObjectCreatedWithErrorsScheme),
                      ) + additional_responses,
            security=self.get_security(method='post'),
            # body_parameters=('{} to create'.format(self.entity), self.scheme_class),
            ext_body_parameters=ext_body_parameters
        )

    def on_post(self, req, resp, **kwargs):
        try:
            file = req.files['file']
            file_path = settings.FILES['upload_to'] + '/' + file.filename
            local_file = open(file_path, 'wb')
            local_file.write(file.read())
            self.set_response(resp, responses.ObjectCreatedResponse(data_key='object_pk', data=file.filename))
        except Exception as e:
            self.set_response(resp, OperationalError(e))
            return False


class SimpleFileGet(CustomGetAction):
    path_parameters = ({'name': 'file_name', 'description': 'file name'},)
    no_auth_needed = True

    def get_spec_info(self):
        spec = super().get_spec_info()
        spec['get']['produces'] = ['image/ico', 'image/jpg', 'image/png', 'text/csv', 'application/xls']
        return spec

    def on_get(self, req, resp, **kwargs):
        try:
            file_name = kwargs['file_name']
            file_path = settings.FILES['upload_to'] + '/' + file_name
            file = open(file_path, 'rb')
            resp.data = file.read()
            resp.content_type = mimetypes.guess_type(file_name)[0]
            resp.append_header('Content-Disposition', 'attachment; filename="{}"'.format(file_name))
            resp.status = falcon.HTTP_200
            return
        except Exception as e:
            self.set_response(resp, OperationalError(e))
            return False


class RateList(List):
    scheme_class = RateSchemeGet
    model_class = model.Rate
    entity_plural = 'Rates'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        if not user.is_admin:
            cls = self.model_class
            # ret = ret.filter(cls.pool_id != 0)#TODO:filter for user
        return filt, ret