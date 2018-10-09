from falcon_rest.signals import Signal


class AuthSuccess(Signal):
    pass


class AuthFailed(Signal):
    pass


auth_success = AuthSuccess()
auth_failed = AuthFailed()
