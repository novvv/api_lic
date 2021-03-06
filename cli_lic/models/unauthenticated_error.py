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


class UnauthenticatedError(object):
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
        'error': 'ForbiddenErrorError',
        'error_type': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'error': 'error',
        'error_type': 'error_type',
        'success': 'success'
    }

    def __init__(self, error=None, error_type='unauthenticated_error', success=False):
        """
        UnauthenticatedError - a model defined in Swagger
        """

        self._error = None
        self._error_type = None
        self._success = None

        if error is not None:
          self.error = error
        if error_type is not None:
          self.error_type = error_type
        if success is not None:
          self.success = success

    @property
    def error(self):
        """
        Gets the error of this UnauthenticatedError.

        :return: The error of this UnauthenticatedError.
        :rtype: ForbiddenErrorError
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this UnauthenticatedError.

        :param error: The error of this UnauthenticatedError.
        :type: ForbiddenErrorError
        """

        self._error = error

    @property
    def error_type(self):
        """
        Gets the error_type of this UnauthenticatedError.

        :return: The error_type of this UnauthenticatedError.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this UnauthenticatedError.

        :param error_type: The error_type of this UnauthenticatedError.
        :type: str
        """

        self._error_type = error_type

    @property
    def success(self):
        """
        Gets the success of this UnauthenticatedError.

        :return: The success of this UnauthenticatedError.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this UnauthenticatedError.

        :param success: The success of this UnauthenticatedError.
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
        if not isinstance(other, UnauthenticatedError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
