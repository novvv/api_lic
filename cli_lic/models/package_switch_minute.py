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


class PackageSwitchMinute(object):
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
        'rate_per_minute': 'float',
        'amount': 'int',
        'package_name': 'str',
        'package_switch_uuid': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'rate_per_minute': 'rate_per_minute',
        'amount': 'amount',
        'package_name': 'package_name',
        'package_switch_uuid': 'package_switch_uuid'
    }

    def __init__(self, enabled=None, rate_per_minute=None, amount=None, package_name=None, package_switch_uuid=None):
        """
        PackageSwitchMinute - a model defined in Swagger
        """

        self._enabled = None
        self._rate_per_minute = None
        self._amount = None
        self._package_name = None
        self._package_switch_uuid = None

        if enabled is not None:
          self.enabled = enabled
        if rate_per_minute is not None:
          self.rate_per_minute = rate_per_minute
        if amount is not None:
          self.amount = amount
        if package_name is not None:
          self.package_name = package_name
        if package_switch_uuid is not None:
          self.package_switch_uuid = package_switch_uuid

    @property
    def enabled(self):
        """
        Gets the enabled of this PackageSwitchMinute.

        :return: The enabled of this PackageSwitchMinute.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this PackageSwitchMinute.

        :param enabled: The enabled of this PackageSwitchMinute.
        :type: bool
        """

        self._enabled = enabled

    @property
    def rate_per_minute(self):
        """
        Gets the rate_per_minute of this PackageSwitchMinute.

        :return: The rate_per_minute of this PackageSwitchMinute.
        :rtype: float
        """
        return self._rate_per_minute

    @rate_per_minute.setter
    def rate_per_minute(self, rate_per_minute):
        """
        Sets the rate_per_minute of this PackageSwitchMinute.

        :param rate_per_minute: The rate_per_minute of this PackageSwitchMinute.
        :type: float
        """

        self._rate_per_minute = rate_per_minute

    @property
    def amount(self):
        """
        Gets the amount of this PackageSwitchMinute.

        :return: The amount of this PackageSwitchMinute.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PackageSwitchMinute.

        :param amount: The amount of this PackageSwitchMinute.
        :type: int
        """

        self._amount = amount

    @property
    def package_name(self):
        """
        Gets the package_name of this PackageSwitchMinute.

        :return: The package_name of this PackageSwitchMinute.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """
        Sets the package_name of this PackageSwitchMinute.

        :param package_name: The package_name of this PackageSwitchMinute.
        :type: str
        """
        if package_name is not None and len(package_name) > 64:
            raise ValueError("Invalid value for `package_name`, length must be less than or equal to `64`")

        self._package_name = package_name

    @property
    def package_switch_uuid(self):
        """
        Gets the package_switch_uuid of this PackageSwitchMinute.

        :return: The package_switch_uuid of this PackageSwitchMinute.
        :rtype: str
        """
        return self._package_switch_uuid

    @package_switch_uuid.setter
    def package_switch_uuid(self, package_switch_uuid):
        """
        Sets the package_switch_uuid of this PackageSwitchMinute.

        :param package_switch_uuid: The package_switch_uuid of this PackageSwitchMinute.
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
        if not isinstance(other, PackageSwitchMinute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
