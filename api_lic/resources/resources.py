import json
from xmljson import BadgerFish as bf,Parker as X2J
from xml.etree.ElementTree import Element,fromstring,tostring
import xml.etree.ElementTree as ET
from xml.dom import minidom
from api_lic.__version__ import __version__ as VERSION
from datetime import datetime
from pytz import UTC
from dateutil.parser import parse as parse_datetime
from csv import DictWriter
import falcon
from falcon_rest.db.errors import IntegrityError, FkConstraintViolation, DataError,NoResultFound
from falcon_rest import schemes, swagger, responses
from falcon_rest.responses import errors,SuccessResponseObjectInfo,SuccessResponseObjectsList,\
    SuccessResponse,SuccessResponseJustOk,ValidationErrorResponse
from falcon_rest.helpers import check_permission
from falcon_rest.resources.base_resource import BaseResource,OperationalError
from falcon_rest.logger import log
from falcon_rest.resources.resources import Create as _Create,Resource as _Resource,List as _List,\
    CustomAction as _CustomAction,CustomPatchAction as _CustomPatchAction,\
    DEFAULT_SECURITY,RestrictedModel,RestrictRule,PreConditionFailedException,ATTRIBUTE_ERROR_RE
from urllib.parse import parse_qsl
from falcon_rest import conf
from falcon_rest.conf import settings
from sqlalchemy import (Column, desc, and_,or_, text as text_, PrimaryKeyConstraint, inspect)
from sqlalchemy import (
    Integer, SmallInteger, Float, Text, String, DateTime, Date, Time, Boolean, ForeignKey, BigInteger
)
from api_lic.fields import Choice
from marshmallow.fields import validate
from marshmallow import (
    Schema, pre_load, pre_dump, post_dump, post_load, validates_schema,
    validate,validates, fields, ValidationError
)
from ..rbac.rbac_role import UserRole, CompanyAdminRole, AdminRole,ResellerRole
import io,csv
import xlwt
import uuid

def generate_uuid_str():
    return lambda: str(uuid.uuid4())


class SuccessResponseJustOk201(responses.SuccessResponseJustOk):
    status_code = 201
    falcon_status_code = falcon.HTTP_201

class AlreadyExistsResponse(responses.OperationErrorResponse):
    tpl = '{} error: {}'
    def __init__(self,entity,msg):
        self.data=errors.Error(code=1000, reason='already_exists',
                        message='{} error {}'.format(entity,msg) )

def user_context(self, req, resp, **kwargs):
    user = self.get_user(req)
    if user and user.get_role() in (UserRole,CompanyAdminRole) and hasattr(self,'is_company') and self.is_company and not 'company_uuid' in kwargs:
        kwargs['company_uuid']=user.company_uuid
    # if user and user.get_role() in (ResellerRole) and hasattr(self,'is_reseller') and self.is_reseller and not 'reseller_uuid' in kwargs:
    #     kwargs['reseller_uuid']=user.reseller_uuid
    return kwargs

