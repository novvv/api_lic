from falcon_rest.db import Column, fields, orm
from falcon_rest import schemes, swagger
from falcon_rest.resources.resources import List, BaseResource, check_permission, DEFAULT_SECURITY
from falcon_rest import responses
from falcon_rest.responses import errors
from .. import BaseModel, RestoreExceptionToRevisionWhereWasDeleted, RestoreExceptionToCurrentRevision
from . object_revision_record import ObjectRevisionRecordModel, ObjectRevisionRecordSchemeGet
from falcon_rest.conf import settings


class ObjectRevisionModel(BaseModel):
    use_history = False

    __tablename__ = 'object_revision'

    id = Column(fields.BigInteger().with_variant(fields.Integer, "sqlite"), primary_key=True)
    user_id = Column(fields.String(36), index=True, nullable=False)
    entity_name = Column(fields.String(64), index=True, nullable=False)
    entity_pk = Column(fields.String(64), index=True, nullable=False)
    action = Column(fields.String(16), index=True, nullable=False, default='create')
    revision_number = Column(fields.Integer, index=True, nullable=False)
    revision_time = Column(fields.DateTime(timezone=True), default=orm.func.now(), nullable=False)
    restored_from_revision_id = Column(fields.BigInteger().with_variant(fields.Integer, "sqlite"), nullable=True)

    changes = orm.relationship(ObjectRevisionRecordModel)

    def restore(self, user):
        for entity in settings.entities:
            if entity['name'] == self.entity_name:
                return entity['model'].restore(self, user)


class ObjectRevisionSchemeGet(schemes.BaseModelScheme):
    changes = schemes.fields.List(schemes.fields.Nested(ObjectRevisionRecordSchemeGet))
    action = schemes.fields.String(
        validate=schemes.validate.OneOf(choices=('create', 'update', 'delete', 'restore'))
    )

    class Meta:
        model = ObjectRevisionModel
        search_fields = ('user_id', 'entity_name', 'entity_pk', 'action', 'revision_number')


List = List.create(ObjectRevisionModel, ObjectRevisionSchemeGet, 'Object revisions')


CantRestoreToDeleted = errors.Error(
    1110, 'You can\'t restore object to revision where it was deleted', 'cant_restore_to_deleted'
)


CantRestoreToCurrentRevision = errors.Error(
    1120, 'You can\'t restore object to the last revision', 'cant_restore_to_the_last_revision'
)


class RestoreObject(BaseResource):
    allow_methods = ['post']

    def __init__(self, **kwargs):
        super(RestoreObject, self).__init__()
        self.security = kwargs.get('security', DEFAULT_SECURITY)

    def on_post(self, req, resp, **kwargs):
        obj = self.get_object(resp, ObjectRevisionModel, **kwargs)
        user = self.get_user(req)
        if not check_permission('ObjectRevision', req, 'restore', obj) or (
            hasattr(user, 'can_restore') and not user.can_restore(obj)
        ):
            self.set_response(
                resp, responses.ForbiddenErrorResponse(data=errors.AuthErrors.Forbidden)
            )
            return

        try:
            if obj.restore(self.get_user(req)):
                self.set_response(resp, responses.SuccessResponseJustOk())
        except RestoreExceptionToRevisionWhereWasDeleted:
            self.set_response(resp, responses.OperationErrorResponse(data=CantRestoreToDeleted))
        except RestoreExceptionToCurrentRevision:
            self.set_response(resp, responses.OperationErrorResponse(data=CantRestoreToCurrentRevision))

    def get_spec(self):
        return swagger.specify.get_spec(
            method='post', description='Restores object to the specified revision',
            path_parameters=({'name': 'id', 'description': 'ID of revision to restore to'}, ),
            responses=(
                responses.SuccessResponseJustOk(),
                responses.ObjectNotFoundErrorResponse()
            ),
            security=self.security
        )
