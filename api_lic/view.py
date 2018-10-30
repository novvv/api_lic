# from falcon_rest.db import fields, orm , get_db
import csv
import falcon
import io
import json
from datetime import datetime
from time import mktime

from dateutil.parser import parse as parse_datetime
from pytz import UTC
# from falcon_rest.db import Column
# from falcon_rest.conf import settings
# from falcon_rest.contrib.files import create_file_model_class, create_scheme
# from falcon_rest.contrib.files.endpoints import UploadFile, GetDownloadLink, DownloadFile, ShowFile
# from marshmallow_sqlalchemy import field_for, fields as sa
from sqlalchemy import (desc)
from sqlalchemy import text as text_, and_, or_
from sqlalchemy.sql import func

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
from .scheme import *
from .scheme import _valid,_valid_unique
from .resources.resources import Create, Resource, List, CustomAction
from .auth import auth
from . import settings

DEFAULT_SECURITY = ['auth_token']
import uuid


def generate_uuid_str():
    return lambda: str(uuid.uuid4())


# Revisions
# from  falcon_rest.contrib.objects_history.object_revision.object_revision import ObjectRevisionModel,ObjectRevisionSchemeGet


class ObjectRevisionList(List):
    scheme_class = ObjectRevisionFilterSchemeGet
    model_class = model.ObjectRevisionModel
    entity_plural = 'Object revisions'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()


# ++++++++++++++User
class UserCreate(Create):
    scheme_class = UserScheme
    entity = 'User'
    unique_field = 'name'
    additional_responses = ()
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    # noinspection PyUnusedLocal
    def before_create(self, obj, **kwargs):
        return obj


class UserRegisterCreate(Create):
    model_class = model.User
    scheme_class = UserRegisterScheme
    entity = 'Company registration'
    no_auth_needed = True

    def after_create(self,object_id, req, resp, **kwargs):
        user = model.User.get(object_id)
        user.token = auth.get_token(user)
        if user:
            user.apply_mail('registration')

class UserResource(Resource):
    model_class = model.User
    scheme_class = UserScheme
    scheme_class_get = UserSchemeGet
    scheme_class_modify = UserSchemeModify
    entity = 'User'
    id_field = 'user_uuid'
    has_update_by = True
    unique_field = 'email'
    security = (DEFAULT_SECURITY)
    restrict = ()

    def delete_object(self, req, resp, model_class, **kwargs):
        if kwargs['user_uuid'] == settings.ADMIN_UUID:
            return True
        return super().delete_object(req, resp, model_class, **kwargs)

    def before_update(self, obj, req):
        return obj

class UserByEmailResource(Resource):
    model_class = model.User
    scheme_class = UserScheme
    scheme_class_get = UserSchemeGet
    scheme_class_modify = UserSchemeModify
    entity = 'User'
    id_field = 'email'
    has_update_by = True
    unique_field = 'user_uuid'
    security = (DEFAULT_SECURITY)
    restrict = ()

    def get_object(self, resp, model_class, **kwargs):
        if 'email' in kwargs:
            q=model.User.filter(func.lower(model.User.email)==kwargs['email'].lower()).first()
            if q:

                kwargs={'user_uuid':q.user_uuid}
            else:
                self.set_response(resp, responses.ObjectNotFoundErrorResponse())
                return None
        return super().get_object(resp, model_class, **kwargs)


    def delete_object(self, req, resp, model_class, **kwargs):
        if 'email' in kwargs:
            q = model.User.filter(func.lower(model.User.email) == kwargs['email'].lower()).first()
            if q:
                kwargs = {'user_uuid': q.user_uuid}
                if kwargs['user_uuid'] == settings.ADMIN_UUID:
                    self.set_response(resp, responses.ObjectNotFoundErrorResponse())
                    return None
            else:
                self.set_response(resp, responses.ObjectNotFoundErrorResponse())
                return None
        return super().delete_object(req,resp, model_class, **kwargs)


    def before_update(self, obj, req):
        return obj


class UserList(List):
    scheme_class = UserSchemeGet
    model_class = model.User
    entity_plural = 'Users'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()
    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        return filt, ret


class UserResetPassword(CustomAction):
    scheme_class = UserResetPasswordScheme
    model_class = model.User
    body_parameters = ('User data', UserResetPasswordScheme)
    method = 'post'

    def on_post(self, req, resp, **kwargs):
        return self.proceed(req, resp, **kwargs)

    def apply(self, obj, req, resp, **kwargs):
        user = auth.get_user_from_token(req.data['token'])
        if user:
            user.passwd = req.data['password']
            user.apply_mail('welcome')
            # model.MailSender.apply_mail(user, 'welcom', obj.client.billing_email)

# --------------User