class Create(_Create):
    ext_body_parameters = ()
    def on_post(self, req, resp, **kwargs):
        self.init_req(req)
        kwargs=user_context(self, req, resp, **kwargs)
        self.apply_restrict_rules(req, kwargs)
        scheme = self.scheme_class()
        if not check_permission(self, req, 'create'):
            self.set_response(
                resp, responses.ForbiddenErrorResponse(data=errors.AuthErrors.Forbidden)
            )
            return

        if self.check_request_data(req, resp, scheme):
            try:
                data = self.create_object(req, scheme, **kwargs)
                self.set_response(
                    resp, self.scheme_class.get_object_created_response(data=data)
                )
                self.after_create(data, req, resp, **kwargs)
            except IntegrityError as e:
                #self.set_response(resp, responses.AlreadyExistsResponse(
                #    data=errors.CommonErrors.get_already_exists_error(self.entity, self.unique_field))
                #)
                try:
                    msg = str(e).split('\n')[1].split(':')[1]
                except:
                    msg = str(e)

                self.set_response(resp, AlreadyExistsResponse(self.entity,msg) )

            except FkConstraintViolation as e:
                self.set_response(resp, responses.FkConstraintViolationResponse(
                    data=errors.CommonErrors.get_fk_violation_error(
                        e.table_name, e.fk_column_name, e.column_name, e.value)
                )
                )
            except schemes.validate.ValidationError as e:
                self.set_response(resp, responses.ValidationErrorResponse(data=e.messages))

            except DataError as e:
                log.error(e)
                #self.set_response(resp, responses.OperationErrorResponse(data=errors.CommonErrors.DataError))
                self.set_response( resp,OperationalError(e) )

            except Exception as e:
                log.error(e)
                # self.set_response(resp, responses.OperationErrorResponse(data=errors.CommonErrors.DataError))
                self.set_response(resp, OperationalError(e))

    def get_spec(self):
        if self.unique_field:
            additional_responses = self.additional_responses + (
                responses.AlreadyExistsResponse(entity=[self.entity, self.unique_field]),
            )
        else:  # pragma: no cover
            additional_responses = self.additional_responses
        if self.ext_body_parameters == ():
            return swagger.specify.get_spec(
                method='post', description='Creates new {}'.format(self.entity.lower()),
                path_parameters=self.path_parameters,
                body_parameters=('{} to create'.format(self.entity), self.scheme_class),
                responses=(
                    self.scheme_class.get_object_created_response(entity=self.entity),
                    responses.ValidationErrorResponse(),
                    responses.FkConstraintViolationResponse()
                ) + additional_responses + self.get_additional_responses(method='post'),
                security=self.get_security(method='post'),
                #consumes='multipart/form-data',
                #ext_body_parameters=self.ext_body_parameters
            )
        else:
            return swagger.specify.get_spec(
                method='post', description='Creates new {}'.format(self.entity.lower()),
                path_parameters=self.path_parameters,
                #body_parameters=('{} to create'.format(self.entity), self.scheme_class),
                responses=(
                              self.scheme_class.get_object_created_response(entity=self.entity),
                              responses.ValidationErrorResponse(),
                              responses.FkConstraintViolationResponse()
                          ) + additional_responses + self.get_additional_responses(method='post'),
                security=self.get_security(method='post'),
                consumes=['application/json','multipart/form-data'],
                ext_body_parameters=(
                                        {
                                            'name':'body',
                                            'type':'object',
                                            'in': 'body',
                                            'description':'{} to create'.format(self.entity),
                                            'schema':{
                '$ref': '#/definitions/{}'.format(self.scheme_class.__name__.replace('Scheme', ''))
                                    }
                                        },
                                    )+self.ext_body_parameters
            )

    def create_object(self, req, scheme, **kwargs):
        if hasattr(self, 'no_auth_needed') and self.no_auth_needed:
            return self.before_create(
                self.get_loaded_data(scheme), **kwargs
            ).save()
        else:
            return self.before_create(
                self.get_loaded_data(scheme), **kwargs
            ).save(save_history=True, user=self.get_user(req))

    def after_create(self,object_id, req, resp, **kwargs):
        pass

