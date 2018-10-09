from falcon_rest import schemes


class CredentialsScheme(schemes.Schema):
    email = schemes.fields.String(required=True)
    password = schemes.fields.String(required=True)


class AuthTokenSchemeInner(schemes.Schema):
    token = schemes.fields.String(dump_only=True)
    exp = schemes.fields.DateTime(dump_only=True)
    user_type = schemes.fields.String(dump_only=True)

class AuthTokenScheme(schemes.SuccessScheme):
    payload = schemes.fields.Nested(AuthTokenSchemeInner())

class AuthTokenExtScheme(schemes.SuccessScheme):
    payload = schemes.fields.Nested(AuthTokenSchemeInner())

class PasswordCheckScheme(schemes.Schema):
    password = schemes.fields.String(required=True)


class TokenCheckScheme(schemes.Schema):
    token = schemes.fields.String(required=True)
    exp = schemes.fields.DateTime(dump_only=True)


class UserCredentialsScheme(schemes.Schema):
    email = schemes.fields.String(required=True)
    password = schemes.fields.String(required=True)