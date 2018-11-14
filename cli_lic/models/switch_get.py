# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SwitchGet(object):
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
        'enabled': 'bool',
        'switch_ip': 'str',
        'current_port_count': 'int',
        'packages': 'list[PackageSwitch]',
        'email': 'str',
        'switch_uuid': 'str',
        'minute_remaining': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'switch_ip': 'switch_ip',
        'current_port_count': 'current_port_count',
        'packages': 'packages',
        'email': 'email',
        'switch_uuid': 'switch_uuid',
        'minute_remaining': 'minute_remaining'
    }

    def __init__(self, enabled=None, switch_ip=None, current_port_count=None, packages=None, email=None, switch_uuid=None, minute_remaining=None):
        """
        SwitchGet - a model defined in Swagger
        """

        self._enabled = None
        self._switch_ip = None
        self._current_port_count = None
        self._packages = None
        self._email = None
        self._switch_uuid = None
        self._minute_remaining = None

        if enabled is not None:
          self.enabled = enabled
        if switch_ip is not None:
          self.switch_ip = switch_ip
        if current_port_count is not None:
          self.current_port_count = current_port_count
        if packages is not None:
          self.packages = packages
        if email is not None:
          self.email = email
        if switch_uuid is not None:
          self.switch_uuid = switch_uuid
        if minute_remaining is not None:
          self.minute_remaining = minute_remaining

    @property
    def enabled(self):
        """
        Gets the enabled of this SwitchGet.

        :return: The enabled of this SwitchGet.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SwitchGet.

        :param enabled: The enabled of this SwitchGet.
        :type: bool
        """

        self._enabled = enabled

    @property
    def switch_ip(self):
        """
        Gets the switch_ip of this SwitchGet.

        :return: The switch_ip of this SwitchGet.
        :rtype: str
        """
        return self._switch_ip

    @switch_ip.setter
    def switch_ip(self, switch_ip):
        """
        Sets the switch_ip of this SwitchGet.

        :param switch_ip: The switch_ip of this SwitchGet.
        :type: str
        """
        if switch_ip is not None and len(switch_ip) > 16:
            raise ValueError("Invalid value for `switch_ip`, length must be less than or equal to `16`")

        self._switch_ip = switch_ip

    @property
    def current_port_count(self):
        """
        Gets the current_port_count of this SwitchGet.

        :return: The current_port_count of this SwitchGet.
        :rtype: int
        """
        return self._current_port_count

    @current_port_count.setter
    def current_port_count(self, current_port_count):
        """
        Sets the current_port_count of this SwitchGet.

        :param current_port_count: The current_port_count of this SwitchGet.
        :type: int
        """

        self._current_port_count = current_port_count

    @property
    def packages(self):
        """
        Gets the packages of this SwitchGet.

        :return: The packages of this SwitchGet.
        :rtype: list[PackageSwitch]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this SwitchGet.

        :param packages: The packages of this SwitchGet.
        :type: list[PackageSwitch]
        """

        self._packages = packages

    @property
    def email(self):
        """
        Gets the email of this SwitchGet.

        :return: The email of this SwitchGet.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this SwitchGet.

        :param email: The email of this SwitchGet.
        :type: str
        """
        if email is not None and len(email) > 256:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `256`")

        self._email = email

    @property
    def switch_uuid(self):
        """
        Gets the switch_uuid of this SwitchGet.

        :return: The switch_uuid of this SwitchGet.
        :rtype: str
        """
        return self._switch_uuid

    @switch_uuid.setter
    def switch_uuid(self, switch_uuid):
        """
        Sets the switch_uuid of this SwitchGet.

        :param switch_uuid: The switch_uuid of this SwitchGet.
        :type: str
        """
        if switch_uuid is not None and len(switch_uuid) > 36:
            raise ValueError("Invalid value for `switch_uuid`, length must be less than or equal to `36`")

        self._switch_uuid = switch_uuid

    @property
    def minute_remaining(self):
        """
        Gets the minute_remaining of this SwitchGet.

        :return: The minute_remaining of this SwitchGet.
        :rtype: int
        """
        return self._minute_remaining

    @minute_remaining.setter
    def minute_remaining(self, minute_remaining):
        """
        Sets the minute_remaining of this SwitchGet.

        :param minute_remaining: The minute_remaining of this SwitchGet.
        :type: int
        """

        self._minute_remaining = minute_remaining

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
        if not isinstance(other, SwitchGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
