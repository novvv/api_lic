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


class LicenseLrnGet(object):
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
        'license_lrn_uuid': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'ordered_amount': 'int',
        'dip_count': 'int',
        'cps': 'int',
        'ip': 'str',
        'amount': 'int',
        'user_email': 'str',
        'lrn_port': 'int',
        'package': 'PackageLrn',
        'enabled': 'bool',
        'user_uuid': 'str',
        'package_lrn_uuid': 'str',
        'type': 'int'
    }

    attribute_map = {
        'license_lrn_uuid': 'license_lrn_uuid',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'ordered_amount': 'ordered_amount',
        'dip_count': 'dip_count',
        'cps': 'cps',
        'ip': 'ip',
        'amount': 'amount',
        'user_email': 'user_email',
        'lrn_port': 'lrn_port',
        'package': 'package',
        'enabled': 'enabled',
        'user_uuid': 'user_uuid',
        'package_lrn_uuid': 'package_lrn_uuid',
        'type': 'type'
    }

    def __init__(self, license_lrn_uuid=None, start_time=None, end_time=None, ordered_amount=None, dip_count=None, cps=None, ip=None, amount=None, user_email=None, lrn_port=None, package=None, enabled=None, user_uuid=None, package_lrn_uuid=None, type=None):
        """
        LicenseLrnGet - a model defined in Swagger
        """

        self._license_lrn_uuid = None
        self._start_time = None
        self._end_time = None
        self._ordered_amount = None
        self._dip_count = None
        self._cps = None
        self._ip = None
        self._amount = None
        self._user_email = None
        self._lrn_port = None
        self._package = None
        self._enabled = None
        self._user_uuid = None
        self._package_lrn_uuid = None
        self._type = None

        if license_lrn_uuid is not None:
          self.license_lrn_uuid = license_lrn_uuid
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if ordered_amount is not None:
          self.ordered_amount = ordered_amount
        if dip_count is not None:
          self.dip_count = dip_count
        if cps is not None:
          self.cps = cps
        self.ip = ip
        if amount is not None:
          self.amount = amount
        if user_email is not None:
          self.user_email = user_email
        if lrn_port is not None:
          self.lrn_port = lrn_port
        if package is not None:
          self.package = package
        if enabled is not None:
          self.enabled = enabled
        if user_uuid is not None:
          self.user_uuid = user_uuid
        if package_lrn_uuid is not None:
          self.package_lrn_uuid = package_lrn_uuid
        if type is not None:
          self.type = type

    @property
    def license_lrn_uuid(self):
        """
        Gets the license_lrn_uuid of this LicenseLrnGet.

        :return: The license_lrn_uuid of this LicenseLrnGet.
        :rtype: str
        """
        return self._license_lrn_uuid

    @license_lrn_uuid.setter
    def license_lrn_uuid(self, license_lrn_uuid):
        """
        Sets the license_lrn_uuid of this LicenseLrnGet.

        :param license_lrn_uuid: The license_lrn_uuid of this LicenseLrnGet.
        :type: str
        """
        if license_lrn_uuid is not None and len(license_lrn_uuid) > 36:
            raise ValueError("Invalid value for `license_lrn_uuid`, length must be less than or equal to `36`")

        self._license_lrn_uuid = license_lrn_uuid

    @property
    def start_time(self):
        """
        Gets the start_time of this LicenseLrnGet.

        :return: The start_time of this LicenseLrnGet.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this LicenseLrnGet.

        :param start_time: The start_time of this LicenseLrnGet.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this LicenseLrnGet.

        :return: The end_time of this LicenseLrnGet.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this LicenseLrnGet.

        :param end_time: The end_time of this LicenseLrnGet.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def ordered_amount(self):
        """
        Gets the ordered_amount of this LicenseLrnGet.

        :return: The ordered_amount of this LicenseLrnGet.
        :rtype: int
        """
        return self._ordered_amount

    @ordered_amount.setter
    def ordered_amount(self, ordered_amount):
        """
        Sets the ordered_amount of this LicenseLrnGet.

        :param ordered_amount: The ordered_amount of this LicenseLrnGet.
        :type: int
        """

        self._ordered_amount = ordered_amount

    @property
    def dip_count(self):
        """
        Gets the dip_count of this LicenseLrnGet.

        :return: The dip_count of this LicenseLrnGet.
        :rtype: int
        """
        return self._dip_count

    @dip_count.setter
    def dip_count(self, dip_count):
        """
        Sets the dip_count of this LicenseLrnGet.

        :param dip_count: The dip_count of this LicenseLrnGet.
        :type: int
        """

        self._dip_count = dip_count

    @property
    def cps(self):
        """
        Gets the cps of this LicenseLrnGet.

        :return: The cps of this LicenseLrnGet.
        :rtype: int
        """
        return self._cps

    @cps.setter
    def cps(self, cps):
        """
        Sets the cps of this LicenseLrnGet.

        :param cps: The cps of this LicenseLrnGet.
        :type: int
        """

        self._cps = cps

    @property
    def ip(self):
        """
        Gets the ip of this LicenseLrnGet.

        :return: The ip of this LicenseLrnGet.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this LicenseLrnGet.

        :param ip: The ip of this LicenseLrnGet.
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")
        if ip is not None and len(ip) > 16:
            raise ValueError("Invalid value for `ip`, length must be less than or equal to `16`")

        self._ip = ip

    @property
    def amount(self):
        """
        Gets the amount of this LicenseLrnGet.

        :return: The amount of this LicenseLrnGet.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this LicenseLrnGet.

        :param amount: The amount of this LicenseLrnGet.
        :type: int
        """

        self._amount = amount

    @property
    def user_email(self):
        """
        Gets the user_email of this LicenseLrnGet.

        :return: The user_email of this LicenseLrnGet.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """
        Sets the user_email of this LicenseLrnGet.

        :param user_email: The user_email of this LicenseLrnGet.
        :type: str
        """
        if user_email is not None and len(user_email) > 128:
            raise ValueError("Invalid value for `user_email`, length must be less than or equal to `128`")

        self._user_email = user_email

    @property
    def lrn_port(self):
        """
        Gets the lrn_port of this LicenseLrnGet.

        :return: The lrn_port of this LicenseLrnGet.
        :rtype: int
        """
        return self._lrn_port

    @lrn_port.setter
    def lrn_port(self, lrn_port):
        """
        Sets the lrn_port of this LicenseLrnGet.

        :param lrn_port: The lrn_port of this LicenseLrnGet.
        :type: int
        """

        self._lrn_port = lrn_port

    @property
    def package(self):
        """
        Gets the package of this LicenseLrnGet.

        :return: The package of this LicenseLrnGet.
        :rtype: PackageLrn
        """
        return self._package

    @package.setter
    def package(self, package):
        """
        Sets the package of this LicenseLrnGet.

        :param package: The package of this LicenseLrnGet.
        :type: PackageLrn
        """

        self._package = package

    @property
    def enabled(self):
        """
        Gets the enabled of this LicenseLrnGet.

        :return: The enabled of this LicenseLrnGet.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this LicenseLrnGet.

        :param enabled: The enabled of this LicenseLrnGet.
        :type: bool
        """

        self._enabled = enabled

    @property
    def user_uuid(self):
        """
        Gets the user_uuid of this LicenseLrnGet.

        :return: The user_uuid of this LicenseLrnGet.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """
        Sets the user_uuid of this LicenseLrnGet.

        :param user_uuid: The user_uuid of this LicenseLrnGet.
        :type: str
        """
        if user_uuid is not None and len(user_uuid) > 36:
            raise ValueError("Invalid value for `user_uuid`, length must be less than or equal to `36`")

        self._user_uuid = user_uuid

    @property
    def package_lrn_uuid(self):
        """
        Gets the package_lrn_uuid of this LicenseLrnGet.

        :return: The package_lrn_uuid of this LicenseLrnGet.
        :rtype: str
        """
        return self._package_lrn_uuid

    @package_lrn_uuid.setter
    def package_lrn_uuid(self, package_lrn_uuid):
        """
        Sets the package_lrn_uuid of this LicenseLrnGet.

        :param package_lrn_uuid: The package_lrn_uuid of this LicenseLrnGet.
        :type: str
        """
        if package_lrn_uuid is not None and len(package_lrn_uuid) > 36:
            raise ValueError("Invalid value for `package_lrn_uuid`, length must be less than or equal to `36`")

        self._package_lrn_uuid = package_lrn_uuid

    @property
    def type(self):
        """
        Gets the type of this LicenseLrnGet.

        :return: The type of this LicenseLrnGet.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LicenseLrnGet.

        :param type: The type of this LicenseLrnGet.
        :type: int
        """

        self._type = type

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
        if not isinstance(other, LicenseLrnGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
