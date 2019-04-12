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


class InlineResponse20024(object):
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
        'success': 'bool',
        'payload': 'InlineResponse20024Payload'
    }

    attribute_map = {
        'success': 'success',
        'payload': 'payload'
    }

    def __init__(self, success=True, payload=None):
        """
        InlineResponse20024 - a model defined in Swagger
        """

        self._success = None
        self._payload = None

        if success is not None:
          self.success = success
        if payload is not None:
          self.payload = payload

    @property
    def success(self):
        """
        Gets the success of this InlineResponse20024.

        :return: The success of this InlineResponse20024.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this InlineResponse20024.

        :param success: The success of this InlineResponse20024.
        :type: bool
        """

        self._success = success

    @property
    def payload(self):
        """
        Gets the payload of this InlineResponse20024.

        :return: The payload of this InlineResponse20024.
        :rtype: InlineResponse20024Payload
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this InlineResponse20024.

        :param payload: The payload of this InlineResponse20024.
        :type: InlineResponse20024Payload
        """

        self._payload = payload

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
        if not isinstance(other, InlineResponse20024):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
