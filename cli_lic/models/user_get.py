# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserGet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'role_name': 'str',
        'passwd': 'str',
        'is_admin': 'bool',
        'logo_file_uuid': 'str',
        'user_uuid': 'str',
        'created_on': 'datetime',
        'email': 'str',
        'last_login': 'datetime',
        'is_active': 'bool'
    }

    attribute_map = {
        'role_name': 'role_name',
        'passwd': 'passwd',
        'is_admin': 'is_admin',
        'logo_file_uuid': 'logo_file_uuid',
        'user_uuid': 'user_uuid',
        'created_on': 'created_on',
        'email': 'email',
        'last_login': 'last_login',
        'is_active': 'is_active'
    }

    def __init__(self, role_name=None, passwd=None, is_admin=None, logo_file_uuid=None, user_uuid=None, created_on=None, email=None, last_login=None, is_active=None):
        """
        UserGet - a model defined in Swagger
        """

        self._role_name = None
        self._passwd = None
        self._is_admin = None
        self._logo_file_uuid = None
        self._user_uuid = None
        self._created_on = None
        self._email = None
        self._last_login = None
        self._is_active = None

        if role_name is not None:
          self.role_name = role_name
        if passwd is not None:
          self.passwd = passwd
        if is_admin is not None:
          self.is_admin = is_admin
        if logo_file_uuid is not None:
          self.logo_file_uuid = logo_file_uuid
        if user_uuid is not None:
          self.user_uuid = user_uuid
        if created_on is not None:
          self.created_on = created_on
        self.email = email
        if last_login is not None:
          self.last_login = last_login
        if is_active is not None:
          self.is_active = is_active

    @property
    def role_name(self):
        """
        Gets the role_name of this UserGet.

        :return: The role_name of this UserGet.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """
        Sets the role_name of this UserGet.

        :param role_name: The role_name of this UserGet.
        :type: str
        """
        allowed_values = ["admin", "user"]
        if role_name not in allowed_values:
            raise ValueError(
                "Invalid value for `role_name` ({0}), must be one of {1}"
                .format(role_name, allowed_values)
            )

        self._role_name = role_name

    @property
    def passwd(self):
        """
        Gets the passwd of this UserGet.

        :return: The passwd of this UserGet.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """
        Sets the passwd of this UserGet.

        :param passwd: The passwd of this UserGet.
        :type: str
        """

        self._passwd = passwd

    @property
    def is_admin(self):
        """
        Gets the is_admin of this UserGet.

        :return: The is_admin of this UserGet.
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """
        Sets the is_admin of this UserGet.

        :param is_admin: The is_admin of this UserGet.
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def logo_file_uuid(self):
        """
        Gets the logo_file_uuid of this UserGet.

        :return: The logo_file_uuid of this UserGet.
        :rtype: str
        """
        return self._logo_file_uuid

    @logo_file_uuid.setter
    def logo_file_uuid(self, logo_file_uuid):
        """
        Sets the logo_file_uuid of this UserGet.

        :param logo_file_uuid: The logo_file_uuid of this UserGet.
        :type: str
        """

        self._logo_file_uuid = logo_file_uuid

    @property
    def user_uuid(self):
        """
        Gets the user_uuid of this UserGet.

        :return: The user_uuid of this UserGet.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """
        Sets the user_uuid of this UserGet.

        :param user_uuid: The user_uuid of this UserGet.
        :type: str
        """
        if user_uuid is not None and len(user_uuid) > 36:
            raise ValueError("Invalid value for `user_uuid`, length must be less than or equal to `36`")

        self._user_uuid = user_uuid

    @property
    def created_on(self):
        """
        Gets the created_on of this UserGet.

        :return: The created_on of this UserGet.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this UserGet.

        :param created_on: The created_on of this UserGet.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def email(self):
        """
        Gets the email of this UserGet.

        :return: The email of this UserGet.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserGet.

        :param email: The email of this UserGet.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def last_login(self):
        """
        Gets the last_login of this UserGet.

        :return: The last_login of this UserGet.
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """
        Sets the last_login of this UserGet.

        :param last_login: The last_login of this UserGet.
        :type: datetime
        """

        self._last_login = last_login

    @property
    def is_active(self):
        """
        Gets the is_active of this UserGet.

        :return: The is_active of this UserGet.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this UserGet.

        :param is_active: The is_active of this UserGet.
        :type: bool
        """

        self._is_active = is_active

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UserGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
