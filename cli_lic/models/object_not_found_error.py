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


class ObjectNotFoundError(object):
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
        'error_type': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'error_type': 'error_type',
        'success': 'success'
    }

    def __init__(self, error_type='not_found_error', success=False):
        """
        ObjectNotFoundError - a model defined in Swagger
        """

        self._error_type = None
        self._success = None

        if error_type is not None:
          self.error_type = error_type
        if success is not None:
          self.success = success

    @property
    def error_type(self):
        """
        Gets the error_type of this ObjectNotFoundError.

        :return: The error_type of this ObjectNotFoundError.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this ObjectNotFoundError.

        :param error_type: The error_type of this ObjectNotFoundError.
        :type: str
        """

        self._error_type = error_type

    @property
    def success(self):
        """
        Gets the success of this ObjectNotFoundError.

        :return: The success of this ObjectNotFoundError.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ObjectNotFoundError.

        :param success: The success of this ObjectNotFoundError.
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
        if not isinstance(other, ObjectNotFoundError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
