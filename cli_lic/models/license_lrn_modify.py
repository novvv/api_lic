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


class LicenseLrnModify(object):
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
        'package_lrn_uuid': 'str',
        'end_time': 'datetime',
        'ip': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'package_lrn_uuid': 'package_lrn_uuid',
        'end_time': 'end_time',
        'ip': 'ip'
    }

    def __init__(self, enabled=None, package_lrn_uuid=None, end_time=None, ip=None):
        """
        LicenseLrnModify - a model defined in Swagger
        """

        self._enabled = None
        self._package_lrn_uuid = None
        self._end_time = None
        self._ip = None

        if enabled is not None:
          self.enabled = enabled
        if package_lrn_uuid is not None:
          self.package_lrn_uuid = package_lrn_uuid
        if end_time is not None:
          self.end_time = end_time
        if ip is not None:
          self.ip = ip

    @property
    def enabled(self):
        """
        Gets the enabled of this LicenseLrnModify.

        :return: The enabled of this LicenseLrnModify.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this LicenseLrnModify.

        :param enabled: The enabled of this LicenseLrnModify.
        :type: bool
        """

        self._enabled = enabled

    @property
    def package_lrn_uuid(self):
        """
        Gets the package_lrn_uuid of this LicenseLrnModify.

        :return: The package_lrn_uuid of this LicenseLrnModify.
        :rtype: str
        """
        return self._package_lrn_uuid

    @package_lrn_uuid.setter
    def package_lrn_uuid(self, package_lrn_uuid):
        """
        Sets the package_lrn_uuid of this LicenseLrnModify.

        :param package_lrn_uuid: The package_lrn_uuid of this LicenseLrnModify.
        :type: str
        """
        if package_lrn_uuid is not None and len(package_lrn_uuid) > 36:
            raise ValueError("Invalid value for `package_lrn_uuid`, length must be less than or equal to `36`")

        self._package_lrn_uuid = package_lrn_uuid

    @property
    def end_time(self):
        """
        Gets the end_time of this LicenseLrnModify.

        :return: The end_time of this LicenseLrnModify.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this LicenseLrnModify.

        :param end_time: The end_time of this LicenseLrnModify.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def ip(self):
        """
        Gets the ip of this LicenseLrnModify.

        :return: The ip of this LicenseLrnModify.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this LicenseLrnModify.

        :param ip: The ip of this LicenseLrnModify.
        :type: str
        """
        if ip is not None and len(ip) > 16:
            raise ValueError("Invalid value for `ip`, length must be less than or equal to `16`")

        self._ip = ip

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
        if not isinstance(other, LicenseLrnModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
