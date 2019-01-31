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
        'end_time': 'datetime',
        'start_time': 'datetime',
        'package_switch_uuid': 'str',
        'user_uuid': 'str',
        'enabled': 'bool',
        'user_email': 'str',
        'type': 'int',
        'license_switch_uuid': 'str',
        'switch_port': 'int',
        'package': 'PackageSwitch',
        'ip': 'str',
        'ordered_amount': 'int',
        'minute_count': 'int',
        'amount': 'int'
    }

    attribute_map = {
        'end_time': 'end_time',
        'start_time': 'start_time',
        'package_switch_uuid': 'package_switch_uuid',
        'user_uuid': 'user_uuid',
        'enabled': 'enabled',
        'user_email': 'user_email',
        'type': 'type',
        'license_switch_uuid': 'license_switch_uuid',
        'switch_port': 'switch_port',
        'package': 'package',
        'ip': 'ip',
        'ordered_amount': 'ordered_amount',
        'minute_count': 'minute_count',
        'amount': 'amount'
    }

    def __init__(self, end_time=None, start_time=None, package_switch_uuid=None, user_uuid=None, enabled=None, user_email=None, type=None, license_switch_uuid=None, switch_port=None, package=None, ip=None, ordered_amount=None, minute_count=None, amount=None):
        """
        LicenseSwitchGet - a model defined in Swagger
        """

        self._end_time = None
        self._start_time = None
        self._package_switch_uuid = None
        self._user_uuid = None
        self._enabled = None
        self._user_email = None
        self._type = None
        self._license_switch_uuid = None
        self._switch_port = None
        self._package = None
        self._ip = None
        self._ordered_amount = None
        self._minute_count = None
        self._amount = None

        if end_time is not None:
          self.end_time = end_time
        if start_time is not None:
          self.start_time = start_time
        if package_switch_uuid is not None:
          self.package_switch_uuid = package_switch_uuid
        if user_uuid is not None:
          self.user_uuid = user_uuid
        if enabled is not None:
          self.enabled = enabled
        if user_email is not None:
          self.user_email = user_email
        if type is not None:
          self.type = type
        if license_switch_uuid is not None:
          self.license_switch_uuid = license_switch_uuid
        if switch_port is not None:
          self.switch_port = switch_port
        if package is not None:
          self.package = package
        self.ip = ip
        if ordered_amount is not None:
          self.ordered_amount = ordered_amount
        if minute_count is not None:
          self.minute_count = minute_count
        if amount is not None:
          self.amount = amount

    @property
    def end_time(self):
        """
        Gets the end_time of this LicenseSwitchGet.

        :return: The end_time of this LicenseSwitchGet.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this LicenseSwitchGet.

        :param end_time: The end_time of this LicenseSwitchGet.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def start_time(self):
        """
        Gets the start_time of this LicenseSwitchGet.

        :return: The start_time of this LicenseSwitchGet.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this LicenseSwitchGet.

        :param start_time: The start_time of this LicenseSwitchGet.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def package_switch_uuid(self):
        """
        Gets the package_switch_uuid of this LicenseSwitchGet.

        :return: The package_switch_uuid of this LicenseSwitchGet.
        :rtype: str
        """
        return self._package_switch_uuid

    @package_switch_uuid.setter
    def package_switch_uuid(self, package_switch_uuid):
        """
        Sets the package_switch_uuid of this LicenseSwitchGet.

        :param package_switch_uuid: The package_switch_uuid of this LicenseSwitchGet.
        :type: str
        """
        if package_switch_uuid is not None and len(package_switch_uuid) > 36:
            raise ValueError("Invalid value for `package_switch_uuid`, length must be less than or equal to `36`")

        self._package_switch_uuid = package_switch_uuid

    @property
    def user_uuid(self):
        """
        Gets the user_uuid of this LicenseSwitchGet.

        :return: The user_uuid of this LicenseSwitchGet.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """
        Sets the user_uuid of this LicenseSwitchGet.

        :param user_uuid: The user_uuid of this LicenseSwitchGet.
        :type: str
        """
        if user_uuid is not None and len(user_uuid) > 36:
            raise ValueError("Invalid value for `user_uuid`, length must be less than or equal to `36`")

        self._user_uuid = user_uuid

    @property
    def enabled(self):
        """
        Gets the enabled of this LicenseSwitchGet.

        :return: The enabled of this LicenseSwitchGet.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this LicenseSwitchGet.

        :param enabled: The enabled of this LicenseSwitchGet.
        :type: bool
        """

        self._enabled = enabled

    @property
    def user_email(self):
        """
        Gets the user_email of this LicenseSwitchGet.

        :return: The user_email of this LicenseSwitchGet.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """
        Sets the user_email of this LicenseSwitchGet.

        :param user_email: The user_email of this LicenseSwitchGet.
        :type: str
        """
        if user_email is not None and len(user_email) > 128:
            raise ValueError("Invalid value for `user_email`, length must be less than or equal to `128`")

        self._user_email = user_email

    @property
    def type(self):
        """
        Gets the type of this LicenseSwitchGet.

        :return: The type of this LicenseSwitchGet.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LicenseSwitchGet.

        :param type: The type of this LicenseSwitchGet.
        :type: int
        """

        self._type = type

    @property
    def license_switch_uuid(self):
        """
        Gets the license_switch_uuid of this LicenseSwitchGet.

        :return: The license_switch_uuid of this LicenseSwitchGet.
        :rtype: str
        """
        return self._license_switch_uuid

    @license_switch_uuid.setter
    def license_switch_uuid(self, license_switch_uuid):
        """
        Sets the license_switch_uuid of this LicenseSwitchGet.

        :param license_switch_uuid: The license_switch_uuid of this LicenseSwitchGet.
        :type: str
        """
        if license_switch_uuid is not None and len(license_switch_uuid) > 36:
            raise ValueError("Invalid value for `license_switch_uuid`, length must be less than or equal to `36`")

        self._license_switch_uuid = license_switch_uuid

    @property
    def switch_port(self):
        """
        Gets the switch_port of this LicenseSwitchGet.

        :return: The switch_port of this LicenseSwitchGet.
        :rtype: int
        """
        return self._switch_port

    @switch_port.setter
    def switch_port(self, switch_port):
        """
        Sets the switch_port of this LicenseSwitchGet.

        :param switch_port: The switch_port of this LicenseSwitchGet.
        :type: int
        """

        self._switch_port = switch_port

    @property
    def package(self):
        """
        Gets the package of this LicenseSwitchGet.

        :return: The package of this LicenseSwitchGet.
        :rtype: PackageSwitch
        """
        return self._package

    @package.setter
    def package(self, package):
        """
        Sets the package of this LicenseSwitchGet.

        :param package: The package of this LicenseSwitchGet.
        :type: PackageSwitch
        """

        self._package = package

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
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")
        if ip is not None and len(ip) > 16:
            raise ValueError("Invalid value for `ip`, length must be less than or equal to `16`")

        self._ip = ip

    @property
    def ordered_amount(self):
        """
        Gets the ordered_amount of this LicenseSwitchGet.

        :return: The ordered_amount of this LicenseSwitchGet.
        :rtype: int
        """
        return self._ordered_amount

    @ordered_amount.setter
    def ordered_amount(self, ordered_amount):
        """
        Sets the ordered_amount of this LicenseSwitchGet.

        :param ordered_amount: The ordered_amount of this LicenseSwitchGet.
        :type: int
        """

        self._ordered_amount = ordered_amount

    @property
    def minute_count(self):
        """
        Gets the minute_count of this LicenseSwitchGet.

        :return: The minute_count of this LicenseSwitchGet.
        :rtype: int
        """
        return self._minute_count

    @minute_count.setter
    def minute_count(self, minute_count):
        """
        Sets the minute_count of this LicenseSwitchGet.

        :param minute_count: The minute_count of this LicenseSwitchGet.
        :type: int
        """

        self._minute_count = minute_count

    @property
    def amount(self):
        """
        Gets the amount of this LicenseSwitchGet.

        :return: The amount of this LicenseSwitchGet.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this LicenseSwitchGet.

        :param amount: The amount of this LicenseSwitchGet.
        :type: int
        """

        self._amount = amount

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
