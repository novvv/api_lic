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


class LicenseSwitchModify(object):
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
        'end_time': 'datetime',
        'package_switch_uuid': 'str',
        'ip': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'end_time': 'end_time',
        'package_switch_uuid': 'package_switch_uuid',
        'ip': 'ip',
        'enabled': 'enabled'
    }

    def __init__(self, end_time=None, package_switch_uuid=None, ip=None, enabled=None):
        """
        LicenseSwitchModify - a model defined in Swagger
        """

        self._end_time = None
        self._package_switch_uuid = None
        self._ip = None
        self._enabled = None

        if end_time is not None:
          self.end_time = end_time
        if package_switch_uuid is not None:
          self.package_switch_uuid = package_switch_uuid
        if ip is not None:
          self.ip = ip
        if enabled is not None:
          self.enabled = enabled

    @property
    def end_time(self):
        """
        Gets the end_time of this LicenseSwitchModify.

        :return: The end_time of this LicenseSwitchModify.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this LicenseSwitchModify.

        :param end_time: The end_time of this LicenseSwitchModify.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def package_switch_uuid(self):
        """
        Gets the package_switch_uuid of this LicenseSwitchModify.

        :return: The package_switch_uuid of this LicenseSwitchModify.
        :rtype: str
        """
        return self._package_switch_uuid

    @package_switch_uuid.setter
    def package_switch_uuid(self, package_switch_uuid):
        """
        Sets the package_switch_uuid of this LicenseSwitchModify.

        :param package_switch_uuid: The package_switch_uuid of this LicenseSwitchModify.
        :type: str
        """
        if package_switch_uuid is not None and len(package_switch_uuid) > 36:
            raise ValueError("Invalid value for `package_switch_uuid`, length must be less than or equal to `36`")

        self._package_switch_uuid = package_switch_uuid

    @property
    def ip(self):
        """
        Gets the ip of this LicenseSwitchModify.

        :return: The ip of this LicenseSwitchModify.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this LicenseSwitchModify.

        :param ip: The ip of this LicenseSwitchModify.
        :type: str
        """
        if ip is not None and len(ip) > 16:
            raise ValueError("Invalid value for `ip`, length must be less than or equal to `16`")

        self._ip = ip

    @property
    def enabled(self):
        """
        Gets the enabled of this LicenseSwitchModify.

        :return: The enabled of this LicenseSwitchModify.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this LicenseSwitchModify.

        :param enabled: The enabled of this LicenseSwitchModify.
        :type: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, LicenseSwitchModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
