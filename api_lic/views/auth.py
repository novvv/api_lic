import csv
import falcon
import io
import json
from datetime import datetime, timedelta
from time import mktime
import jwt
from dateutil.parser import parse as parse_datetime
from pytz import UTC
from urllib.parse import parse_qsl, urlencode
from sqlalchemy.sql import func, select, case, cast, alias, literal
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import (Column, desc, and_, or_, text as text_, PrimaryKeyConstraint, inspect, Sequence,
                        UniqueConstraint)
from falcon_rest.responses import responses
from falcon_rest.resources.resources import DEFAULT_SECURITY
# from .tasks import *
from ..scheme import *
from ..resources.resources import Create, Resource, List, CustomAction,CustomPostAction
from ..auth import auth

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

class UserResetPassword(CustomPostAction):
    scheme_class = UserResetPasswordScheme
    model_class = model.User
    body_parameters = ('User data', UserResetPasswordScheme)
    method = 'post'
    path_parameters = ({'name': 'token', 'description': 'Token from email'},)

    no_auth_needed = True

    def on_post(self, req, resp, **kwargs):
        return self.proceed(req, resp, **kwargs)

    def proceed(self, req, resp, **kwargs):
        import jwt
        try:
            token_data = jwt.decode(kwargs['token'], settings.JWT_SIGNATURE)
            user = model.User.get(token_data['user_uuid'])
            if user:
                user.passwd = req.data['passwd']
                user.save()
                user.apply_mail('welcome')
                # log = model.RetrievePasswordLog.get(token_data['log_id'])
                # if log:
                #     log.confirm_ip = get_request_ip(req)
                #     log.modify_time = datetime.now(UTC)
                #     log.status = 'Modified successfully'
                #     log.save()
                self.set_response(resp, responses.SuccessResponseJustOk())
                return True
                # model.MailSender.apply_mail(user, 'retrieve_password', user.email) # obj.client.billing_email)
        except Exception as e:
            pass
        self.set_response(resp, responses.ObjectNotFoundErrorResponse())

# class UserResetPassword(CustomAction):
#     scheme_class = UserResetPasswordScheme
#     model_class = model.User
#     body_parameters = ('User data', UserResetPasswordScheme)
#     method = 'post'
#
#     def on_post(self, req, resp, **kwargs):
#         return self.proceed(req, resp, **kwargs)
#
#     def apply(self, obj, req, resp, **kwargs):
#         user = auth.get_user_from_token(req.data['token'])
#         if user:
#             user.passwd = req.data['password']
#             user.apply_mail('welcome')
#             # model.MailSender.apply_mail(user, 'welcom', obj.client.billing_email)
#
class UserConfirmRegister(CustomPostAction):
    scheme_class = UserConfirmRegisterScheme
    model_class = model.User
    body_parameters = ('User data', UserConfirmRegisterScheme)
    method = 'post'
    path_parameters = ({'name': 'token', 'description': 'Token from email'},)
    no_auth_needed = True

    def on_post(self, req, resp, **kwargs):
        try:
            token_data = jwt.decode(kwargs['token'], settings.JWT_SIGNATURE)
            kwargs['user_uuid'] = token_data['user_uuid']
            return self.proceed(req, resp, **kwargs)
        except Exception as e:
            log.error('user confirm register error {}'.format(str(e)))
            self.set_response(resp, responses.ObjectNotFoundErrorResponse())

    def apply(self, obj, req, resp, **kwargs):
        try:
            if obj:
                obj.confirmed_on = datetime.now(UTC)
                obj.is_active = True
                obj.save()
                self.set_response(resp, responses.SuccessResponseJustOk())
                return True
        except Exception as e:
            log.error('user confirm register error {}'.format(str(e)))
            pass
        self.set_response(resp, responses.ObjectNotFoundErrorResponse())


class UserForgotPassword(CustomPostAction):
    scheme_class = UserResetPasswordLetterScheme
    body_parameters = ('Email to check', UserResetPasswordLetterScheme)
    method = 'post'
    model_class = model.User
    no_auth_needed = True

    def on_post(self, req, resp, **kwargs):
        return self.proceed(req, resp, **kwargs)

    def proceed(self, req, resp, **kwargs):
        import jwt
        from urllib3.util import parse_url

        cls = self.model_class
        user = cls.filter(cls.email == req.data['email']).first()
        if user:
            exp = (datetime.now(UTC) + timedelta(hours=2)).timestamp()
            # token_data ={'user_uuid':user.user_uuid,'password':req.data['password'],'exp':exp}
            token_data = {'user_uuid': user.user_uuid, 'exp': exp}
            token = jwt.encode(token_data, settings.JWT_SIGNATURE, algorithm='HS256').decode('utf-8')
            ui_url = '{}/#/auth/reset/{}'.format(settings.UI_BASE_URL, token)
            user.token = token
            # user.reset_password_url = ui_url
            # '{}{}{}/auth/reset_password/{}'.format(settings.API_SCHEME, settings.API_HOST, settings.API_BASE_PATH, token)
            ret = user.apply_mail('retrieve_password')  # obj.client.billing_email
            if ret:
                self.set_response(resp, responses.OperationErrorResponse(data='mail error'))
                return False
            self.set_response(resp, responses.SuccessResponseJustOk())
            return False
        self.set_response(resp, responses.ObjectNotFoundErrorResponse())
        return False






# --------------User
