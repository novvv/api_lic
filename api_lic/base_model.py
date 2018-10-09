from .objects_history import BaseModel
#import api_dnl
#import falcon_rest
from falcon_rest.db import get_db#,BaseModel
from sqlalchemy.sql import func
from sqlalchemy import func, distinct,inspect
from sqlalchemy.orm import lazyload
from sqlalchemy.dialects import postgresql
from falcon_rest.logger import log

import json

class BaseModel(BaseModel):
    __abstract__ = True
    #db_label = 'lic'

    def __repr__(self):
        # return 'obj'
        parts = []
        for column_name in inspect(self.__class__).columns.keys():
            parts.append('{} = {}'.format(column_name, getattr(self, column_name)))
        return '<{}: {}>'.format(self.__class__.__name__, ', '.join(parts))

    def as_dict(self):
        return object_to_dict(self)

    @classmethod
    def session(cls):
        return get_db(cls.db_label).session

    @classmethod
    def get_objects_list(cls, query=None, filtering=None, paging=None,
                         ordering=None):
        from sqlalchemy import alias, cast, String
        qs = query or cls.query()

        if filtering:
            for k, v in filtering.items():
                if type(v)==type('') and '*' in v:  # pragma: no cover
                    v = v.upper()
                    qs = qs.filter(func.upper(cast(getattr(cls, k), String)).like(v.replace('*', '%')))
                else:
                    qs = qs.filter(getattr(cls, k) == v)

        if ordering:  # pragma: no cover
            order_by = getattr(cls, ordering['by'])
            if ordering['dir'] == 'desc':
                order_by = order_by.desc().nullslast()

            qs = qs.order_by(order_by)

        try:
            cnt = get_count(qs)
        except Exception as e:
            cnt = len(qs.all())

        if paging:
            if 'from' in paging:
                qs = qs.offset(paging['from'])
            if 'till' in paging:
                qs = qs.limit(paging['till'] - paging.get('from', 0))
        try:
            log.debug(_q_str(qs))
        except:
            log.debug(str(qs))
        return qs.all(), cnt

    @classmethod
    def get_objects_query_list(cls, query=None, filtering=None, paging=None,
                         ordering=None):
        from sqlalchemy import alias,cast,String
        qs = query or cls.query()
        if hasattr(cls,'_tab'):
            tab = cls._tab
        else:
            tab = alias(qs,cls.__tablename__)
        if filtering:
            for k, v in filtering.items():

                if type(v)==type('') and '*' in v:  # pragma: no cover
                    v = v.upper()
                    qs = qs.filter(func.upper(cast(getattr(tab.c, k),String)).like(v.replace('*', '%')))
                else:
                    qs = qs.filter(getattr(tab.c, k) == v)

        if ordering:  # pragma: no cover
            order_by = getattr(tab.c, ordering['by'])
            if ordering['dir'] == 'desc':
                order_by = order_by.desc().nullslast()

            qs = qs.order_by(order_by)

        try:
            cnt = get_count(qs)#cnt = qs.count()
        except Exception as e:
            cnt = len(qs.all())

        if paging:
            if 'from' in paging:
                qs = qs.offset(paging['from'])
            if 'till' in paging:
                qs = qs.limit(paging['till'] - paging.get('from', 0))
        try:
            log.debug(_q_str(qs))
        except:
            log.debug(str(qs))
        return qs.all(), cnt

def _q_str(q):
    return str(q.statement.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))
def object_to_dict(obj, found=None, deep=False):
    from datetime import datetime
    from sqlalchemy.orm import class_mapper
    if found is None:
        found = set()
    mapper = class_mapper(obj.__class__)
    columns = [column.key for column in mapper.columns if hasattr(obj,column.key)]
    get_key_value = lambda c: (c, getattr(obj, c).isoformat()) if isinstance(getattr(obj, c), datetime) else (c, getattr(obj, c))
    out = dict(map(get_key_value, columns))
    if deep:
        for name, relation in mapper.relationships.items():
            if relation not in found:
                found.add(relation)
                related_obj = getattr(obj, name)
                if related_obj is not None:
                    if relation.uselist:
                        out[name] = [object_to_dict(child, found,deep) for child in related_obj]
                    else:
                        out[name] = object_to_dict(related_obj, found,deep)
    return out

def get_count(q):
	disable_group_by = False
	if len(q._entities) > 1:
		# currently support only one entity
		raise Exception('only one entity is supported for get_count, got: %s' % q)
	entity = q._entities[0]
	if hasattr(entity, 'column'):
		# _ColumnEntity has column attr - on case: query(Model.column)...
		col = entity.column
		if q._group_by and q._distinct:
			# which query can have both?
			raise NotImplementedError
		if q._group_by or q._distinct:
			col = distinct(col)
		if q._group_by:
			# need to disable group_by and enable distinct - we can do this because we have only 1 entity
			disable_group_by = True
		count_func = func.count(col)
	else:
		# _MapperEntity doesn't have column attr - on case: query(Model)...
		count_func = func.count()
	if q._group_by and not disable_group_by:
		count_func = count_func.over(None)
	count_q = q.options(lazyload('*')).statement.with_only_columns([count_func]).order_by(None)
	if disable_group_by:
		count_q = count_q.group_by(None)
	return q.session.execute(count_q).scalar()

