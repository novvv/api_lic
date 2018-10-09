from falcon_rest.db.base_model_class import BaseModelClass
from falcon_rest.db import get_db


class RestoreExceptionToRevisionWhereWasDeleted(Exception):
    pass


class RestoreExceptionToCurrentRevision(Exception):
    pass


class _BaseModelWithHistoryClass(BaseModelClass):
    use_history = True

    previous_data = None

    object_revision_module = None
    object_revision_record_module = None

    def save(self, **kwargs):
        result = super(_BaseModelWithHistoryClass, self).save(**kwargs)
        if result and kwargs.get('save_history', False):
            self.add_history_record_on_create_or_update(**kwargs)
        return result

    def get_current_revision_number(self):
        return self.object_revision_module.ObjectRevisionModel.filter(
            self.object_revision_module.ObjectRevisionModel.entity_name == self.get_name(),
            self.object_revision_module.ObjectRevisionModel.entity_pk == str(self.get_object_primary_key_value())
        ).count()

    def get_next_revision_number(self):
        return self.get_current_revision_number() + 1

    def get_action_create_or_update(self, next_revision_number, entity_name, entity_pk):
        if next_revision_number == 1:
            return 'create'

        previous_revision = self.object_revision_module.ObjectRevisionModel.filter(
            entity_name=entity_name, entity_pk=entity_pk
        ).order_by(self.object_revision_module.ObjectRevisionModel.revision_number.desc()).first()

        if previous_revision.action == 'delete':
            return 'create'

        return 'update'

    def add_history_record_on_create_or_update(self, **kwargs):
        if 'user' not in kwargs:  # pragma: no cover
            raise Exception(
                'No user passed to object save method while use_history == True and save_history=True passed'
            )

        entity_name = self.get_name()
        entity_pk = str(self.get_object_primary_key_value())

        revision_number = self.get_next_revision_number()

        action = self.get_action_create_or_update(revision_number, entity_name, entity_pk)

        revision_obj_id = self.object_revision_module.ObjectRevisionModel(
            user_id=kwargs['user'].get_id(),
            entity_name=entity_name,
            entity_pk=entity_pk,
            action=action,
            revision_number=revision_number
        ).save()

        if action == 'create' or not self.previous_data:
            for field_name, value in self.get_current_data().items():
                self.object_revision_module.ObjectRevisionRecordModel(
                    object_revision_id=revision_obj_id,
                    field_name=field_name,
                    old_value=None,
                    new_value=value
                ).save()
        else:
            for field_name, values in self.get_diff().items():
                self.object_revision_module.ObjectRevisionRecordModel(
                    object_revision_id=revision_obj_id,
                    field_name=field_name,
                    old_value=values[0],
                    new_value=values[1]
                ).save()

        get_db(self.db_label).commit()

    @classmethod
    def restore(cls, object_revision, user):
        if object_revision.action == 'delete':
            raise RestoreExceptionToRevisionWhereWasDeleted()

        if not cls.object_revision_module.ObjectRevisionModel.filter(
            cls.object_revision_module.ObjectRevisionModel.entity_name == object_revision.entity_name,
            cls.object_revision_module.ObjectRevisionModel.entity_pk == object_revision.entity_pk,
            cls.object_revision_module.ObjectRevisionModel.revision_number > object_revision.revision_number
        ).count():
            raise RestoreExceptionToCurrentRevision()

        revisions_list = cls.object_revision_module.ObjectRevisionModel.filter(
            cls.object_revision_module.ObjectRevisionModel.entity_name == object_revision.entity_name,
            cls.object_revision_module.ObjectRevisionModel.entity_pk == object_revision.entity_pk,
            cls.object_revision_module.ObjectRevisionModel.revision_number <= object_revision.revision_number
        ).order_by(cls.object_revision_module.ObjectRevisionModel.revision_number.desc())

        needed_revisions_list = []
        for revision in revisions_list.all():
            needed_revisions_list.append(revision)
            if revision.action in ['create', 'restore']:
                break

        fields_values = {}
        for revision in reversed(needed_revisions_list):
            for change in revision.changes:
                column = cls.__table__.columns[change.field_name]
                if str(column.type) in ['DATETIME', 'DATE', 'TIME'] and column.server_default:
                    continue
                fields_values[change.field_name] = change.new_value

        obj = cls.query().get(*tuple(object_revision.entity_pk.strip('()').split(',')))
        current_data = obj.get_current_data()

        for field_name, field_value in fields_values.items():
            setattr(obj, field_name, cls.restore_value(field_value))

        if obj.save():
            revision_obj_id = cls.object_revision_module.ObjectRevisionModel(
                user_id=user.get_id(),
                entity_name=obj.get_name(),
                entity_pk=str(obj.get_object_primary_key_value()),
                action='restore',
                restored_from_revision_id=object_revision.id,
                revision_number=obj.get_next_revision_number()
            ).save()
            for field_name in fields_values.keys():
                cls.object_revision_module.ObjectRevisionRecordModel(
                    object_revision_id=revision_obj_id,
                    field_name=field_name,
                    old_value=current_data[field_name],
                    new_value=fields_values[field_name]
                ).save()
            return True

    def delete(self, **kwargs):
        result = super(_BaseModelWithHistoryClass, self).delete(**kwargs)
        if result and kwargs.get('save_history', False):
            self.object_revision_module.ObjectRevisionModel(
                user_id=kwargs['user'].get_id(),
                entity_name=self.get_name(),
                entity_pk=str(self.get_object_primary_key_value()),
                action='delete',
                revision_number=self.get_next_revision_number()
            ).save()
        return result

    @classmethod
    def get_object_by_primary_key(cls, **kwargs):
        obj = super(_BaseModelWithHistoryClass, cls).get_object_by_primary_key(**kwargs)
        if cls.use_history:
            obj.store_previous_data()
        return obj

    @classmethod
    def get_object_by_id(cls, id_value, **kwargs):
        obj = super(_BaseModelWithHistoryClass, cls).get_object_by_id(id_value)
        if cls.use_history:
            obj.store_previous_data()
        return obj

    def store_previous_data(self):
        self.previous_data = self.get_current_data()

    def get_diff(self):
        if not self.use_history:
            raise NotImplementedError('This object does not use history (i.e. use_history = False)')

        diff = dict()
        for k, v in self.previous_data.items():
            current_value = self.get_value(getattr(self, k))
            if v != current_value:
                diff[k] = [self.get_value(v), current_value]

        return diff

    @staticmethod
    def get_value(value):
        if isinstance(value, bool):
            return 'True' if value else 'False'
        elif value is None:
            return None
        else:
            return str(value)

    @staticmethod
    def restore_value(value):
        if value == 'True':
            return True
        elif value == 'False':
            return False
        else:
            return value

    def get_current_data(self):
        current_data = dict()
        for field_name in self.get_fields():
            current_data[field_name] = self.get_value(getattr(self, field_name))

        return current_data
