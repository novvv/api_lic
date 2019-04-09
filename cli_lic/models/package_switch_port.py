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


class PackageSwitchPort(object):
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
        'rate_per_port': 'float',
        'package_switch_uuid': 'str',
        'amount': 'int',
        'package_name': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'rate_per_port': 'rate_per_port',
        'package_switch_uuid': 'package_switch_uuid',
        'amount': 'amount',
        'package_name': 'package_name'
    }

    def __init__(self, enabled=None, rate_per_port=None, package_switch_uuid=None, amount=None, package_name=None):
        """
        PackageSwitchPort - a model defined in Swagger
        """

        self._enabled = None
        self._rate_per_port = None
        self._package_switch_uuid = None
        self._amount = None
        self._package_name = None

        if enabled is not None:
          self.enabled = enabled
        if rate_per_port is not None:
          self.rate_per_port = rate_per_port
        if package_switch_uuid is not None:
          self.package_switch_uuid = package_switch_uuid
        if amount is not None:
          self.amount = amount
        if package_name is not None:
          self.package_name = package_name

    @property
    def enabled(self):
        """
        Gets the enabled of this PackageSwitchPort.

        :return: The enabled of this PackageSwitchPort.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this PackageSwitchPort.

        :param enabled: The enabled of this PackageSwitchPort.
        :type: bool
        """

        self._enabled = enabled

    @property
    def rate_per_port(self):
        """
        Gets the rate_per_port of this PackageSwitchPort.

        :return: The rate_per_port of this PackageSwitchPort.
        :rtype: float
        """
        return self._rate_per_port

    @rate_per_port.setter
    def rate_per_port(self, rate_per_port):
        """
        Sets the rate_per_port of this PackageSwitchPort.

        :param rate_per_port: The rate_per_port of this PackageSwitchPort.
        :type: float
        """

        self._rate_per_port = rate_per_port

    @property
    def package_switch_uuid(self):
        """
        Gets the package_switch_uuid of this PackageSwitchPort.

        :return: The package_switch_uuid of this PackageSwitchPort.
        :rtype: str
        """
        return self._package_switch_uuid

    @package_switch_uuid.setter
    def package_switch_uuid(self, package_switch_uuid):
        """
        Sets the package_switch_uuid of this PackageSwitchPort.

        :param package_switch_uuid: The package_switch_uuid of this PackageSwitchPort.
        :type: str
        """
        if package_switch_uuid is not None and len(package_switch_uuid) > 36:
            raise ValueError("Invalid value for `package_switch_uuid`, length must be less than or equal to `36`")

        self._package_switch_uuid = package_switch_uuid

    @property
    def amount(self):
        """
        Gets the amount of this PackageSwitchPort.

        :return: The amount of this PackageSwitchPort.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PackageSwitchPort.

        :param amount: The amount of this PackageSwitchPort.
        :type: int
        """

        self._amount = amount

    @property
    def package_name(self):
        """
        Gets the package_name of this PackageSwitchPort.

        :return: The package_name of this PackageSwitchPort.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """
        Sets the package_name of this PackageSwitchPort.

        :param package_name: The package_name of this PackageSwitchPort.
        :type: str
        """
        if package_name is not None and len(package_name) > 64:
            raise ValueError("Invalid value for `package_name`, length must be less than or equal to `64`")

        self._package_name = package_name

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
        if not isinstance(other, PackageSwitchPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
