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


class TokenCheck(object):
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
        'token': 'str',
        'exp': 'datetime'
    }

    attribute_map = {
        'token': 'token',
        'exp': 'exp'
    }

    def __init__(self, token=None, exp=None):
        """
        TokenCheck - a model defined in Swagger
        """

        self._token = None
        self._exp = None

        self.token = token
        if exp is not None:
          self.exp = exp

    @property
    def token(self):
        """
        Gets the token of this TokenCheck.

        :return: The token of this TokenCheck.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this TokenCheck.

        :param token: The token of this TokenCheck.
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")

        self._token = token

    @property
    def exp(self):
        """
        Gets the exp of this TokenCheck.

        :return: The exp of this TokenCheck.
        :rtype: datetime
        """
        return self._exp

    @exp.setter
    def exp(self, exp):
        """
        Sets the exp of this TokenCheck.

        :param exp: The exp of this TokenCheck.
        :type: datetime
        """

        self._exp = exp

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
        if not isinstance(other, TokenCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
