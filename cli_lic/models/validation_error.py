# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ValidationError(object):
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
        'errors': 'list[object]'
    }

    attribute_map = {
        'success': 'success',
        'error_type': 'error_type',
        'errors': 'errors'
    }

    def __init__(self, success=False, error_type='validation_error', errors=None):
        """
        ValidationError - a model defined in Swagger
        """

        self._success = None
        self._error_type = None
        self._errors = None

        if success is not None:
          self.success = success
        if error_type is not None:
          self.error_type = error_type
        if errors is not None:
          self.errors = errors

    @property
    def success(self):
        """
        Gets the success of this ValidationError.

        :return: The success of this ValidationError.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ValidationError.

        :param success: The success of this ValidationError.
        :type: bool
        """

        self._success = success

    @property
    def error_type(self):
        """
        Gets the error_type of this ValidationError.

        :return: The error_type of this ValidationError.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this ValidationError.

        :param error_type: The error_type of this ValidationError.
        :type: str
        """

        self._error_type = error_type

    @property
    def errors(self):
        """
        Gets the errors of this ValidationError.
        Key is the field name and value is the list of the validation errors for this fields

        :return: The errors of this ValidationError.
        :rtype: list[object]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ValidationError.
        Key is the field name and value is the list of the validation errors for this fields

        :param errors: The errors of this ValidationError.
        :type: list[object]
        """

        self._errors = errors

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
        if not isinstance(other, ValidationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
