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


class ForbiddenErrorError(object):
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
        'reason': 'str',
        'code': 'int',
        'message': 'str'
    }

    attribute_map = {
        'reason': 'reason',
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, reason=None, code=None, message=None):
        """
        ForbiddenErrorError - a model defined in Swagger
        """

        self._reason = None
        self._code = None
        self._message = None

        if reason is not None:
          self.reason = reason
        if code is not None:
          self.code = code
        if message is not None:
          self.message = message

    @property
    def reason(self):
        """
        Gets the reason of this ForbiddenErrorError.

        :return: The reason of this ForbiddenErrorError.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this ForbiddenErrorError.

        :param reason: The reason of this ForbiddenErrorError.
        :type: str
        """

        self._reason = reason

    @property
    def code(self):
        """
        Gets the code of this ForbiddenErrorError.

        :return: The code of this ForbiddenErrorError.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ForbiddenErrorError.

        :param code: The code of this ForbiddenErrorError.
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this ForbiddenErrorError.

        :return: The message of this ForbiddenErrorError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ForbiddenErrorError.

        :param message: The message of this ForbiddenErrorError.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, ForbiddenErrorError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
