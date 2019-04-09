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


class LicenseSwitch(object):
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
        'duration': 'str',
        'start_time': 'datetime',
        'ip': 'str',
        'switch_uuid': 'str',
        'package_switch_uuid': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'start_time': 'start_time',
        'ip': 'ip',
        'switch_uuid': 'switch_uuid',
        'package_switch_uuid': 'package_switch_uuid'
    }

    def __init__(self, duration='1 month', start_time=None, ip=None, switch_uuid=None, package_switch_uuid=None):
        """
        LicenseSwitch - a model defined in Swagger
        """

        self._duration = None
        self._start_time = None
        self._ip = None
        self._switch_uuid = None
        self._package_switch_uuid = None

        if duration is not None:
          self.duration = duration
        if start_time is not None:
          self.start_time = start_time
        self.ip = ip
        if switch_uuid is not None:
          self.switch_uuid = switch_uuid
        if package_switch_uuid is not None:
          self.package_switch_uuid = package_switch_uuid

    @property
    def duration(self):
        """
        Gets the duration of this LicenseSwitch.

        :return: The duration of this LicenseSwitch.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this LicenseSwitch.

        :param duration: The duration of this LicenseSwitch.
        :type: str
        """
        allowed_values = ["1 month", "3 months", "12 months", "6 months"]
        if duration not in allowed_values:
            raise ValueError(
                "Invalid value for `duration` ({0}), must be one of {1}"
                .format(duration, allowed_values)
            )

        self._duration = duration

    @property
    def start_time(self):
        """
        Gets the start_time of this LicenseSwitch.

        :return: The start_time of this LicenseSwitch.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this LicenseSwitch.

        :param start_time: The start_time of this LicenseSwitch.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def ip(self):
        """
        Gets the ip of this LicenseSwitch.

        :return: The ip of this LicenseSwitch.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this LicenseSwitch.

        :param ip: The ip of this LicenseSwitch.
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")
        if ip is not None and len(ip) > 16:
            raise ValueError("Invalid value for `ip`, length must be less than or equal to `16`")

        self._ip = ip

    @property
    def switch_uuid(self):
        """
        Gets the switch_uuid of this LicenseSwitch.

        :return: The switch_uuid of this LicenseSwitch.
        :rtype: str
        """
        return self._switch_uuid

    @switch_uuid.setter
    def switch_uuid(self, switch_uuid):
        """
        Sets the switch_uuid of this LicenseSwitch.

        :param switch_uuid: The switch_uuid of this LicenseSwitch.
        :type: str
        """
        if switch_uuid is not None and len(switch_uuid) > 64:
            raise ValueError("Invalid value for `switch_uuid`, length must be less than or equal to `64`")

        self._switch_uuid = switch_uuid

    @property
    def package_switch_uuid(self):
        """
        Gets the package_switch_uuid of this LicenseSwitch.

        :return: The package_switch_uuid of this LicenseSwitch.
        :rtype: str
        """
        return self._package_switch_uuid

    @package_switch_uuid.setter
    def package_switch_uuid(self, package_switch_uuid):
        """
        Sets the package_switch_uuid of this LicenseSwitch.

        :param package_switch_uuid: The package_switch_uuid of this LicenseSwitch.
        :type: str
        """
        if package_switch_uuid is not None and len(package_switch_uuid) > 36:
            raise ValueError("Invalid value for `package_switch_uuid`, length must be less than or equal to `36`")

        self._package_switch_uuid = package_switch_uuid

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
        if not isinstance(other, LicenseSwitch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
