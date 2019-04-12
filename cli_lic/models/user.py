# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class User(object):
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
        'passwd': 'str',
        'logo_file_uuid': 'str',
        'email': 'str',
        'is_active': 'bool',
        'is_admin': 'bool'
    }

    attribute_map = {
        'passwd': 'passwd',
        'logo_file_uuid': 'logo_file_uuid',
        'email': 'email',
        'is_active': 'is_active',
        'is_admin': 'is_admin'
    }

    def __init__(self, passwd=None, logo_file_uuid=None, email=None, is_active=None, is_admin=None):
        """
        User - a model defined in Swagger
        """

        self._passwd = None
        self._logo_file_uuid = None
        self._email = None
        self._is_active = None
        self._is_admin = None

        if passwd is not None:
          self.passwd = passwd
        if logo_file_uuid is not None:
          self.logo_file_uuid = logo_file_uuid
        self.email = email
        if is_active is not None:
          self.is_active = is_active
        if is_admin is not None:
          self.is_admin = is_admin

    @property
    def passwd(self):
        """
        Gets the passwd of this User.

        :return: The passwd of this User.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """
        Sets the passwd of this User.

        :param passwd: The passwd of this User.
        :type: str
        """

        self._passwd = passwd

    @property
    def logo_file_uuid(self):
        """
        Gets the logo_file_uuid of this User.

        :return: The logo_file_uuid of this User.
        :rtype: str
        """
        return self._logo_file_uuid

    @logo_file_uuid.setter
    def logo_file_uuid(self, logo_file_uuid):
        """
        Sets the logo_file_uuid of this User.

        :param logo_file_uuid: The logo_file_uuid of this User.
        :type: str
        """

        self._logo_file_uuid = logo_file_uuid

    @property
    def email(self):
        """
        Gets the email of this User.

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.

        :param email: The email of this User.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def is_active(self):
        """
        Gets the is_active of this User.

        :return: The is_active of this User.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this User.

        :param is_active: The is_active of this User.
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_admin(self):
        """
        Gets the is_admin of this User.

        :return: The is_admin of this User.
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """
        Sets the is_admin of this User.

        :param is_admin: The is_admin of this User.
        :type: bool
        """

        self._is_admin = is_admin

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
