# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AttributeNotExists(object):
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
        'attribute': 'str',
        'error_type': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'attribute': 'attribute',
        'error_type': 'error_type',
        'success': 'success'
    }

    def __init__(self, attribute=None, error_type='attribute_not_exists', success=False):
        """
        AttributeNotExists - a model defined in Swagger
        """

        self._attribute = None
        self._error_type = None
        self._success = None

        if attribute is not None:
          self.attribute = attribute
        if error_type is not None:
          self.error_type = error_type
        if success is not None:
          self.success = success

    @property
    def attribute(self):
        """
        Gets the attribute of this AttributeNotExists.

        :return: The attribute of this AttributeNotExists.
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """
        Sets the attribute of this AttributeNotExists.

        :param attribute: The attribute of this AttributeNotExists.
        :type: str
        """

        self._attribute = attribute

    @property
    def error_type(self):
        """
        Gets the error_type of this AttributeNotExists.

        :return: The error_type of this AttributeNotExists.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this AttributeNotExists.

        :param error_type: The error_type of this AttributeNotExists.
        :type: str
        """

        self._error_type = error_type

    @property
    def success(self):
        """
        Gets the success of this AttributeNotExists.

        :return: The success of this AttributeNotExists.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this AttributeNotExists.

        :param success: The success of this AttributeNotExists.
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
        if not isinstance(other, AttributeNotExists):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
