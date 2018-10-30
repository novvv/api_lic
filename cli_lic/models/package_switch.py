# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PackageSwitch(object):
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
        'amount': 'int',
        'switch_uuid': 'str',
        'enabled': 'bool',
        'package_name': 'str',
        'type': 'str',
        'minute_count': 'int',
        'switch_port': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'switch_uuid': 'switch_uuid',
        'enabled': 'enabled',
        'package_name': 'package_name',
        'type': 'type',
        'minute_count': 'minute_count',
        'switch_port': 'switch_port'
    }

    def __init__(self, amount=None, switch_uuid=None, enabled=None, package_name=None, type='switch pay per port', minute_count=None, switch_port=None):
        """
        PackageSwitch - a model defined in Swagger
        """

        self._amount = None
        self._switch_uuid = None
        self._enabled = None
        self._package_name = None
        self._type = None
        self._minute_count = None
        self._switch_port = None

        if amount is not None:
          self.amount = amount
        if switch_uuid is not None:
          self.switch_uuid = switch_uuid
        if enabled is not None:
          self.enabled = enabled
        if package_name is not None:
          self.package_name = package_name
        if type is not None:
          self.type = type
        if minute_count is not None:
          self.minute_count = minute_count
        if switch_port is not None:
          self.switch_port = switch_port

    @property
    def amount(self):
        """
        Gets the amount of this PackageSwitch.

        :return: The amount of this PackageSwitch.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PackageSwitch.

        :param amount: The amount of this PackageSwitch.
        :type: int
        """

        self._amount = amount

    @property
    def switch_uuid(self):
        """
        Gets the switch_uuid of this PackageSwitch.

        :return: The switch_uuid of this PackageSwitch.
        :rtype: str
        """
        return self._switch_uuid

    @switch_uuid.setter
    def switch_uuid(self, switch_uuid):
        """
        Sets the switch_uuid of this PackageSwitch.

        :param switch_uuid: The switch_uuid of this PackageSwitch.
        :type: str
        """
        if switch_uuid is not None and len(switch_uuid) > 36:
            raise ValueError("Invalid value for `switch_uuid`, length must be less than or equal to `36`")

        self._switch_uuid = switch_uuid

    @property
    def enabled(self):
        """
        Gets the enabled of this PackageSwitch.

        :return: The enabled of this PackageSwitch.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this PackageSwitch.

        :param enabled: The enabled of this PackageSwitch.
        :type: bool
        """

        self._enabled = enabled

    @property
    def package_name(self):
        """
        Gets the package_name of this PackageSwitch.

        :return: The package_name of this PackageSwitch.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """
        Sets the package_name of this PackageSwitch.

        :param package_name: The package_name of this PackageSwitch.
        :type: str
        """
        if package_name is not None and len(package_name) > 64:
            raise ValueError("Invalid value for `package_name`, length must be less than or equal to `64`")

        self._package_name = package_name

    @property
    def type(self):
        """
        Gets the type of this PackageSwitch.

        :return: The type of this PackageSwitch.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PackageSwitch.

        :param type: The type of this PackageSwitch.
        :type: str
        """
        allowed_values = ["switch pay per port", "switch pay per minute"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def minute_count(self):
        """
        Gets the minute_count of this PackageSwitch.

        :return: The minute_count of this PackageSwitch.
        :rtype: int
        """
        return self._minute_count

    @minute_count.setter
    def minute_count(self, minute_count):
        """
        Sets the minute_count of this PackageSwitch.

        :param minute_count: The minute_count of this PackageSwitch.
        :type: int
        """

        self._minute_count = minute_count

    @property
    def switch_port(self):
        """
        Gets the switch_port of this PackageSwitch.

        :return: The switch_port of this PackageSwitch.
        :rtype: int
        """
        return self._switch_port

    @switch_port.setter
    def switch_port(self, switch_port):
        """
        Sets the switch_port of this PackageSwitch.

        :param switch_port: The switch_port of this PackageSwitch.
        :type: int
        """

        self._switch_port = switch_port

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
        if not isinstance(other, PackageSwitch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
