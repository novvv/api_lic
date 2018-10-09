# noinspection PyProtectedMember,PyUnresolvedReferences
from . base_model_class import (
    _BaseModelWithHistoryClass, RestoreExceptionToRevisionWhereWasDeleted, RestoreExceptionToCurrentRevision
)
# noinspection PyProtectedMember
from falcon_rest.db import _declarative_base


BaseModel = _declarative_base(cls=_BaseModelWithHistoryClass)
