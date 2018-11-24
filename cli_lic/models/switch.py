# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Switch(object):
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
        'expired_on': 'datetime',
        'enabled': 'bool',
        'email': 'str',
        'minute_remaining': 'int',
        'switch_ip': 'str',
        'current_port_count': 'int'
    }

    attribute_map = {
        'expired_on': 'expired_on',
        'enabled': 'enabled',
        'email': 'email',
        'minute_remaining': 'minute_remaining',
        'switch_ip': 'switch_ip',
        'current_port_count': 'current_port_count'
    }

    def __init__(self, expired_on=None, enabled=None, email=None, minute_remaining=None, switch_ip=None, current_port_count=None):
        """
        Switch - a model defined in Swagger
        """

        self._expired_on = None
        self._enabled = None
        self._email = None
        self._minute_remaining = None
        self._switch_ip = None
        self._current_port_count = None

        if expired_on is not None:
          self.expired_on = expired_on
        if enabled is not None:
          self.enabled = enabled
        if email is not None:
          self.email = email
        if minute_remaining is not None:
          self.minute_remaining = minute_remaining
        if switch_ip is not None:
          self.switch_ip = switch_ip
        if current_port_count is not None:
          self.current_port_count = current_port_count

    @property
    def expired_on(self):
        """
        Gets the expired_on of this Switch.

        :return: The expired_on of this Switch.
        :rtype: datetime
        """
        return self._expired_on

    @expired_on.setter
    def expired_on(self, expired_on):
        """
        Sets the expired_on of this Switch.

        :param expired_on: The expired_on of this Switch.
        :type: datetime
        """

        self._expired_on = expired_on

    @property
    def enabled(self):
        """
        Gets the enabled of this Switch.

        :return: The enabled of this Switch.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this Switch.

        :param enabled: The enabled of this Switch.
        :type: bool
        """

        self._enabled = enabled

    @property
    def email(self):
        """
        Gets the email of this Switch.

        :return: The email of this Switch.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Switch.

        :param email: The email of this Switch.
        :type: str
        """
        if email is not None and len(email) > 256:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `256`")

        self._email = email

    @property
    def minute_remaining(self):
        """
        Gets the minute_remaining of this Switch.

        :return: The minute_remaining of this Switch.
        :rtype: int
        """
        return self._minute_remaining

    @minute_remaining.setter
    def minute_remaining(self, minute_remaining):
        """
        Sets the minute_remaining of this Switch.

        :param minute_remaining: The minute_remaining of this Switch.
        :type: int
        """

        self._minute_remaining = minute_remaining

    @property
    def switch_ip(self):
        """
        Gets the switch_ip of this Switch.

        :return: The switch_ip of this Switch.
        :rtype: str
        """
        return self._switch_ip

    @switch_ip.setter
    def switch_ip(self, switch_ip):
        """
        Sets the switch_ip of this Switch.

        :param switch_ip: The switch_ip of this Switch.
        :type: str
        """
        if switch_ip is not None and len(switch_ip) > 16:
            raise ValueError("Invalid value for `switch_ip`, length must be less than or equal to `16`")

        self._switch_ip = switch_ip

    @property
    def current_port_count(self):
        """
        Gets the current_port_count of this Switch.

        :return: The current_port_count of this Switch.
        :rtype: int
        """
        return self._current_port_count

    @current_port_count.setter
    def current_port_count(self, current_port_count):
        """
        Sets the current_port_count of this Switch.

        :param current_port_count: The current_port_count of this Switch.
        :type: int
        """

        self._current_port_count = current_port_count

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
        if not isinstance(other, Switch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
