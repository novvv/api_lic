# from falcon_rest.db import fields, orm , get_db
# from falcon_rest.db import Column
# from falcon_rest.conf import settings
# from falcon_rest.contrib.files import create_file_model_class, create_scheme
# from falcon_rest.contrib.files.endpoints import UploadFile, GetDownloadLink, DownloadFile, ShowFile
# from marshmallow_sqlalchemy import field_for, fields as sa

# from api_dnl.base_model import DnlApiBaseModel
# from api_dnl.model import rev
from sqlalchemy.sql import func, select, case, cast, alias, literal
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import (Column, desc, and_, or_, text as text_, PrimaryKeyConstraint, inspect, Sequence,
                        UniqueConstraint)
from falcon_rest.responses import responses
from.auth import DEFAULT_SECURITY
# from .tasks import *
from ..scheme import *
from ..resources.resources import Create, Resource, List


class EmailTemplateCreate(Create):
    scheme_class = EmailTemplateScheme
    model_class = model.EmailTemplate
    entity = 'EmailTemplate'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()


class EmailTemplateResource(Resource):
    model_class = model.EmailTemplate
    scheme_class = EmailTemplateScheme
    scheme_class_get = EmailTemplateSchemeGet
    entity = 'EmailTemplate'
    id_field = 'name'
    unique_field = 'name'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()
    has_delete_operation = False


class EmailTemplateList(List):
    scheme_class = EmailTemplateSchemeGet
    model_class = model.EmailTemplate
    entity_plural = 'EmailTemplate list'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()






# +++Notification+++
class NotificationCreate(Create):
    scheme_class = NotificationScheme
    model_class = model.Notification
    entity = 'Notification'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def before_create(self, obj, **kwargs):
        user = self.get_user(self.req)
        # obj.created_by=user.name
        # obj.created_on=datetime.now(UTC)
        return obj


class NotificationResource(Resource):
    model_class = model.Notification
    scheme_class = NotificationScheme
    scheme_class_get = NotificationSchemeGet
    scheme_class_modify = NotificationSchemeModify
    entity = 'Notification'
    id_field = 'notification_uuid'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()


# ---Notification---

# +++Plan+++
class PlanCreate(Create):
    scheme_class = PlanScheme
    model_class = model.Plan
    entity = 'Plan'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def before_create(self, obj, **kwargs):
        user = self.get_user(self.req)
        # obj.created_by=user.name
        # obj.created_on=datetime.now(UTC)
        return obj


class PlanResource(Resource):
    model_class = model.Plan
    scheme_class = PlanScheme
    scheme_class_get = PlanSchemeGet
    scheme_class_modify = PlanSchemeModify
    entity = 'Plan'
    id_field = 'plan_uuid'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()

# ---Plan---
# +++PackageLrn+++
class PackageLrnCreate(Create):
    scheme_class = PackageLrnScheme
    model_class = model.PackageLrn
    entity = 'PackageLrn'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()
    unique_field = 'package_name'
    def before_create(self, obj, **kwargs):
        user = self.get_user(self.req)
        #obj.created_by=user.name
        #obj.created_on=datetime.now(UTC)
        return obj
class PackageLrnResource(Resource):
    model_class = model.PackageLrn
    scheme_class = PackageLrnScheme
    scheme_class_get = PackageLrnSchemeGet
    scheme_class_modify = PackageLrnSchemeModify
    entity = 'PackageLrn'
    id_field = 'package_lrn_uuid'
    unique_field = 'package_name'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()
class PackageLrnList(List):
    scheme_class = PackageLrnSchemeGet
    model_class = model.PackageLrn
    entity_plural = 'PackageLrns'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()
    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        if not user.is_admin:
            cls = self.model_class
            #ret = ret.filter(cls.pool_id != 0)#TODO:filter for user
        return filt, ret
# ---PackageLrn---

# +++DnlLicenseInfo+++
class DnlLicenseInfoCreate(Create):
    scheme_class = DnlLicenseInfoScheme
    model_class = model.DnlLicenseInfo
    entity = 'DnlLicenseInfo'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()
    def before_create(self, obj, **kwargs):
        user = self.get_user(self.req)
        #obj.created_by=user.name
        #obj.created_on=datetime.now(UTC)
        return obj
class DnlLicenseInfoResource(Resource):
    model_class = model.DnlLicenseInfo
    scheme_class = DnlLicenseInfoScheme
    scheme_class_get = DnlLicenseInfoSchemeGet
    scheme_class_modify = DnlLicenseInfoSchemeModify
    entity = 'DnlLicenseInfo'
    id_field = 'id'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()
