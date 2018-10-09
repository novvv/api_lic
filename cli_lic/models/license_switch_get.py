# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LicenseSwitchGet(object):
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
        'ip': 'str',
        'license_uuid': 'str',
        'type': 'str',
        'license': 'License'
    }

    attribute_map = {
        'ip': 'ip',
        'license_uuid': 'license_uuid',
        'type': 'type',
        'license': 'license'
    }

    def __init__(self, ip=None, license_uuid=None, type='pay per port', license=None):
        """
        LicenseSwitchGet - a model defined in Swagger
        """

        self._ip = None
        self._license_uuid = None
        self._type = None
        self._license = None

        if ip is not None:
          self.ip = ip
        if license_uuid is not None:
          self.license_uuid = license_uuid
        if type is not None:
          self.type = type
        if license is not None:
          self.license = license

    @property
    def ip(self):
        """
        Gets the ip of this LicenseSwitchGet.

        :return: The ip of this LicenseSwitchGet.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this LicenseSwitchGet.

        :param ip: The ip of this LicenseSwitchGet.
        :type: str
        """
        if ip is not None and len(ip) > 16:
            raise ValueError("Invalid value for `ip`, length must be less than or equal to `16`")

        self._ip = ip

    @property
    def license_uuid(self):
        """
        Gets the license_uuid of this LicenseSwitchGet.

        :return: The license_uuid of this LicenseSwitchGet.
        :rtype: str
        """
        return self._license_uuid

    @license_uuid.setter
    def license_uuid(self, license_uuid):
        """
        Sets the license_uuid of this LicenseSwitchGet.

        :param license_uuid: The license_uuid of this LicenseSwitchGet.
        :type: str
        """
        if license_uuid is not None and len(license_uuid) > 36:
            raise ValueError("Invalid value for `license_uuid`, length must be less than or equal to `36`")

        self._license_uuid = license_uuid

    @property
    def type(self):
        """
        Gets the type of this LicenseSwitchGet.

        :return: The type of this LicenseSwitchGet.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LicenseSwitchGet.

        :param type: The type of this LicenseSwitchGet.
        :type: str
        """
        allowed_values = ["pay per port", "pay per minute"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def license(self):
        """
        Gets the license of this LicenseSwitchGet.

        :return: The license of this LicenseSwitchGet.
        :rtype: License
        """
        return self._license

    @license.setter
    def license(self, license):
        """
        Sets the license of this LicenseSwitchGet.

        :param license: The license of this LicenseSwitchGet.
        :type: License
        """

        self._license = license

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
        if not isinstance(other, LicenseSwitchGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
