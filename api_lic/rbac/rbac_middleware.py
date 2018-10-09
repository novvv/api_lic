import falcon
from ..middleware import middleware
from falcon_rest import responses


class RbacMiddleware(middleware.Middleware):
    def check_token(self, req, resp, resource, params):
        if super(RbacMiddleware, self).check_token(req, resp, resource, params) and req.method != 'OPTIONS':
            if hasattr(resource, 'acl'):
                perm = resource.acl.is_allowed(resource, req.method.lower(), req.context.get('user'))

                if not perm.check():
                    resource.set_response(
                        resp, responses.ForbiddenErrorResponse()
                    )
                    raise falcon.HTTPUnauthorized()
                else:
                    return True
