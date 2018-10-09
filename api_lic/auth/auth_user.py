class AuthUser(object):
    @classmethod
    def get_user_from_credentials(cls, credentials):
        """
        Returns user from DB or None if user not found
        Example:
            try:
                return cls.filter(cls.username == credentials['username']).one()
            except errors.NoResultFound:
                return None
        :param credentials: dict
        :return: User or None
        """
        raise NotImplementedError('Method "get_user_from_credentials" must be implemented in any derived class')

    def get_token_data(self):
        """
        Returns data to store in token
        Example:
            return dict(user_id=self.user_id)

        :return: dict
        """
        raise NotImplementedError('Method "get_token_data" must be implemented in any derived class')

    @classmethod
    def get_user_from_token_data(cls, token_data):
        """
        Returns user object from token_data
        Example:
            return cls.filter(user_id=token_data['user_id']).one()

        :param token_data: dict
        :return: User
        """
        raise NotImplementedError('Method "get_user_from_token_data" must be implemented in any derived class')

    def can_login(self, req, resp):
        return True
