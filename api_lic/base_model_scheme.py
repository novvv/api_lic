#
from marshmallow_sqlalchemy import convert,ModelSchemaOpts
from falcon_rest.schemes import ObjectCreatedUuidAsPk, ObjectCreatedCompositeOrStrPk,BaseModelScheme as _BaseModelScheme
from falcon_rest.responses import ObjectCreatedResponse

class MyModelConverter(convert.ModelConverter):
    def _get_field_class_for_property(self, prop):
        if hasattr(prop, 'direction'):
            field_cls = convert.Related
        elif hasattr(prop,'columns'):
            column = prop.columns[0]
            field_cls = self._get_field_class_for_column(column)
        elif hasattr(prop,'_proxied_property'):
            prop1=prop._proxied_property
            if hasattr(prop1, 'direction'):
                field_cls = convert.Related
            elif hasattr(prop1, 'columns'):
                column = prop1.columns[0]
                field_cls = self._get_field_class_for_column(column)
            else:
                raise convert.ModelConversionError('Property and proxy field not found! {}:{}'.format(str(prop),prop.name))
        return field_cls

    def _add_column_kwargs(self, kwargs, column):
        try:
            super(MyModelConverter,self)._add_column_kwargs(kwargs, column)
        except AttributeError as e:
            kwargs['allow_none'] = True
            #raise convert.ModelConversionError('Add column kwargs:! {}:{}:{}'.format(str(column), column.name,str(e)))


class BaseOpts(ModelSchemaOpts):
    def __init__(self, meta):
        super(BaseOpts, self).__init__(meta)
        self.model_converter = getattr(meta, 'model_converter', MyModelConverter)

class BaseModelScheme(_BaseModelScheme):
    OPTIONS_CLASS = BaseOpts
    @classmethod
    def get_object_created_response(cls, **kwargs):
        if 'scheme_class' in kwargs:
            scheme_class = kwargs['scheme_class']
            del kwargs['scheme_class']
        else:
            scheme_class = cls

        pk_field_name = scheme_class.Meta.model.get_model_class_primary_key()
        pk_field = scheme_class.Meta.model.get_field(pk_field_name)
        try:
            pk_type = str(pk_field.type).lower()
        except:
            pk_type = 'unknown'

        if 'int' in pk_type:
            pass
        elif 'varchar' in pk_type:
            if 'uuid' in pk_field_name:
                if 'scheme' not in kwargs:
                    kwargs['scheme'] = ObjectCreatedUuidAsPk
                if 'data_key' not in kwargs:
                    kwargs['data_key'] = 'object_uuid'
            else:
                if 'scheme' not in kwargs:
                    kwargs['scheme'] = ObjectCreatedCompositeOrStrPk
                if 'data_key' not in kwargs:
                    kwargs['data_key'] = 'object_pk'

        return ObjectCreatedResponse(**kwargs)