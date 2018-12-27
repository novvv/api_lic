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


class PackageSwitchModify(object):
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
        'switch_uuid': 'str',
        'expire_date': 'datetime',
        'sub_type': 'str',
        'enabled': 'bool',
        'start_date': 'datetime',
        'minute_count': 'int',
        'amount': 'int',
        'package_name': 'str',
        'type': 'str',
        'switch_port': 'int'
    }

    attribute_map = {
        'switch_uuid': 'switch_uuid',
        'expire_date': 'expire_date',
        'sub_type': 'sub_type',
        'enabled': 'enabled',
        'start_date': 'start_date',
        'minute_count': 'minute_count',
        'amount': 'amount',
        'package_name': 'package_name',
        'type': 'type',
        'switch_port': 'switch_port'
    }

    def __init__(self, switch_uuid=None, expire_date=None, sub_type='hosted_switch', enabled=None, start_date=None, minute_count=None, amount=None, package_name=None, type='switch pay per port', switch_port=None):
        """
        PackageSwitchModify - a model defined in Swagger
        """

        self._switch_uuid = None
        self._expire_date = None
        self._sub_type = None
        self._enabled = None
        self._start_date = None
        self._minute_count = None
        self._amount = None
        self._package_name = None
        self._type = None
        self._switch_port = None

        if switch_uuid is not None:
          self.switch_uuid = switch_uuid
        if expire_date is not None:
          self.expire_date = expire_date
        if sub_type is not None:
          self.sub_type = sub_type
        if enabled is not None:
          self.enabled = enabled
        if start_date is not None:
          self.start_date = start_date
        if minute_count is not None:
          self.minute_count = minute_count
        if amount is not None:
          self.amount = amount
        if package_name is not None:
          self.package_name = package_name
        if type is not None:
          self.type = type
        if switch_port is not None:
          self.switch_port = switch_port

    @property
    def switch_uuid(self):
        """
        Gets the switch_uuid of this PackageSwitchModify.

        :return: The switch_uuid of this PackageSwitchModify.
        :rtype: str
        """
        return self._switch_uuid

    @switch_uuid.setter
    def switch_uuid(self, switch_uuid):
        """
        Sets the switch_uuid of this PackageSwitchModify.

        :param switch_uuid: The switch_uuid of this PackageSwitchModify.
        :type: str
        """
        if switch_uuid is not None and len(switch_uuid) > 64:
            raise ValueError("Invalid value for `switch_uuid`, length must be less than or equal to `64`")

        self._switch_uuid = switch_uuid

    @property
    def expire_date(self):
        """
        Gets the expire_date of this PackageSwitchModify.

        :return: The expire_date of this PackageSwitchModify.
        :rtype: datetime
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """
        Sets the expire_date of this PackageSwitchModify.

        :param expire_date: The expire_date of this PackageSwitchModify.
        :type: datetime
        """

        self._expire_date = expire_date

    @property
    def sub_type(self):
        """
        Gets the sub_type of this PackageSwitchModify.

        :return: The sub_type of this PackageSwitchModify.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """
        Sets the sub_type of this PackageSwitchModify.

        :param sub_type: The sub_type of this PackageSwitchModify.
        :type: str
        """
        allowed_values = ["hosted_switch", "on_premise", "one_time"]
        if sub_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sub_type` ({0}), must be one of {1}"
                .format(sub_type, allowed_values)
            )

        self._sub_type = sub_type

    @property
    def enabled(self):
        """
        Gets the enabled of this PackageSwitchModify.

        :return: The enabled of this PackageSwitchModify.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this PackageSwitchModify.

        :param enabled: The enabled of this PackageSwitchModify.
        :type: bool
        """

        self._enabled = enabled

    @property
    def start_date(self):
        """
        Gets the start_date of this PackageSwitchModify.

        :return: The start_date of this PackageSwitchModify.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this PackageSwitchModify.

        :param start_date: The start_date of this PackageSwitchModify.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def minute_count(self):
        """
        Gets the minute_count of this PackageSwitchModify.

        :return: The minute_count of this PackageSwitchModify.
        :rtype: int
        """
        return self._minute_count

    @minute_count.setter
    def minute_count(self, minute_count):
        """
        Sets the minute_count of this PackageSwitchModify.

        :param minute_count: The minute_count of this PackageSwitchModify.
        :type: int
        """

        self._minute_count = minute_count

    @property
    def amount(self):
        """
        Gets the amount of this PackageSwitchModify.

        :return: The amount of this PackageSwitchModify.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PackageSwitchModify.

        :param amount: The amount of this PackageSwitchModify.
        :type: int
        """

        self._amount = amount

    @property
    def package_name(self):
        """
        Gets the package_name of this PackageSwitchModify.

        :return: The package_name of this PackageSwitchModify.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """
        Sets the package_name of this PackageSwitchModify.

        :param package_name: The package_name of this PackageSwitchModify.
        :type: str
        """
        if package_name is not None and len(package_name) > 64:
            raise ValueError("Invalid value for `package_name`, length must be less than or equal to `64`")

        self._package_name = package_name

    @property
    def type(self):
        """
        Gets the type of this PackageSwitchModify.

        :return: The type of this PackageSwitchModify.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PackageSwitchModify.

        :param type: The type of this PackageSwitchModify.
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
    def switch_port(self):
        """
        Gets the switch_port of this PackageSwitchModify.

        :return: The switch_port of this PackageSwitchModify.
        :rtype: int
        """
        return self._switch_port

    @switch_port.setter
    def switch_port(self, switch_port):
        """
        Sets the switch_port of this PackageSwitchModify.

        :param switch_port: The switch_port of this PackageSwitchModify.
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
        if not isinstance(other, PackageSwitchModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
