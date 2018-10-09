import json
import falcon
from falcon_rest.conf import settings
#from .. import settings
from falcon_rest.logger import log
from falcon_rest.resources import BaseResource
from falcon_rest import responses
from falcon_rest.responses import errors
from werkzeug.wrappers import Request
from . import middleware_signals


class Middleware(object):
    app_name = None

    def set_app_name(self, app_name):
        self.app_name = app_name

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def process_request(self, req, resp):
        req.context['app_name'] = self.app_name
        middleware_signals.process_request_start.send(self, req=req, resp=resp)

        if settings.ALLOW_ORIGINS and req.headers.get('ORIGIN') in settings.ALLOW_ORIGINS:  # pragma: no cover
            resp.append_header('Access-Control-Allow-Origin', req.headers['ORIGIN'])
            resp.append_header('Access-Control-Allow-Headers', 'Authorization, Content-Type, X-Auth-Token')
            resp.append_header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE')

        req.data = {}

        if not req.content_type or 'application/json' in req.content_type:
            body = req.stream.read()
            if body:
                try:
                    req.data = json.loads(body.decode('utf-8'))
                except (ValueError, UnicodeDecodeError) as e:
                    resource = BaseResource()
                    resource.set_response(
                        resp,
                        responses.MalformedJsonResponse(
                            data=responses.errors.CommonErrors.MalformedJson.set_message(str(e))
                        )
                    )

                    raise falcon.HTTPError(falcon.HTTP_753)

        elif 'multipart/form-data' in req.content_type:
            werkzeug_req = Request(req.env)
            req.data = {k: v for k, v in werkzeug_req.form.items()}
            req.files = werkzeug_req.files

        log_msg = '{} {} from {} ({}), data: {}'.format(req.method, req.path, req.user_agent, req.remote_addr, req.data)

        if hasattr(req, 'files'):
            log_msg += ', FILES: {}'.format(dict(req.files))

        log.debug(log_msg)

        middleware_signals.process_request_end.send(self, req=req, resp=resp)

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def process_resource(self, req, resp, resource, params):
        middleware_signals.process_resource_start.send(self, req=req, resp=resp, resource=resource, params=params)
        self.check_token(req, resp, resource, params)
        middleware_signals.process_resource_end.send(self, req=req, resp=resp, resource=resource, params=params)

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def process_response(self, req, resp, resource, req_succeeded):
        middleware_signals.process_response_start.send(
            self, req=req, resp=resp, resource=resource, req_succeeded=req_succeeded
        )

        log_body = '<cut>' if 'swagger.' in req.path else resp.body
        log.debug('Responding with {}: {}'.format(resp.status, log_body))
        middleware_signals.process_response_end.send(
            self, req=req, resp=resp, resource=resource, req_succeeded=req_succeeded
        )

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def check_token(self, req, resp, resource, params):
        if getattr(resource, 'no_auth_needed', False):
            return True

        if req.path not in settings.PATHS_NOT_NEEDED_AUTH and req.method != 'OPTIONS':
            resource = BaseResource()
            resource.init_req(req)

            token = req.headers.get('X-AUTH-TOKEN')
            if not token:
                from urllib.parse import parse_qsl
                qs = dict(parse_qsl(req.query_string))
                token = qs.get('auth_token')
            if not token:
                resource.set_response(
                    resp, responses.UnauthenticatedErrorResponse(data=errors.AuthErrors.AuthTokenNotProvided)
                )
                raise falcon.HTTPUnauthorized()
            else:

                user = settings.get_auth_module().auth.get_user_from_token(token)
                if user:
                    req.context['user'] = user

                elif user is None:
                    resource.set_response(
                        resp, responses.UnauthenticatedErrorResponse(data=errors.AuthErrors.IncorrectTokenProvided)
                    )
                    middleware_signals.token_incorrect.send(self, req=req, resp=resp)
                    raise falcon.HTTPUnauthorized()
                elif user is False:
                    resource.set_response(
                        resp, responses.UnauthenticatedErrorResponse(data=errors.AuthErrors.TokenExpired)
                    )
                    middleware_signals.token_expired.send(
                        self, req=req, resp=resp,
                        token_data=settings.get_auth_module().auth.decode_without_verification(token)
                    )
                    raise falcon.HTTPUnauthorized()

                return True
        else:
            return True
