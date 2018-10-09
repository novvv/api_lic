class RbacPermAllow(object):
    @classmethod
    def check(cls):
        return True


class RbacPermDeny(object):
    @classmethod
    def check(cls):
        return False
