from falcon_rest.db import Column, fields
from falcon_rest import schemes
from .. import BaseModel


class ObjectRevisionRecordModel(BaseModel):
    use_history = False

    __tablename__ = 'object_revision_record'

    id = Column(fields.BigInteger().with_variant(fields.Integer, "sqlite"), primary_key=True)
    object_revision_id = Column(fields.ForeignKey('object_revision.id', ondelete='CASCADE'), nullable=False)
    field_name = Column(fields.String(64), nullable=False)
    old_value = Column(fields.Text, nullable=True)
    new_value = Column(fields.Text, nullable=True)


class ObjectRevisionRecordSchemeGet(schemes.BaseModelScheme):
    class Meta:
        model = ObjectRevisionRecordModel
        exclude = ('id',)
