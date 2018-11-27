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


class SwitchModify(object):
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
        'current_port_count': 'int',
        'minute_remaining': 'int',
        'expired_on': 'datetime',
        'enabled': 'bool',
        'switch_ip': 'str',
        'email': 'str'
    }

    attribute_map = {
        'current_port_count': 'current_port_count',
        'minute_remaining': 'minute_remaining',
        'expired_on': 'expired_on',
        'enabled': 'enabled',
        'switch_ip': 'switch_ip',
        'email': 'email'
    }

    def __init__(self, current_port_count=None, minute_remaining=None, expired_on=None, enabled=None, switch_ip=None, email=None):
        """
        SwitchModify - a model defined in Swagger
        """

        self._current_port_count = None
        self._minute_remaining = None
        self._expired_on = None
        self._enabled = None
        self._switch_ip = None
        self._email = None

        if current_port_count is not None:
          self.current_port_count = current_port_count
        if minute_remaining is not None:
          self.minute_remaining = minute_remaining
        if expired_on is not None:
          self.expired_on = expired_on
        if enabled is not None:
          self.enabled = enabled
        if switch_ip is not None:
          self.switch_ip = switch_ip
        if email is not None:
          self.email = email

    @property
    def current_port_count(self):
        """
        Gets the current_port_count of this SwitchModify.

        :return: The current_port_count of this SwitchModify.
        :rtype: int
        """
        return self._current_port_count

    @current_port_count.setter
    def current_port_count(self, current_port_count):
        """
        Sets the current_port_count of this SwitchModify.

        :param current_port_count: The current_port_count of this SwitchModify.
        :type: int
        """

        self._current_port_count = current_port_count

    @property
    def minute_remaining(self):
        """
        Gets the minute_remaining of this SwitchModify.

        :return: The minute_remaining of this SwitchModify.
        :rtype: int
        """
        return self._minute_remaining

    @minute_remaining.setter
    def minute_remaining(self, minute_remaining):
        """
        Sets the minute_remaining of this SwitchModify.

        :param minute_remaining: The minute_remaining of this SwitchModify.
        :type: int
        """

        self._minute_remaining = minute_remaining

    @property
    def expired_on(self):
        """
        Gets the expired_on of this SwitchModify.

        :return: The expired_on of this SwitchModify.
        :rtype: datetime
        """
        return self._expired_on

    @expired_on.setter
    def expired_on(self, expired_on):
        """
        Sets the expired_on of this SwitchModify.

        :param expired_on: The expired_on of this SwitchModify.
        :type: datetime
        """

        self._expired_on = expired_on

    @property
    def enabled(self):
        """
        Gets the enabled of this SwitchModify.

        :return: The enabled of this SwitchModify.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SwitchModify.

        :param enabled: The enabled of this SwitchModify.
        :type: bool
        """

        self._enabled = enabled

    @property
    def switch_ip(self):
        """
        Gets the switch_ip of this SwitchModify.

        :return: The switch_ip of this SwitchModify.
        :rtype: str
        """
        return self._switch_ip

    @switch_ip.setter
    def switch_ip(self, switch_ip):
        """
        Sets the switch_ip of this SwitchModify.

        :param switch_ip: The switch_ip of this SwitchModify.
        :type: str
        """
        if switch_ip is not None and len(switch_ip) > 16:
            raise ValueError("Invalid value for `switch_ip`, length must be less than or equal to `16`")

        self._switch_ip = switch_ip

    @property
    def email(self):
        """
        Gets the email of this SwitchModify.

        :return: The email of this SwitchModify.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this SwitchModify.

        :param email: The email of this SwitchModify.
        :type: str
        """
        if email is not None and len(email) > 256:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `256`")

        self._email = email

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
        if not isinstance(other, SwitchModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