class DnlLicenseInfoList(List):
    scheme_class = DnlLicenseInfoSchemeGet
    model_class = model.DnlLicenseInfo
    entity_plural = 'DnlLicenseInfos'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()
    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        if not user.is_admin:
            cls = self.model_class
            #ret = ret.filter(cls.pool_id != 0)#TODO:filter for user
        return filt, ret
# ---DnlLicenseInfo---

# +++PackageSwitch+++
class PackageSwitchCreate(Create):
    scheme_class = PackageSwitchScheme
    model_class = model.PackageSwitch
    entity = 'PackageSwitch'
    unique_field = 'package_name'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()
    def before_create(self, obj, **kwargs):
        user = self.get_user(self.req)
        #obj.created_by=user.name
        #obj.created_on=datetime.now(UTC)
        return obj



class PackageSwitchResource(Resource):
    model_class = model.PackageSwitch
    scheme_class = PackageSwitchScheme
    scheme_class_get = PackageSwitchSchemeGet
    scheme_class_modify = PackageSwitchSchemeModify
    entity = 'PackageSwitch'
    id_field = 'package_switch_uuid'
    unique_field = 'package_name'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()
class PackageSwitchList(List):
    scheme_class = PackageSwitchSchemeGet
    model_class = model.PackageSwitch
    entity_plural = 'PackageSwitchs'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()
    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        if not user.is_admin:
            cls = self.model_class
            #ret = ret.filter(cls.pool_id != 0)#TODO:filter for user
        return filt, ret
# ---PackageSwitch---


class LicenseLrnAdminResource(Resource):
    model_class = model.LicenseLrn
    scheme_class = LicenseLrnScheme
    scheme_class_get = LicenseLrnSchemeGet
    scheme_class_modify = LicenseLrnSchemeModify
    entity = 'LicenseLrn'
    id_field = 'user_uuid'
    security = (DEFAULT_SECURITY)
    path_parameters = ({'name':'package_lrn_uuid','description':'package uuid'},)
    restrict = ()
    has_modify_operation = False
    has_info_operation = False

    def delete_object(self, req, resp, model_class, **kwargs):
        cls=self.model_class
        q = cls.filter(and_(cls.package_lrn_uuid==kwargs['package_lrn_uuid'],cls.user_uuid==kwargs['user_uuid'])).first()
        if q:
            kwargs = {'license_lrn_uuid': q.license_lrn_uuid}
            return super().delete_object(req,resp, model_class, **kwargs)
        else:
            self.set_response(resp, responses.ObjectNotFoundErrorResponse())
            return None

class LicenseSwitchAdminResource(Resource):
    model_class = model.LicenseSwitch
    scheme_class = LicenseSwitchScheme
    scheme_class_get = LicenseSwitchSchemeGet
    scheme_class_modify = LicenseSwitchSchemeModify
    entity = 'LicenseSwitch'
    id_field = 'user_uuid'
    security = (DEFAULT_SECURITY)
    path_parameters = ({'name':'package_switch_uuid','description':'package uuid'},)
    restrict = ()
    has_modify_operation = False
    has_info_operation = False

    def delete_object(self, req, resp, model_class, **kwargs):
        cls=self.model_class
        q = cls.filter(and_(cls.package_switch_uuid==kwargs['package_switch_uuid'],cls.user_uuid==kwargs['user_uuid'])).first()
        if q:
            kwargs = {'license_switch_uuid': q.license_switch_uuid}
            return super().delete_object(req,resp, model_class, **kwargs)
        else:
            self.set_response(resp, responses.ObjectNotFoundErrorResponse())
            return None


# +++TransactionLog+++

class TransactionLogResource(Resource):
    model_class = model.TransactionLog
    scheme_class = TransactionLogScheme
    scheme_class_get = TransactionLogSchemeGet
    entity = 'TransactionLog'
    id_field = 'transaction_log_uuid'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()
    has_modify_operation = False
    has_delete_operation = False

class TransactionLogList(List):
    scheme_class = TransactionLogSchemeGet
    model_class = model.TransactionLog
    entity_plural = 'TransactionLogs'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()
    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
        user = self.get_user(self.req)
        if not user.is_admin:
            cls = self.model_class
            #ret = ret.filter(cls.pool_id != 0)#TODO:filter for user
        return filt, ret
# ---TransactionLog---
