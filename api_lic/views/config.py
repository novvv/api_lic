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
# +++ConfigPayment+++
class ConfigPaymentResource(Resource):
    model_class = model.ConfigPayment
    scheme_class = ConfigPaymentScheme
    scheme_class_get = ConfigPaymentSchemeGet
    scheme_class_modify = ConfigPaymentSchemeModify
    entity = 'ConfigPayment'
    #id_field = 'id'
    security = (DEFAULT_SECURITY)
    path_parameters = ()
    restrict = ()
    has_delete_operation = False

    def get_object_data(self, resp, model_class, scheme_class, **kwargs):
        kwargs['id'] = 1
        obj = self.get_object(resp, model_class, **kwargs)
        if not obj:
            obj = model_class(id=1)
        return scheme_class().dump(obj).data

    def update_object(self, req, resp, model_class, scheme_class, **kwargs):
        kwargs['id'] = 1
        self.init_req(req)
        obj = self.get_object(resp, model_class, **kwargs)
        if not obj:
            self.model_class(id=1).save()
        scheme = scheme_class().load(self.req_data, instance=self.before_update(obj, req), partial=True)
        if scheme.errors:
            self.set_response(resp, responses.ValidationErrorResponse(data=scheme.errors))
            return False
        result = scheme.data.save(save_history=True, user=self.get_user(req))
        self.after_update(result, obj, scheme.data)
        return result

# ---ConfigPayment---

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

