
from falcon_rest.conf import settings
from falcon_rest.resources import BaseResource, resources
from falcon_rest import schemes, responses
from falcon_rest.swagger import specify
from . import auth, auth_schemes
from . auth_signals import auth_success, auth_failed
from . auth_schemes import UserCredentialsScheme,AuthTokenExtScheme,AuthTokenSchemeInner

class Auth(BaseResource):
    allow_methods = ['put']
    def __init__(self, **kwargs):
        super(Auth, self).__init__()
        self.credentials_scheme_class = UserCredentialsScheme  #kwargs.get('credentials_scheme_class', auth_schemes.CredentialsScheme)
        self.security = kwargs.get('security', ['api_auth'])

    def on_post(self, req, resp, **kwargs):
        credentials_scheme = self.credentials_scheme_class()
        if self.check_request_data(req, resp, credentials_scheme):
            credentials = self.get_loaded_data(credentials_scheme)
            user = settings.get_auth_user_model(req=req).get_user_from_credentials(credentials)
            if user and auth.check_password(credentials['password'], user.password):
                if not hasattr(user, 'can_login') or user.can_login(req, resp):
                    token = auth.get_token(user)
                    exp = auth.get_token_exp(token)
                    user_type = user.user_type()
                    self.set_response(
                        resp, responses.SuccessResponse(
                            scheme=AuthTokenExtScheme, data={'token': token,'exp':exp ,'user_type':user_type}
                        )
                    )
                    auth_success.send(self, req=req, resp=resp, user=user)
                else:
                    auth_failed.send(self, req=req, resp=resp, data=credentials, user=user)
                    #self.set_response(resp, responses.UnAuthorizedErrorResponse())
            else:
                auth_failed.send(self, req=req, resp=resp, data=credentials, user=user)
                self.set_response(resp, responses.UnAuthorizedErrorResponse())

    def get_spec(self):
        return specify.get_spec(
            method='post', description='Authenticate',
            body_parameters=('Credentials', self.credentials_scheme_class),
            responses=(
                responses.SuccessResponse(scheme=AuthTokenExtScheme),
                responses.ValidationErrorResponse(),
                responses.UnAuthorizedErrorResponse(),
                responses.ObjectNotFoundErrorResponse()
            ),
            security=self.security
        )
### auth

class PasswordCheck(BaseResource):
    allow_methods = ['post']

    def __init__(self, **kwargs):
        super(PasswordCheck, self).__init__()
        self.security = kwargs.get('security', resources.DEFAULT_SECURITY)

    def on_post(self, req, resp, **kwargs):
        password_scheme = auth_schemes.PasswordCheckScheme()

        if self.check_request_data(req, resp, password_scheme):
            data = self.get_loaded_data(password_scheme)
            if auth.check_password(data['password'], self.get_user(req).password):
                self.set_response(resp, responses.SuccessResponse(scheme=schemes.SuccessScheme))
            else:
                self.set_response(resp, responses.OperationErrorResponse(data=responses.errors.UserErrors.IncorrectPassword))

    def get_spec(self):
        return specify.get_spec(
            method='post', description='Checks current user password',
            body_parameters=('User password', auth_schemes.PasswordCheckScheme),
            responses=(
                responses.SuccessResponseJustOk(),
                responses.ValidationErrorResponse(),
                responses.OperationErrorResponse('Incorrect password')
            ),
            security=self.security
        )


class TokenCheck(BaseResource):
    allow_methods = ['post']

    def __init__(self, **kwargs):
        super(TokenCheck, self).__init__()
        self.security = kwargs.get('security', resources.DEFAULT_SECURITY)

    def on_post(self, req, resp, **kwargs):
        self.init_req(req)
        token = auth.get_token(self.get_user(req))
        exp = auth.get_token_exp(token)
        self.set_response(
            resp, responses.SuccessResponse(
                scheme=auth_schemes.AuthTokenExtScheme, data={'token': token,'exp':exp}
            )
        )

    def get_spec(self):
        return specify.get_spec(
            method='post', description='Checks and refreshes token',
            responses=(
                responses.SuccessResponse(scheme=auth_schemes.AuthTokenExtScheme),
                responses.ValidationErrorResponse(),
                responses.OperationErrorResponse('Incorrect token')
            ),
            security=self.security
        )
