# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserInfoModify(object):
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
        'passwd': 'str'
    }

    attribute_map = {
        'email': 'email',
        'passwd': 'passwd'
    }

    def __init__(self, email=None, passwd=None):
        """
        UserInfoModify - a model defined in Swagger
        """

        self._email = None
        self._passwd = None

        if email is not None:
          self.email = email
        if passwd is not None:
          self.passwd = passwd

    @property
    def email(self):
        """
        Gets the email of this UserInfoModify.

        :return: The email of this UserInfoModify.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserInfoModify.

        :param email: The email of this UserInfoModify.
        :type: str
        """

        self._email = email

    @property
    def passwd(self):
        """
        Gets the passwd of this UserInfoModify.

        :return: The passwd of this UserInfoModify.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """
        Sets the passwd of this UserInfoModify.

        :param passwd: The passwd of this UserInfoModify.
        :type: str
        """

        self._passwd = passwd

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
        if not isinstance(other, UserInfoModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
