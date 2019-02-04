# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserRegister(object):
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
        'email': 'str',
        'passwd': 'str',
        'first_name': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'email': 'email',
        'passwd': 'passwd',
        'first_name': 'first_name',
        'last_name': 'last_name'
    }

    def __init__(self, email=None, passwd=None, first_name=None, last_name=None):
        """
        UserRegister - a model defined in Swagger
        """

        self._email = None
        self._passwd = None
        self._first_name = None
        self._last_name = None

        self.email = email
        if passwd is not None:
          self.passwd = passwd
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name

    @property
    def email(self):
        """
        Gets the email of this UserRegister.

        :return: The email of this UserRegister.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserRegister.

        :param email: The email of this UserRegister.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def passwd(self):
        """
        Gets the passwd of this UserRegister.

        :return: The passwd of this UserRegister.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """
        Sets the passwd of this UserRegister.

        :param passwd: The passwd of this UserRegister.
        :type: str
        """

        self._passwd = passwd

    @property
    def first_name(self):
        """
        Gets the first_name of this UserRegister.

        :return: The first_name of this UserRegister.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserRegister.

        :param first_name: The first_name of this UserRegister.
        :type: str
        """
        if first_name is not None and len(first_name) > 32:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `32`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this UserRegister.

        :return: The last_name of this UserRegister.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserRegister.

        :param last_name: The last_name of this UserRegister.
        :type: str
        """
        if last_name is not None and len(last_name) > 32:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `32`")

        self._last_name = last_name

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
        if not isinstance(other, UserRegister):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
