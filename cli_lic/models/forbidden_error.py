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


class ForbiddenError(object):
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
        'error_type': 'str',
        'error': 'OperationErrorError'
    }

    attribute_map = {
        'success': 'success',
        'error_type': 'error_type',
        'error': 'error'
    }

    def __init__(self, success=False, error_type='forbidden_error', error=None):
        """
        ForbiddenError - a model defined in Swagger
        """

        self._success = None
        self._error_type = None
        self._error = None

        if success is not None:
          self.success = success
        if error_type is not None:
          self.error_type = error_type
        if error is not None:
          self.error = error

    @property
    def success(self):
        """
        Gets the success of this ForbiddenError.

        :return: The success of this ForbiddenError.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ForbiddenError.

        :param success: The success of this ForbiddenError.
        :type: bool
        """

        self._success = success

    @property
    def error_type(self):
        """
        Gets the error_type of this ForbiddenError.

        :return: The error_type of this ForbiddenError.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this ForbiddenError.

        :param error_type: The error_type of this ForbiddenError.
        :type: str
        """

        self._error_type = error_type

    @property
    def error(self):
        """
        Gets the error of this ForbiddenError.

        :return: The error of this ForbiddenError.
        :rtype: OperationErrorError
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ForbiddenError.

        :param error: The error of this ForbiddenError.
        :type: OperationErrorError
        """

        self._error = error

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
        if not isinstance(other, ForbiddenError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
