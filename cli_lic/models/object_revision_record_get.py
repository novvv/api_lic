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


class ObjectRevisionRecordGet(object):
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
        'field_name': 'str',
        'old_value': 'str',
        'new_value': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'old_value': 'old_value',
        'new_value': 'new_value'
    }

    def __init__(self, field_name=None, old_value=None, new_value=None):
        """
        ObjectRevisionRecordGet - a model defined in Swagger
        """

        self._field_name = None
        self._old_value = None
        self._new_value = None

        self.field_name = field_name
        if old_value is not None:
          self.old_value = old_value
        if new_value is not None:
          self.new_value = new_value

    @property
    def field_name(self):
        """
        Gets the field_name of this ObjectRevisionRecordGet.

        :return: The field_name of this ObjectRevisionRecordGet.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this ObjectRevisionRecordGet.

        :param field_name: The field_name of this ObjectRevisionRecordGet.
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")
        if field_name is not None and len(field_name) > 64:
            raise ValueError("Invalid value for `field_name`, length must be less than or equal to `64`")

        self._field_name = field_name

    @property
    def old_value(self):
        """
        Gets the old_value of this ObjectRevisionRecordGet.

        :return: The old_value of this ObjectRevisionRecordGet.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """
        Sets the old_value of this ObjectRevisionRecordGet.

        :param old_value: The old_value of this ObjectRevisionRecordGet.
        :type: str
        """

        self._old_value = old_value

    @property
    def new_value(self):
        """
        Gets the new_value of this ObjectRevisionRecordGet.

        :return: The new_value of this ObjectRevisionRecordGet.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """
        Sets the new_value of this ObjectRevisionRecordGet.

        :param new_value: The new_value of this ObjectRevisionRecordGet.
        :type: str
        """

        self._new_value = new_value

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
        if not isinstance(other, ObjectRevisionRecordGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
