class RbacUser(object):
    def get_role(self):
        """
        Returns role to store in token
        Example:
            return AdminRole if self.is_admin else UserRole

        :return: RbacRole
        """
        raise NotImplementedError('Method "get_role" must be implemented in any derived class')

    def rbac_hash(self):
        return self.get_role()
