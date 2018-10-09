from falcon_rest.schemes import (CHOICES_VALIDATION_ERR_MESSAGE, BaseModelScheme)
#from falcon_rest.db import Column
from falcon_rest.conf import settings
from falcon_rest.contrib.files import create_file_model_class, create_scheme
#from falcon_rest.contrib.files.endpoints import UploadFile, GetDownloadLink, DownloadFile, ShowFile
#from marshmallow_sqlalchemy import field_for, fields as sa

from sqlalchemy import inspect
from marshmallow import (
    Schema, pre_load, pre_dump, post_dump, post_load, validates_schema,
    validate,validates, fields, ValidationError
)
from marshmallow.fields import (
 Field,Raw,Nested, Dict, List, String, UUID, Number, Integer, Decimal, Boolean,
 FormattedString, Float, DateTime, LocalDateTime, Time, Date, TimeDelta, Url, URL,
 Email, Method, Function, Str, Bool, Int, Constant )

def valid_dict(d):
    return validate.OneOf(choices=d.values(),labels=d.keys(),error=CHOICES_VALIDATION_ERR_MESSAGE)

class Choice(String):
    def _get_choices(self,field_name,scheme_class):
        schema=scheme_class
        model = schema.Meta.model
        syns = inspect(model).synonyms
        if field_name in syns:
            field_name = syns[field_name].name
        cols = inspect(model).columns
        if field_name in cols:
            try:
                dic = cols[field_name].type.choices
                choices = tuple(dic.values())
                return choices
                # self.enum = choices
                # self.validate = valid_dict(dic) #validate.OneOf(choices=choices,error=CHOICES_VALIDATION_ERR_MESSAGE)
                self.validate = validate.OneOf(choices=choices, error=CHOICES_VALIDATION_ERR_MESSAGE)
            except Exception as e:
                return {}

    def _add_to_schema(self, field_name, schema):
        try:
            self.parent = self.parent or schema
            self.name = self.name or field_name
            if hasattr(self,'attribute') and self.attribute:
                field_name=self.attribute
            model=schema.Meta.model
            syns=inspect(model).synonyms
            if field_name in syns:
                field_name = syns[field_name].name
            cols=inspect(model).columns
            if field_name in cols:
                try:
                    dic = cols[field_name].type.choices
                    choices=tuple(dic.values() )
                    #self.enum = choices
                    #self.validate = valid_dict(dic) #validate.OneOf(choices=choices,error=CHOICES_VALIDATION_ERR_MESSAGE)
                    self.validate = validate.OneOf(choices=choices,error=CHOICES_VALIDATION_ERR_MESSAGE)
                    self.validators = [self.validate]
                    if not self.default:
                        self.default = choices[0]
                except Exception as e:
                    raise Exception('Schema '+str(schema)+' field '+ field_name+' error:'+str(e))
        except Exception as e:
            raise Exception('Schema model ' + str(schema) + ' field ' + field_name + ' error:' + str(e))