class Resource(_Resource):
    @classmethod
    def create(
            cls, model_class, scheme_class, scheme_class_get, entity, id_field, has_update_by=False, unique_field=None,
            scheme_class_modify=None, security=None, restrict=()
    ):
        return type(
            '{}.Resource'.format(model_class.__module__), (cls,),
            dict(
                model_class=model_class, scheme_class=scheme_class, scheme_class_get=scheme_class_get,
                scheme_class_modify=scheme_class_modify,
                entity=entity, id_field=id_field,
                has_update_by=has_update_by, unique_field=unique_field,
                security=(security if security is not None else DEFAULT_SECURITY),
                restrict=restrict
            )
        )
    def get_spec_info(self):
        return swagger.specify.get_spec(
            method='get', description='Gets {}'.format(self.entity.lower()),
            path_parameters=self.get_path_parameters(),
            responses=self.get_common_on_get_responses() + self.get_additional_responses(method='get'),
            security=self.get_security(method='get', action='info')
        )
    def get_spec_modify(self):
        if self.scheme_class or self.scheme_class_modify:
            body_parameters = (
                '{} to modify'.format(self.entity),
                self.scheme_class_modify if self.scheme_class_modify else self.scheme_class

            )
        else:
            body_parameters = ()

        return swagger.specify.get_spec(
            method='patch', description='Modifies {}'.format(self.entity.lower()),
            path_parameters=self.get_path_parameters(),
            body_parameters=body_parameters,
            responses=
                #responses.SuccessResponseJustOk(),
                self.get_common_on_get_responses()
                #responses.ObjectNotFoundErrorResponse()
             + self.get_additional_responses(method='patch'),
            security=self.get_security(method='patch', action='modify')
        )
    def on_get(self, req, resp, **kwargs):  # pragma: no cover
        self.init_req(req)
        kw=user_context(self, req, resp, **kwargs)
        try:
            ret = super(Resource, self).on_get(req, resp, **kw)
        except NoResultFound:
            self.set_response(resp, responses.ObjectNotFoundErrorResponse())
            return None


    def before_delete(self, obj, req, resp, **kwargs):
        return True

    def on_delete(self, req, resp, **kwargs):
        self.init_req(req)
        if not self.has_delete_operation:  # pragma: no cover
            return self.method_not_allowed_response(resp, 'DELETE')
        obj =  self.get_object(resp, self.model_class, **kwargs)
        if not check_permission(self, req, 'delete', obj):
            self.set_response(
                resp, responses.ForbiddenErrorResponse(data=errors.AuthErrors.Forbidden)
            )
            return

        kw = user_context(self, req, resp, **kwargs)
        try:
            self.before_delete( obj, req, resp, **kwargs)
        except Exception as e:
            self.set_response(resp, OperationalError(e))
            return
        try:
            if self.delete_object(req, resp, self.model_class, **kwargs):
                self.set_response(resp, responses.SuccessResponseJustOk())
        except NoResultFound:
            self.set_response(resp, responses.ObjectNotFoundErrorResponse())


    def on_patch(self, req, resp, **kwargs):
        self.init_req(req)
        kwargs=user_context(self, req, resp, **kwargs)
        if not self.has_modify_operation:  # pragma: no cover
            return self.method_not_allowed_response(resp, 'PATCH')

        if not check_permission(self, req, 'modify', self.get_object(resp, self.model_class, **kwargs)):
            self.set_response(
                resp, responses.ForbiddenErrorResponse(data=errors.AuthErrors.Forbidden)
            )
            return

        try:
            scheme = self.scheme_class_modify() if self.scheme_class_modify else self.scheme_class()
            if self.check_request_data(req, resp, scheme):
                if self.update_object(
                    req, resp, self.model_class,
                    self.scheme_class_modify if self.scheme_class_modify else self.scheme_class, **kwargs
                ):
                    data = self.get_object_data(resp, self.model_class, self.scheme_class_get, **kwargs)
                    if data:
                        self.set_response(resp, responses.SuccessResponseObjectInfo(data=data))
                    else:
                        self.set_response(resp, responses.SuccessResponseJustOk())
        except IntegrityError as e:
            try:
                msg = str(e).split('\n')[1].split(':')[1]
            except:
                msg = str(e)

            self.set_response(resp, AlreadyExistsResponse(self.entity, msg))
        except FkConstraintViolation as e:
            self.set_response(resp, responses.FkConstraintViolationResponse(
                data=errors.CommonErrors.get_fk_violation_error(e.table_name, e.column_name, e.value))
            )
        except ValidationError as e:
            self.set_response(resp, responses.ValidationErrorResponse(data=e.messages))
        except NoResultFound:
            self.set_response(resp, responses.ObjectNotFoundErrorResponse())
        except Exception as e:
            log.error(e)
            #self.set_response(resp, responses.OperationErrorResponse(data=errors.CommonErrors.DataError))
            self.set_response(resp, OperationalError(e) )

    def update_object(self, req, resp, model_class, scheme_class, **kwargs):
        self.init_req(req)
        obj = self.get_object(resp, model_class, **kwargs)
        if not obj:
            return None
        self.check_unique(obj,req)
        instance = self.before_update(obj, req)
        scheme = scheme_class().load(self.req_data, instance=instance, partial=True)
        if scheme.errors:
            self.set_response(resp, responses.ValidationErrorResponse(data=scheme.errors))
            return False
        user = self.get_user(req)
        if user:
            result = scheme.data.save(save_history=True, user=self.get_user(req))
        else:
            result = scheme.data.save()
        self.after_update(result, obj, scheme.data)
        model_class.session().refresh(obj)
        return result

    def check_unique(self,obj,req):
        if hasattr(self, 'unique_field') and self.unique_field:
            if type(self.unique_field)==type(''):
                all=(self.unique_field,)
            else:
                all = self.unique_field
            for unique_field in all:
                if unique_field in req.data:
                    new = req.data[unique_field]
                    old = getattr(obj, unique_field)
                    cls = self.model_class
                    field = getattr(cls, unique_field)
                    if new != old:
                        if cls.filter(field == new).first():
                            raise ValidationError({unique_field: ['{} {} is invalid (duplicate)'.format(field.name, new)]})

class PatchManyResource(_CustomPatchAction):
    modify_only=False

    def on_patch(self, req, resp, **kwargs):
        self.init_req(req)
        kwargs = user_context(self, req, resp, **kwargs)
        q=self.model_class.query().first()
        if  q:
            kwargs[self.id_field] = q.get_object_primary_key_value()
        else:
            self.model_class(**{self.id_field:1}).save()
            kwargs[self.id_field]='1'

        return self.proceed(req, resp, **kwargs)

    def apply(self, obj, req, resp, **kwargs):
        result = []
        updated = 0
        added = 0
        deleted = 0
        try:
            ids = [it[self.id_field] for it in req.data['items'] if self.id_field in it]
            if not self.modify_only:
                for obj in self.model_class.query().all():
                    if not obj.get_object_primary_key_value() in ids:
                        kwargs[self.id_field]=str(obj.get_object_primary_key_value())
                        if self.delete_object(req, resp, self.model_class, **kwargs):
                            deleted += 1

            for data in req.data['items']:
                req.data=data
                if self.id_field in data and not data[self.id_field]=='null' :
                    kwargs[self.id_field] = data[self.id_field]
                    if self.update_object(
                            req, resp, self.model_class,self.scheme_class, **kwargs):

                        updated += 1
                else:
                    if 'id' in kwargs:
                        del kwargs[self.id_field]
                    scheme = self.scheme_class(exclude=(self.id_field,))
                    if not self.modify_only:
                        if self.check_request_data(req, resp, scheme):
                            #resp = self.scheme_class.get_object_created_response(data=self.create_object(req, scheme, **kwargs) )
                            obj=self.create_object(req, scheme, **kwargs)
                            added +=1

            if (updated+deleted+added)>0:
                self.set_response(
                    resp, responses.SuccessResponse(
                        data={
                            'updated': updated,
                            'deleted': deleted,
                            'added': added,

                        },
                        scheme=schemes.ObjectScheme
                    )
                )
                return True
            else:
                self.set_response(
                    resp, responses.SuccessResponseJustOk())
                return True

        except IntegrityError as e:
            try:
                msg = str(e).split('\n')[1].split(':')[1]
            except:
                msg = str(e)

            self.set_response(resp, AlreadyExistsResponse(self.entity, msg))
            return False
        except FkConstraintViolation as e:
            self.set_response(resp, responses.FkConstraintViolationResponse(
                data=errors.CommonErrors.get_fk_violation_error(e.table_name, e.column_name, e.value))
            )
            return False
        except Exception as e:
            self.set_response(resp, OperationalError(e))
            return False

