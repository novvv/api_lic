from . base_model import (
    BaseModel, RestoreExceptionToRevisionWhereWasDeleted, RestoreExceptionToCurrentRevision
)
from . object_revision import object_revision, object_revision_record


BaseModel.object_revision_module = object_revision
BaseModel.object_revision_record_module = object_revision_record
