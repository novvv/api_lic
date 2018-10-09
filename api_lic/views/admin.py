# from falcon_rest.db import fields, orm , get_db
# from falcon_rest.db import Column
# from falcon_rest.conf import settings
# from falcon_rest.contrib.files import create_file_model_class, create_scheme
# from falcon_rest.contrib.files.endpoints import UploadFile, GetDownloadLink, DownloadFile, ShowFile
# from marshmallow_sqlalchemy import field_for, fields as sa

# from api_dnl.base_model import DnlApiBaseModel
# from api_dnl.model import rev

from falcon_rest.resources.resources import DEFAULT_SECURITY
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

# +++Rate+++
class RateCreate(Create):
    scheme_class = RateScheme
    model_class = model.Rate
    entity = 'Rate'
    path_parameters = ()
    security = (DEFAULT_SECURITY)
    restrict = ()

    def before_create(self, obj, **kwargs):
        user = self.get_user(self.req)
        # obj.created_by=user.name
        # obj.created_on=datetime.now(UTC)
        return obj


class RateResource(Resource):
    model_class = model.Rate
    scheme_class = RateScheme
    scheme_class_get = RateSchemeGet
    scheme_class_modify = RateSchemeModify
    entity = 'Rate'
    id_field = 'rate_uuid'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()

# ---Rate---