def dict_to_csv(data):
    import csv
    import io
    csvfile = io.StringIO()
    if len(data):
        fieldnames = list(data[0].keys())
        #fieldnames = ['orig_code','calls','non_zero_calls','ingress_billed_min','ingress_billed_time','ingress_cost','ingress_time','avg_rate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        return csvfile.getvalue()#str.encode(csvfile.getvalue())
    else:
        return None

def dict_to_xls(data,name=None):

    wb = xlwt.Workbook(encoding='utf-8')
    if not name:
        name='Excel export sheet'
    ws = wb.add_sheet(name)
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    if len(data):
        for c, col in enumerate(data[0]):
            ws.write(0, c, col, font_style)
        for r, row in enumerate(data):
            for c, col in enumerate(row):
                ws.write(r+1, c, row[col],font_style)
    #response = io.StringIO()
    response = io.BytesIO()
    wb.save(response)
    return response.getvalue()

def xml_tostring(x):
    if x == None:
        return ''
    else:
        return str(x)

import  falcon


class List(_List):
    allow_methods = ['get']
    entity_plural = None
    model_class = None

    def _on_get(self, req, resp, **kwargs):
        if (not hasattr(self,'no_auth_needed') or self.no_auth_needed == False )and not check_permission(self, req, 'list'):
            self.set_response(
                resp, responses.ForbiddenErrorResponse(data=errors.AuthErrors.Forbidden)
            )
            return
        try:
            objects_list, total, page, per_page = self.get_objects_list(req, self.model_class, **kwargs)
            self.set_response(
                resp, responses.SuccessResponse(
                    data={
                        'items': self.scheme_class().dump(objects_list, many=True).data,
                        'total': total, 'page': page, 'per_page': per_page
                    },
                    scheme=schemes.ObjectScheme
                )
            )
        except AttributeError as e:
            self.set_response(
                resp, responses.AttributeNotExitsErrorResponse(
                    data=ATTRIBUTE_ERROR_RE.search(str(e)).group(1)
                )
            )
        except Exception as e:
            log.error(e)
            #self.set_response(resp, responses.OperationErrorResponse(data=errors.CommonErrors.DataError))
            self.set_response(resp, OperationalError(e) )

    def on_get(self, req, resp, **kwargs):  # pragma: no cover
        self.init_req(req)
        kwargs = user_context(self, req, resp, **kwargs)
        try:
            #ret = super(IcxList,self).on_get(req, resp, **kwargs)
            ret = self._on_get(req, resp, **kwargs)
        except NoResultFound:
            self.set_response(resp, responses.ObjectNotFoundErrorResponse())
            return None
        if req.headers['ACCEPT']=='application/xml' or req.headers['ACCEPT']=='text/xml':
            data = json.loads(resp.body)
            result = bf(xml_tostring=xml_tostring).etree(data=data, root=Element('xml',attrib={'entity':self.model_class.__name__,'api_version':VERSION,'timestamp':str(datetime.utcnow())}))
            rough_string = tostring(result, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            resp.body = reparsed.toprettyxml(indent='\t')
            resp.content_type = 'text/xml'
        if req.headers['ACCEPT']=='text/csv':
            data = json.loads(resp.body)
            csvfile = io.StringIO()
            items=data['payload']['items']
            if len(items):
                fieldnames = data['payload']['items'][0].keys()
                writer = DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(items)
                resp.body = str.encode(csvfile.getvalue())
            else:
                resp.body=''
            resp.content_type = 'text/csv'

        return ret

    def get_filtering_for_list(self, parsed_qs, **kwargs):
        filtering = {}
        for k, v in parsed_qs.items():
            if k in ['per_page', 'page', 'order_by', 'order_dir','auth_token']:
                continue
            filtering[k] = v
        return filtering

    def modify_query_from_ordering_for_list(self, ordering, query, **kwargs):
        if 'by' in ordering:
            if ordering['by'] not in self.get_all_fields_from_scheme(self.scheme_class)[0]:
                raise Exception('Order by {} not valid!'.format(ordering['by']))
        return ordering, query

    def get_objects_list(self, req, model_class, **kwargs):
        parsed_qs = dict(parse_qsl(req.query_string))
        try:
            per_page = int(parsed_qs.get('per_page'))
        except (ValueError, TypeError):
            per_page = conf.get_default_items_per_page()

        try:
            page = int(parsed_qs.get('page', 0))
        except ValueError:
            page = 0

        if hasattr(self, 'per_page_limit') and per_page > self.per_page_limit:
            raise ValidationError('per_page  over limit {}'.format(self.per_page_limit))

        if 'order_by' in parsed_qs:
            ordering = {
                'by': parsed_qs['order_by'],
                'dir': parsed_qs.get('order_dir', 'asc')
            }
        elif hasattr(self,'ordering'):
            ordering = self.ordering
        else:
            ordering = {}

        filtering = self.get_filtering_for_list(parsed_qs, **kwargs)

        filtering, query = \
            self.modify_query_from_filtering_for_list(filtering, **kwargs)

        if False:
            for c in inspect(self.model_class).columns:
                if c.name in ['alias','name','template_name','group_name']:
                    query = query.filter(or_(c.is_(None),c.notlike('#%')))
                    break


        if ordering:
            ordering, query = \
                self.modify_query_from_ordering_for_list(ordering, query, **kwargs)

        return model_class.get_objects_list(
            query=query,
            filtering=filtering,
            ordering=ordering,
            paging={'from': page * per_page, 'till': (page + 1) * per_page}
        ) + (page, per_page)


    @staticmethod
    def parse_query_field(k,model):
        trans = {'gt': ' >= ', 'gte': ' >= ', 'lt': ' <= ', 'lte': ' <= ', 'in': ' in ({})','eq':' = ', 'isnull':' is null = {}'}
        suffix=k.split('_')[-1]
        if not suffix in trans.keys():
            suffix = 'eq'
            qfield = k
        else:
            qfield='_'.join(k.split('_')[0:-1])
        insp = inspect(model)
        cols = insp.columns
        syns = insp.synonyms
        field=qfield
        if qfield in syns:
            field = syns[qfield].name
        postfix="'{}'"
        try:
            typ=cols[field].type
            if isinstance(typ,DateTime) or isinstance(typ,String) or isinstance(typ,Date):
                postfix="'{}'"
            if suffix in ['in','isnull']:
                postfix = ''
        except:
            postfix = "'{}'"

        if field in cols and hasattr(cols[field],'_element'):
            dbfield=str(cols[field].expression)#_element)
        else:
            dbfield = field
        if suffix in trans.keys():
            return dbfield + trans[suffix]+postfix,qfield
        return k,qfield



    def modify_query_from_filtering_for_list(self, filtering, **kwargs):
        if 'start_query' in kwargs:
            ret=kwargs['start_query']
        else:
            ret = self.model_class.query()

        filt = {}
        query_fields = self.scheme_class.Meta.query_fields if hasattr(self.scheme_class.Meta, 'query_fields') else []
        cols = inspect(self.model_class).columns
        syns = inspect(self.model_class).synonyms
        if filtering:
            for k, v in filtering.items():
                if hasattr(self, 'on_filtering'):
                    ret = getattr(self, 'on_filtering')(ret,k,v, kwargs)
                    continue
                if hasattr(self, 'on_filter_' + k):
                    ret = getattr(self, 'on_filter_' + k)(ret, v, kwargs)
                    continue
                if query_fields and k in query_fields:
                    fop,dbfield=List.parse_query_field(k, self.model_class)
                    if dbfield in cols:
                        col=cols[dbfield]
                    elif dbfield in syns:
                        col = cols[syns[dbfield].name]
                    else:
                        raise Exception('Bad value for filtering! field "{}" not found!'.format(dbfield))
                    if ' in ({})' in fop:
                        lst=v.split(',')
                        v1=[]
                        for i in lst:
                            t = 'unknown'
                            try:
                                if isinstance(col.type,Integer):
                                    t='int'
                                    x=int(i)
                                elif isinstance(col.type,Numeric):
                                    t='numeric'
                                    x=float(i)
                                    x = "'" + i + "'"
                                elif isinstance(col.type,DateTime) or isinstance(cols[dbfield].type,Date):
                                    t='datetime'
                                    x=parse_datetime(i)
                                    x = "'" + i + "'"
                                else:
                                    t = 'string'
                                    x = "'"+i+"'"
                                v1.append(i)
                            except Exception as e:
                                raise Exception('Bad value for filtering list! "{}" "{}" {}'.format(v,i,str(e)))
                        v=','.join(v1)
                    ret=ret.filter(text_(fop.format(v)))
                    continue
                if k in cols and hasattr(cols[k].type, 'choices'):
                    if not v in tuple(cols[k].type.choices.values()):
                        log.error('Bad value for filtering! {}={}'.format(k, v))
                        raise Exception('Bad value for filtering! "{}"="{}" must be one of [{}]'.format(k, v,','.join(list(cols[k].type.choices.values()))))
                        continue
                filt[k] = v

        return (filt, ret)

    @staticmethod
    def get_fields_from_scheme(scheme_class):  # pragma: no cover
        fields_list = []
        fields_names = []

        search_fields = scheme_class.Meta.search_fields if hasattr(scheme_class.Meta, 'search_fields') else []

        # noinspection PyProtectedMember
        for field_name, field in scheme_class._declared_fields.items():
            field_type = swagger.specify.get_field_type(field)

            #if isinstance(field,Numeric):
            #    field_type = 'string'
            if not field_type or field_name in []:
                continue

            if field_name not in search_fields:
                continue

            fields_names.append(field_name)

            if field_type == 'datetime' or field_name not in search_fields:
                continue

            f = {
                'name': field_name,
                'type': field_type
            }

            if isinstance(field.validate, validate.OneOf):
                f['enum'] = field.validate.choices
            if isinstance(field, Choice):
                f['enum'] = field._get_choices(field_name,scheme_class)

            fields_list.append(f)

        return sorted(fields_names), sorted(fields_list, key=lambda item: item['name'])
    @staticmethod
    def get_query_fields_from_scheme(scheme_class):
        fields_list = []
        fields_names = []
        query_fields = scheme_class.Meta.query_fields if hasattr(scheme_class.Meta, 'query_fields') else []
        for query_field in query_fields:
            fop,field_name=List.parse_query_field(query_field, scheme_class.Meta.model)
            decl=scheme_class._declared_fields
            if field_name in decl.keys():
                field=decl[field_name]
                field_type = swagger.specify.get_field_type(field)
                if not field_type and  isinstance(field, fields.Decimal):
                    field_type = 'number'
                if ' in ({})' in fop:
                    field_type = 'string'
                if ' is null' in fop:
                    field_type = 'boolean'
                if not field_type or field_name in []:
                    continue
                fields_names.append(field_name)
                f = {
                    'name': query_field,
                    'type': field_type
                }

                fields_list.append(f)

        return sorted(fields_names),sorted(fields_list, key=lambda item: item['name'])

    @staticmethod
    def get_all_fields_from_scheme(scheme_class):
        sfields_names, search_fields_list = List.get_fields_from_scheme(scheme_class)
        qfields_names, query_fields_list = List.get_query_fields_from_scheme(scheme_class)
        return sorted(sfields_names+qfields_names), \
                 sorted(search_fields_list+query_fields_list, key=lambda item: item['name'])

    def _get_spec_info(self):
        spec=super(List, self).get_spec_info()
        spec['get']['produces']=['application/json','text/csv','text/xml']
        return spec

    def get_spec(self):
        sfields_names, search_fields_list = self.get_fields_from_scheme(self.scheme_class)
        qfields_names, query_fields_list=self.get_query_fields_from_scheme(self.scheme_class)
        fields_names = list(set(sfields_names + qfields_names))
        spec = swagger.specify.get_spec(
            method='get', description='Gets {}'.format(self.entity_plural.lower()), path_parameters=self.path_parameters,
            query_parameters=[
                {'name': 'page', 'type': 'integer'}, {'name': 'per_page', 'type': 'integer'},
                {'name': 'order_by', 'enum': fields_names}, {'name': 'order_dir', 'enum': ['asc', 'desc']}
            ] + search_fields_list + query_fields_list,
            responses=(
                responses.SuccessResponseObjectsList(payload_scheme_items=self.scheme_class),
                responses.AttributeNotExitsErrorResponse()
            ) + self.get_additional_responses(method='get'),
            security=self.get_security(method='get')
        )
        spec['get']['produces'] = ['application/json', 'text/csv', 'text/xml']
        return spec

class CustomAction(_CustomAction):
    def proceed(self, req, resp, **kwargs):

        if (not hasattr(self, 'no_auth_needed') or self.no_auth_needed == False) and \
                not check_permission(self, req, self.action, self.get_object(resp, self.model_class, **kwargs)):
            self.set_response(
                resp, responses.ForbiddenErrorResponse(data=errors.AuthErrors.Forbidden)
            )
            return

        try:
            obj = self.get_object(resp, self.model_class, **kwargs)
            if self.check_conditions(obj, self.pre_conditions, lambda a, b: a == b):
                if self.check_conditions(obj, self.pre_conditions_inverted, lambda a, b: a != b):
                    if self.apply(obj, req, resp, **kwargs):
                        self.set_response(resp, responses.SuccessResponseJustOk())

        except FkConstraintViolation as e:
            self.set_response(resp, responses.FkConstraintViolationResponse(
                data=errors.CommonErrors.get_fk_violation_error(e.table_name, e.column_name, e.value))
            )
        except IntegrityError as e:
            try:
                msg = str(e).split('\n')[1].split(':')[1]
            except:
                msg = str(e)

            self.set_response(resp, AlreadyExistsResponse(self.entity, msg))
            return False
        except PreConditionFailedException as e:
            self.set_response(resp, responses.OperationErrorResponse(
                data=errors.CommonErrors.get_pre_condition_failed_error(e.message))
            )
        except Exception as e:
            self.set_response(resp, OperationalError(e))


class CustomPatchAction(CustomAction):
    method = 'patch'
    def on_patch(self, req, resp, **kwargs):
        self.init_req(req)
        kwargs = user_context(self, req, resp, **kwargs)
        return self.proceed(req, resp, **kwargs)

class CustomPostAction(CustomAction):
    method = 'post'
    def on_post(self, req, resp, **kwargs):
        self.init_req(req)
        kwargs = user_context(self, req, resp, **kwargs)
        return self.proceed(req, resp, **kwargs)

class CustomGetAction(CustomAction):
    method = 'get'
    query_parameters = []
    def on_get(self, req, resp, **kwargs):
        self.init_req(req)
        kwargs = user_context(self, req, resp, **kwargs)
        return self.proceed(req, resp, **kwargs)
    def get_spec(self):
        return swagger.specify.get_spec(
            method=self.method, description=self.description,
            path_parameters=self.path_parameters,
            query_parameters=self.query_parameters,
            body_parameters=self.body_parameters,
            responses=(
                responses.SuccessResponseJustOk(),
                responses.ObjectNotFoundErrorResponse()
            ) + self.additional_responses,
            security=self.get_security(method=self.method)
        )


class ObjectUpdatedScheme(Schema):
    updated = fields.Int()
    deleted = fields.Int()


class ResourceAll(Resource):
    has_info_operation = False
    scheme_class_get = ObjectUpdatedScheme

    def modify_query(self,filt,qs,req, resp, model_class, **kwargs):
        return filt,qs

    def get_query_filter(self, req, resp, model_class, **kwargs):
        filtering = dict(parse_qsl(req.query_string))
        qs = model_class.query()
        filtering,qs = self.modify_query(filtering,qs,req, resp, model_class, **kwargs)
        query_fields = self.scheme_class.Meta.query_fields if hasattr(self.scheme_class.Meta, 'query_fields') else []
        cols = inspect(self.model_class).columns
        if filtering:
            for k, v in filtering.items():
                if query_fields and k in query_fields:
                    fop=List.parse_query_field(k,self.model_class)[0]
                    qs=qs.filter(text_(fop.format(v)))
                    continue
                if k in cols and hasattr(cols[k].type, 'choices'):
                    if not v in tuple(cols[k].type.choices.values()):
                        log.error('Bad value for filtering! {}={}'.format(k, v))
                        raise Exception('Bad value for filtering! "{}"="{}" must be one of [{}]'.format(k, v,','.join(list(cols[k].type.choices.values()))))
                        continue
                if '*' in v:  # pragma: no cover
                    qs = qs.filter(getattr(model_class, k).like(v.replace('*', '%')))
                else:
                    qs = qs.filter(getattr(model_class, k) == v)
        return qs

    def update_object(self, req, resp, model_class, scheme_class, **kwargs):
        self.init_req(req)

        if hasattr(self.model_class, 'update_by'):
            self.req_data['update_by'] = self.get_user().name
        if hasattr(self.model_class,'update_on'):
            self.req_data['update_by'] = datetime.now(UTC)
        if hasattr(self.model_class,'update_at'):
            self.req_data['update_at'] = datetime.now(UTC)
        scheme = scheme_class().load(self.req_data)
        if scheme.errors:
            self.set_response(resp, responses.ValidationErrorResponse(data=scheme.errors))
            return False
        #result = self.model_class.query().update(self.req_data)
        query = self.get_query_filter(req, resp, model_class, **kwargs)
        result = query.update(self.req_data,synchronize_session='fetch')
        self.result=result
        self.model_class.session().commit()
        self.set_response(resp, responses.SuccessResponseObjectInfo(data={'updated':result}))
        return False

    def delete_object(self, req, resp, model_class, **kwargs):
        try:
            query=self.get_query_filter(req, resp, model_class, **kwargs)
            result = query.delete(synchronize_session='fetch')
            model_class.session().commit()
            self.set_response(resp, responses.SuccessResponseObjectInfo(data={'deleted': result}))
        except Exception as e:
            model_class.query().session.rollback()
            log.error('Mass delete error:{}'.format(str(e)))
        return False

    def get_spec_modify(self):
        if self.scheme_class or self.scheme_class_modify:
            body_parameters = (
                '{} to modify'.format(self.entity),
                self.scheme_class_modify if self.scheme_class_modify else self.scheme_class

            )
        else:
            body_parameters = ()

        return swagger.specify.get_spec(
            method='patch', description='Modifies multiple found {}'.format(self.entity.lower()),
            path_parameters=self.get_path_parameters(),
            body_parameters=body_parameters,
            query_parameters=List.get_all_fields_from_scheme(self.scheme_class)[1],
            responses=
                #responses.SuccessResponseJustOk(),
                self.get_common_on_get_responses()
                #responses.ObjectNotFoundErrorResponse()
             + self.get_additional_responses(method='patch'),
            security=self.get_security(method='patch', action='modify')
        )
    def get_spec_delete(self):
        return swagger.specify.get_spec(
            method='delete', description='Deletes multiple found {}'.format(self.entity.lower()),
            path_parameters=self.get_path_parameters(),
            query_parameters=List.get_all_fields_from_scheme(self.scheme_class)[1],
            responses= (
                responses.SuccessResponseObjectInfo(payload_scheme=self.scheme_class_get),
                responses.ObjectNotFoundErrorResponse()
            ) + self.get_additional_responses(method='delete'),
            security=self.get_security(method='delete', action='delete')
        )



def create_entity_endpoints(
        model_class, scheme_class, scheme_class_get, entity_sp, id_field, unique_field=None, has_update_by=False,
        additional_responses=None, path_parameters=None, scheme_class_modify=None, security=None, restrict=()
):
    if hasattr(model_class, 'restrict'):
        restrict = model_class.restrict
    return (
        Create.create(
            scheme_class, entity_sp[0], unique_field, additional_responses, path_parameters=path_parameters,
            **(dict(security=security['create']) if isinstance(security, dict) and 'create' in security else {}),
            restrict=restrict
        ),
        Resource.create(
            model_class, scheme_class, scheme_class_get, entity_sp[0], id_field,
            has_update_by=has_update_by, unique_field=unique_field,
            #scheme_class=scheme_class,
            #scheme_class_get=scheme_class_get,
            scheme_class_modify=scheme_class_modify,
            **(dict(security=security['resource']) if isinstance(security, dict) and 'resource' in security else {}),
            restrict=restrict
        ),
        List.create(
            model_class, scheme_class_get, entity_sp[1], path_parameters=path_parameters,
            **(dict(security=security['list']) if isinstance(security, dict) and 'list' in security else {}),
            restrict=restrict
        )
    )

def caps1(s):
    return ''.join([x.capitalize() for x in s.strip().split('/')])
def caps(s):
    return ''.join([x.capitalize() for x in caps1(s).strip().split('_')])

def gep(
        module, entity, id_field, put_under='',
        has_create=True, has_info=True, has_modify=True, has_delete=True, has_list=True, list_suffix='/list',
        permissions=None
):
    entity_name=caps1(put_under)+caps(entity)
    if hasattr(module, entity_name+'Create'):
        Create = getattr(module, entity_name+'Create',None)
        Create.has_create = has_create

    if hasattr(module, entity_name+'Resource'):
        Resource = getattr(module, entity_name+'Resource',None)

    if hasattr(module, entity_name+'List'):
        List = getattr(module, entity_name+'List',None)


    if settings.COLLECT_ENTITIES:
        permissions = permissions or []

    if put_under:
        put_under = '/{}'.format(put_under)

    end_points = []

    if has_create:
        end_points.append(
            {'path': '{}/{}/create'.format(put_under, entity), 'resource': Create(), 'method': 'post'}
        )
        if settings.COLLECT_ENTITIES:
            permissions.append('create')


    methods = []
    if has_info:
        methods.append('get')
        if settings.COLLECT_ENTITIES:
            permissions.append('show')

    if has_modify:
        methods.append('patch')
        if settings.COLLECT_ENTITIES:
            permissions.append('patch')

    if has_delete:
        methods.append('delete')
        if settings.COLLECT_ENTITIES:
            permissions.append('delete')

    if has_info or has_modify or has_delete:
        end_points.append({
            'path': '{}/{}/{{{}}}'.format(put_under, entity, id_field)
                    if isinstance(id_field, str) else '{}/{}/'.format(put_under, entity) + '/'.join(
                        ['{{{}}}'.format(fld) for fld in id_field]
                    ),
            'resource': Resource(has_info, has_modify, has_delete),
            'methods': methods
        })

    if has_list:
        end_points.append({
            'path': '{}/{}{}'.format(put_under, entity, list_suffix), 'resource': List(), 'method': 'get'
        })
        if settings.COLLECT_ENTITIES:
            permissions.append('list')

    if settings.COLLECT_ENTITIES:
        add_entity(
            module, id_field, '{}/{}'.format(put_under, entity) if put_under else '/{}'.format(entity), permissions
        )

    return end_points

def gep_list(module, entity, id_field, put_under='',):
    return gep(module=module, entity=entity, id_field=id_field, put_under=put_under,
            has_create=False, has_info=False, has_modify=False, has_delete=False, has_list=True, list_suffix='/list',
            permissions=None
    )

def add_entity(module, id_field, path, permissions):
    entity = None
    from api_gsim import BaseModel
    for attr_name, attr in module.__dict__.items():
        if issubclass(attr,BaseModel) and attr_name != 'BaseModel':
            #if attr_name.lower() == '{}model'.format(module.__name__.rsplit('.', 1)[1].replace('_', '')):
                entity = attr
                break

    settings.entities.append(dict(
        model=entity,
        id_field=id_field,
        name=entity.get_name(),
        path=path,
        permissions=permissions
    ))
