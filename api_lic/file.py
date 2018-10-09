from falcon_rest import schemes
from falcon_rest.contrib import files
from falcon_rest.contrib.files import register,create_scheme, \
    ModelUsingFiles as _ModelUsingFiles,create_file_model_class
from falcon_rest.contrib.files.endpoints import UploadFile, GetDownloadLink, \
    DownloadFile, ShowFile
from falcon_rest.db import Column, fields, orm, get_db

from falcon_rest.resources import resources

from sqlalchemy import Column

from .base_model import BaseModel

FileModel = create_file_model_class('file', BaseModel)

FileScheme = create_scheme(FileModel, name='FileScheme',
                           **dict(meta=dict(fields=(),search_fields=('belongs_to_table','belongs_to_field','uuid','public'))))


FileSchemeShort = create_scheme(
    FileModel, name='FileSchemeShort',
    **dict(meta=dict(fields=('uuid', 'attached_on', 'uploaded_on')))
)


FileSchemeDownloadLinkReq = create_scheme(
    FileModel, name='FileSchemeDownloadLinkReq',
    **dict(meta=dict(fields=('uuid', 'belongs_to_pk')))
)


class FileSchemeDownloadLinkResp(schemes.BaseModelScheme):
    download_link = schemes.fields.String(required=True)


file_upload = UploadFile(FileScheme)


class FileDownloadTokenModel(BaseModel):
    __tablename__ = 'file_download_token'

    id = Column(fields.Integer, primary_key=True)
    file_uuid = Column(fields.String(36), unique=True)
    token = Column(fields.String(1024))


get_download_link = GetDownloadLink(
    FileSchemeDownloadLinkReq, FileSchemeDownloadLinkResp,
    FileDownloadTokenModel,
    belongs_to_pk_field_name='belongs_to_uuid',
    path_parameters=(
        dict(name='belongs_to_uuid', type='string',
             description='UUID of entity file belongs to'),
        dict(name='uuid', type='string', description='File UUID'),
    )
)


file_download = DownloadFile(FileDownloadTokenModel, FileModel)


file_show = ShowFile(
    FileModel, path_parameters=(dict(
        name='file_uuid', type='string', description='UUID of file to show'),
    )
)


ListTmpFiles = resources.List.create(
    FileModel.tmp_model_class, FileModel.tmp_file_scheme, 'Tmp files')


ListFiles = resources.List.create(FileModel, FileScheme, 'Files')

class ModelUsingFiles(_ModelUsingFiles):
    def before_save(self):
        # noinspection PyAttributeOutsideInit
        self.autocommit = False
        self.query().session.autoflush = False
        file_fields_values = self.get_file_fields_values()
        tmp_files_to_move = {}
        # files_in
        for k, v in file_fields_values.items():
            if self.file_fields_values_before_save.get(k) != v:
                field = self.get_field(k)
                try:
                    if field.file_model_class.get(v) is None:
                        tmp_files_to_move[k] = v
                except Exception as e:
                    pass
        try:
            self.move_tmp_files(tmp_files_to_move)
        except Exception as e:
            pass

        # self.delete()

    def after_save(self):
        # noinspection PyUnresolvedReferences
        for k, v in self.get_file_fields_values().items():
            if not v is None:
                if self.get_field(k).file_model_class.get(v).belongs_to_pk is None:
                    self.get_field(k).file_model_class.get(v).belongs_to_pk = self.get_object_primary_key_value()
        self.query().session.autoflush = True
        self.commit()

    def move_tmp_files(self, tmp_files_to_move):
        files=[]
        for field_name, file_uuid in tmp_files_to_move.items():
            file_model_class = self.get_field(field_name).file_model_class
            tmp_file = file_model_class.tmp_model_class.get(file_uuid)

            if not tmp_file:
                raise schemes.fields.ValidationError(
                    {field_name: 'File with UUID {input} does not exist'.format(input=file_uuid)}
                )

            f = file_model_class(
                uuid=tmp_file.uuid,
                path=tmp_file.path,
                belongs_to_table=tmp_file.belongs_to_table,
                belongs_to_field=tmp_file.belongs_to_field,
                belongs_to_pk=self.get_object_primary_key_value(),
                uploaded_on=tmp_file.uploaded_on,
                public=tmp_file.public
            )
            #files.append(tmp_file)
            get_db(f.db_label).session.add(f)
            get_db(f.db_label).session.delete(tmp_file)


def relationship(
        file_model_class, model_class_tablename, file_column_name, model_class_name=None, relation_column_name=None
):
    if not model_class_name:
        model_class_name = '{}'.format(''.join([item.title() for item in model_class_tablename.split('_')]))

    file_model_class_name = file_model_class.__name__

    if not relation_column_name:
        relation_column_name = file_column_name.replace('_file_uuid', '')

    join_condition_str = ', '.join([
        'and_({model_class_name}.{file_column_name} == {file_model_class_name}.uuid',
        '{file_model_class_name}.belongs_to_table == "{model_class_tablename}"',
        '{file_model_class_name}.belongs_to_field == "{relation_column_name}")'
    ])
    join_condition_params = dict(
        model_class_name=model_class_name, file_column_name=file_column_name,
        model_class_tablename=model_class_tablename, file_model_class_name=file_model_class_name,
        relation_column_name=relation_column_name
    )

    return orm.relationship(file_model_class, primaryjoin=join_condition_str.format(**join_condition_params))

