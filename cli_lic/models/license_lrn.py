# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LicenseLrn(object):
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
        'start_time': 'datetime',
        'package_lrn_uuid': 'str',
        'end_time': 'datetime',
        'ip': 'str',
        'duration': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'package_lrn_uuid': 'package_lrn_uuid',
        'end_time': 'end_time',
        'ip': 'ip',
        'duration': 'duration'
    }

    def __init__(self, start_time=None, package_lrn_uuid=None, end_time=None, ip=None, duration='1 month'):
        """
        LicenseLrn - a model defined in Swagger
        """

        self._start_time = None
        self._package_lrn_uuid = None
        self._end_time = None
        self._ip = None
        self._duration = None

        if start_time is not None:
          self.start_time = start_time
        if package_lrn_uuid is not None:
          self.package_lrn_uuid = package_lrn_uuid
        if end_time is not None:
          self.end_time = end_time
        self.ip = ip
        if duration is not None:
          self.duration = duration

    @property
    def start_time(self):
        """
        Gets the start_time of this LicenseLrn.

        :return: The start_time of this LicenseLrn.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this LicenseLrn.

        :param start_time: The start_time of this LicenseLrn.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def package_lrn_uuid(self):
        """
        Gets the package_lrn_uuid of this LicenseLrn.

        :return: The package_lrn_uuid of this LicenseLrn.
        :rtype: str
        """
        return self._package_lrn_uuid

    @package_lrn_uuid.setter
    def package_lrn_uuid(self, package_lrn_uuid):
        """
        Sets the package_lrn_uuid of this LicenseLrn.

        :param package_lrn_uuid: The package_lrn_uuid of this LicenseLrn.
        :type: str
        """
        if package_lrn_uuid is not None and len(package_lrn_uuid) > 36:
            raise ValueError("Invalid value for `package_lrn_uuid`, length must be less than or equal to `36`")

        self._package_lrn_uuid = package_lrn_uuid

    @property
    def end_time(self):
        """
        Gets the end_time of this LicenseLrn.

        :return: The end_time of this LicenseLrn.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this LicenseLrn.

        :param end_time: The end_time of this LicenseLrn.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def ip(self):
        """
        Gets the ip of this LicenseLrn.

        :return: The ip of this LicenseLrn.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this LicenseLrn.

        :param ip: The ip of this LicenseLrn.
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")
        if ip is not None and len(ip) > 16:
            raise ValueError("Invalid value for `ip`, length must be less than or equal to `16`")

        self._ip = ip

    @property
    def duration(self):
        """
        Gets the duration of this LicenseLrn.

        :return: The duration of this LicenseLrn.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this LicenseLrn.

        :param duration: The duration of this LicenseLrn.
        :type: str
        """
        allowed_values = ["1 month", "3 months", "12 months", "6 months"]
        if duration not in allowed_values:
            raise ValueError(
                "Invalid value for `duration` ({0}), must be one of {1}"
                .format(duration, allowed_values)
            )

        self._duration = duration

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
        if not isinstance(other, LicenseLrn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
