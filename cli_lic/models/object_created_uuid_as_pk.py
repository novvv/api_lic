# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ObjectCreatedUuidAsPk(object):
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
        'object_uuid': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'object_uuid': 'object_uuid',
        'success': 'success'
    }

    def __init__(self, object_uuid=None, success=True):
        """
        ObjectCreatedUuidAsPk - a model defined in Swagger
        """

        self._object_uuid = None
        self._success = None

        if object_uuid is not None:
          self.object_uuid = object_uuid
        if success is not None:
          self.success = success

    @property
    def object_uuid(self):
        """
        Gets the object_uuid of this ObjectCreatedUuidAsPk.

        :return: The object_uuid of this ObjectCreatedUuidAsPk.
        :rtype: str
        """
        return self._object_uuid

    @object_uuid.setter
    def object_uuid(self, object_uuid):
        """
        Sets the object_uuid of this ObjectCreatedUuidAsPk.

        :param object_uuid: The object_uuid of this ObjectCreatedUuidAsPk.
        :type: str
        """

        self._object_uuid = object_uuid

    @property
    def success(self):
        """
        Gets the success of this ObjectCreatedUuidAsPk.

        :return: The success of this ObjectCreatedUuidAsPk.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ObjectCreatedUuidAsPk.

        :param success: The success of this ObjectCreatedUuidAsPk.
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
        if not isinstance(other, ObjectCreatedUuidAsPk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
