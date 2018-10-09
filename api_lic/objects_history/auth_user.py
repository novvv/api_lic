from falcon_rest.contrib.auth.auth_user import AuthUser as AuthUserBase


# noinspection PyClassHasNoInit,PyAbstractClass
class AuthUser(AuthUserBase):
    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def can_restore(self, object_revision):
        raise NotImplementedError('Method "can_restore" must be implemented in any derived class')

    def get_id(self):
        raise NotImplementedError('Method "get_id" must be implemented in any derived class')
