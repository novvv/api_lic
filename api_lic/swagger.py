import sys
from falcon_rest.swagger import init
from falcon_rest.conf import settings
from falcon_rest.schemes.schemes import ObjectCreatedCompositeOrStrPk, ObjectCreatedUuidAsPk, ForbiddenError
from .routes import ROUTES
from falcon_rest.db import initialize_db
from .base_model import BaseModel
from . import scheme
from falcon_rest import schemes


def init_swagger():
    from .rbac import rbac_acl
    from . import file
    from .auth import auth_schemes
    for name, cls in scheme.__dict__.items():
        if isinstance(cls, schemes.BaseModelScheme):
            for name, field in cls._declared_fields:
                if hasattr(field, 'attribute'):
                    name = field.attribute
                field._add_to_schema(name, cls)
    from falcon_rest.contrib.files import files_register
    from .model import User
    files_register.base_model = BaseModel
    files_register.register_file_field(User, 'logo_file_uuid')

    swagger = init(
        ROUTES, [
            # 'api_dnl.entities',
            'api_lic.scheme', 'api_lic.auth',
            'falcon_rest.contrib.objects_history.object_revision'
        ],
        [auth_schemes.AuthTokenSchemeInner, auth_schemes.AuthTokenScheme, ObjectCreatedCompositeOrStrPk, ForbiddenError,
         ObjectCreatedUuidAsPk, file.FileSchemeDownloadLinkResp, file.FileModel.tmp_file_scheme]
    )

    # swagger.add_oauth2_security_definition(
    #    'api_auth', '{}{}{}{}'.format(
    #        settings.API_SCHEME, settings.API_HOST, settings.API_BASE_PATH, settings.AUTH_END_POINT
    #    )
    # )
    swagger.add_api_key_security_definition('auth_token')

    return swagger


def main(args):
    initialize_db(settings.DB_CONN_STRING, BaseModel)

    if len(args) > 1 and args[1] == 'yaml':
        return init_swagger().get_yaml()
    else:
        return init_swagger().get_json()


if __name__ == '__main__':
    print(main(sys.argv))
