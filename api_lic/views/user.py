# from falcon_rest.db import fields, orm , get_db
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
from falcon_rest.db.errors import IntegrityError, FkConstraintViolation, NoResultFound
from falcon_rest.helpers import check_permission, get_request_ip
from falcon_rest.logger import log
from falcon_rest.resources.base_resource import OperationalError
from falcon_rest.resources.resources import swagger, ResourcesBaseClass, DEFAULT_SECURITY, ATTRIBUTE_ERROR_RE
from falcon_rest.responses import errors
# from .tasks import *
from api_lic import model
from api_lic.resources.resources import Resource, CustomAction, Create, List
from api_lic.scheme import UserInfoScheme, UserInfoSchemeGet, UserResetPasswordLetterScheme
from api_lic.view import DEFAULT_SECURITY
from api_lic.views.admin import LicenseScheme, LicenseSchemeGet, LicenseSchemeModify, LicenseLrnScheme, \
    LicenseLrnSchemeGet, LicenseLrnSchemeModify, LicensePeriodScheme, LicensePeriodSchemeGet, LicensePeriodSchemeModify, \
    LicenseSwitchScheme, LicenseSwitchSchemeGet, LicenseSwitchSchemeModify, NotificationSchemeGet, PaymentScheme, \
    PaymentSchemeGet, PaymentSchemeModify
from ..scheme import *
from ..scheme import _valid
from ..resources.resources import Create, Resource, List, CustomAction, CustomPostAction
from ..rbac.rbac_role import UserRole, AdminRole


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


class UserInfoResource(Resource):
    model_class = model.User
    scheme_class = UserInfoScheme
    scheme_class_get = UserInfoSchemeGet
    scheme_class_modify = UserInfoSchemeModify
    entity = 'User'
    unique_field = 'email'
    has_delete_operation = False
    security = (DEFAULT_SECURITY)
    restrict = ()

    def on_get(self, req, resp, **kwargs):
        kwargs['user_uuid'] = self.get_user(req).user_uuid

        return super(UserInfoResource, self).on_get(req, resp, **kwargs)

    def on_patch(self, req, resp, **kwargs):
        kwargs['user_uuid'] = self.get_user(req).user_uuid
        return super(UserInfoResource, self).on_patch(req, resp, **kwargs)


class UserResetPasswordEmail(CustomAction):
    scheme_class = UserResetPasswordLetterScheme
    body_parameters = ('Email to check', UserResetPasswordLetterScheme)
    method = 'post'
    model_class = model.User

    def on_post(self, req, resp, **kwargs):
        return self.proceed(req, resp, **kwargs)

    def apply(self, obj, req, resp, **kwargs):
        from falcon_rest.contrib.auth import auth
        user = model.User.filter(email=req.data['email']).first()
        if user:
            user.token = auth.get_token(user)
            user.apply_mail('retrieve_password')
            # model.MailSender.apply_mail(user, 'retrieve_password', obj.client.billing_email)


class LicenseCreate(Create):
    scheme_class = LicenseScheme
    model_class = model.License
    entity = 'License'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def before_create(self, obj, **kwargs):
        user = self.get_user(self.req)
        obj.user_uuid=user.user_uuid
        # obj.created_by=user.name
        # obj.created_on=datetime.now(UTC)
        return obj


class LicenseResource(Resource):
    model_class = model.License
    scheme_class = LicenseScheme
    scheme_class_get = LicenseSchemeGet
    scheme_class_modify = LicenseSchemeModify
    entity = 'License'
    id_field = 'license_uuid'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()

    def get_object(self, resp, model_class, **kwargs):
        obj = super().get_object(resp, model_class, **kwargs)
        user = self.get_user(self.req)
        if user.get_role() == UserRole and obj.user_uuid != user.user_user_uuid:
            raise NoResultFound
        return obj


class LicenseList(List):
    scheme_class = LicenseSchemeGet
    model_class = model.License
    entity_plural = 'Licenses'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        if user.get_role() != AdminRole:
            cls = self.model_class
            ret = ret.filter(cls.user_uuid == user.user_uuid)
        return filt, ret


class LicensePeriodCreate(Create):
    scheme_class = LicensePeriodScheme
    model_class = model.LicensePeriod
    entity = 'LicensePeriod'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def before_create(self, obj, **kwargs):
        user = self.get_user(self.req)
        lic = model.License.get(obj.license_uuid)
        if lic.user_uuid != user.user_uuid:
            raise ValidationError({'license_uuid':['not owned by current user!']})
        # obj.created_by=user.name
        # obj.created_on=datetime.now(UTC)
        return obj


class LicensePeriodResource(Resource):
    model_class = model.LicensePeriod
    scheme_class = LicensePeriodScheme
    scheme_class_get = LicensePeriodSchemeGet
    scheme_class_modify = LicensePeriodSchemeModify
    entity = 'LicensePeriod'
    id_field = 'license_period_uuid'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()

    def get_object(self, resp, model_class, **kwargs):
        obj = super().get_object(resp, model_class, **kwargs)
        user = self.get_user(self.req)
        if user.get_role() == UserRole and obj.user_uuid != user.user_user_uuid:
            raise NoResultFound
        return obj


class LicensePeriodList(List):
    scheme_class = LicensePeriodSchemeGet
    model_class = model.LicensePeriod
    entity_plural = 'LicensePeriods'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        if user.get_role() != AdminRole:
            cls = self.model_class
            ret = ret.filter(cls.user_uuid == user.user_uuid)
        return filt, ret


class NotificationList(List):
    scheme_class = NotificationSchemeGet
    model_class = model.Notification
    entity_plural = 'Notifications'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        if user.get_role() != AdminRole:
            cls = self.model_class
            ret = ret.filter(cls.user_uuid == user.user_uuid)
        return filt, ret


class PaymentCreate(Create):
    scheme_class = PaymentScheme
    model_class = model.Payment
    entity = 'Payment'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def before_create(self, obj, **kwargs):
        user = self.get_user(self.req)
        lic = model.LicensePeriod.get(obj.license_period_uuid)
        if lic.license.user_uuid != user.user_uuid:
            raise ValidationError({'license_uuid': ['not owned by current user!']})
        # obj.created_by=user.name
        # obj.created_on=datetime.now(UTC)
        return obj


class PaymentResource(Resource):
    model_class = model.Payment
    scheme_class = PaymentScheme
    scheme_class_get = PaymentSchemeGet
    scheme_class_modify = PaymentSchemeModify
    entity = 'Payment'
    id_field = 'payment_uuid'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()

    def get_object(self, resp, model_class, **kwargs):
        obj = super().get_object(resp, model_class, **kwargs)
        user = self.get_user(self.req)
        if user.get_role() == UserRole and obj.user_uuid != user.user_user_uuid:
            raise NoResultFound
        return obj


class PaymentList(List):
    scheme_class = PaymentSchemeGet
    model_class = model.Payment
    entity_plural = 'Payments'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        if user.get_role() != AdminRole:
            cls = self.model_class
            ret = ret.filter(cls.user_uuid == user.user_uuid)
        return filt, ret
