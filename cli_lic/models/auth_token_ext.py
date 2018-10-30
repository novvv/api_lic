# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AuthTokenExt(object):
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
        'payload': 'AuthTokenInner',
        'success': 'bool'
    }

    attribute_map = {
        'payload': 'payload',
        'success': 'success'
    }

    def __init__(self, payload=None, success=True):
        """
        AuthTokenExt - a model defined in Swagger
        """

        self._payload = None
        self._success = None

        if payload is not None:
          self.payload = payload
        if success is not None:
          self.success = success

    @property
    def payload(self):
        """
        Gets the payload of this AuthTokenExt.

        :return: The payload of this AuthTokenExt.
        :rtype: AuthTokenInner
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this AuthTokenExt.

        :param payload: The payload of this AuthTokenExt.
        :type: AuthTokenInner
        """

        self._payload = payload

    @property
    def success(self):
        """
        Gets the success of this AuthTokenExt.

        :return: The success of this AuthTokenExt.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this AuthTokenExt.

        :param success: The success of this AuthTokenExt.
        :type: bool
        """

        self._success = success

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
        if not isinstance(other, AuthTokenExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
