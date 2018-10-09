from falcon_rest.contrib.rbac import RbacRole,RbacUser,RbacRoleNoRole


class AdminRole(RbacRole):
    @classmethod
    def get_name(cls):
        return 'admin'


class UserRole(RbacRole):
    @classmethod
    def get_name(cls):
        return 'user'

class CompanyAdminRole(RbacRole):
    @classmethod
    def get_name(cls):
        return 'company_admin'

class ResellerRole(RbacRole):
    @classmethod
    def get_name(cls):
        return 'reseller'