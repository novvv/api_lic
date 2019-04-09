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


class PackageLrnGet(object):
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
        'dip_count': 'int',
        'package_lrn_uuid': 'str',
        'package_name': 'str',
        'create_on': 'datetime',
        'type': 'str',
        'lrn_port': 'int',
        'cps': 'int',
        'amount': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'dip_count': 'dip_count',
        'package_lrn_uuid': 'package_lrn_uuid',
        'package_name': 'package_name',
        'create_on': 'create_on',
        'type': 'type',
        'lrn_port': 'lrn_port',
        'cps': 'cps',
        'amount': 'amount'
    }

    def __init__(self, enabled=None, dip_count=None, package_lrn_uuid=None, package_name=None, create_on=None, type='LRN pay per CPS', lrn_port=None, cps=None, amount=None):
        """
        PackageLrnGet - a model defined in Swagger
        """

        self._enabled = None
        self._dip_count = None
        self._package_lrn_uuid = None
        self._package_name = None
        self._create_on = None
        self._type = None
        self._lrn_port = None
        self._cps = None
        self._amount = None

        if enabled is not None:
          self.enabled = enabled
        if dip_count is not None:
          self.dip_count = dip_count
        if package_lrn_uuid is not None:
          self.package_lrn_uuid = package_lrn_uuid
        if package_name is not None:
          self.package_name = package_name
        if create_on is not None:
          self.create_on = create_on
        if type is not None:
          self.type = type
        if lrn_port is not None:
          self.lrn_port = lrn_port
        if cps is not None:
          self.cps = cps
        if amount is not None:
          self.amount = amount

    @property
    def enabled(self):
        """
        Gets the enabled of this PackageLrnGet.

        :return: The enabled of this PackageLrnGet.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this PackageLrnGet.

        :param enabled: The enabled of this PackageLrnGet.
        :type: bool
        """

        self._enabled = enabled

    @property
    def dip_count(self):
        """
        Gets the dip_count of this PackageLrnGet.

        :return: The dip_count of this PackageLrnGet.
        :rtype: int
        """
        return self._dip_count

    @dip_count.setter
    def dip_count(self, dip_count):
        """
        Sets the dip_count of this PackageLrnGet.

        :param dip_count: The dip_count of this PackageLrnGet.
        :type: int
        """

        self._dip_count = dip_count

    @property
    def package_lrn_uuid(self):
        """
        Gets the package_lrn_uuid of this PackageLrnGet.

        :return: The package_lrn_uuid of this PackageLrnGet.
        :rtype: str
        """
        return self._package_lrn_uuid

    @package_lrn_uuid.setter
    def package_lrn_uuid(self, package_lrn_uuid):
        """
        Sets the package_lrn_uuid of this PackageLrnGet.

        :param package_lrn_uuid: The package_lrn_uuid of this PackageLrnGet.
        :type: str
        """
        if package_lrn_uuid is not None and len(package_lrn_uuid) > 36:
            raise ValueError("Invalid value for `package_lrn_uuid`, length must be less than or equal to `36`")

        self._package_lrn_uuid = package_lrn_uuid

    @property
    def package_name(self):
        """
        Gets the package_name of this PackageLrnGet.

        :return: The package_name of this PackageLrnGet.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """
        Sets the package_name of this PackageLrnGet.

        :param package_name: The package_name of this PackageLrnGet.
        :type: str
        """
        if package_name is not None and len(package_name) > 64:
            raise ValueError("Invalid value for `package_name`, length must be less than or equal to `64`")

        self._package_name = package_name

    @property
    def create_on(self):
        """
        Gets the create_on of this PackageLrnGet.

        :return: The create_on of this PackageLrnGet.
        :rtype: datetime
        """
        return self._create_on

    @create_on.setter
    def create_on(self, create_on):
        """
        Sets the create_on of this PackageLrnGet.

        :param create_on: The create_on of this PackageLrnGet.
        :type: datetime
        """

        self._create_on = create_on

    @property
    def type(self):
        """
        Gets the type of this PackageLrnGet.

        :return: The type of this PackageLrnGet.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PackageLrnGet.

        :param type: The type of this PackageLrnGet.
        :type: str
        """
        allowed_values = ["LRN pay per CPS", "LRN pay per DIP"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def lrn_port(self):
        """
        Gets the lrn_port of this PackageLrnGet.

        :return: The lrn_port of this PackageLrnGet.
        :rtype: int
        """
        return self._lrn_port

    @lrn_port.setter
    def lrn_port(self, lrn_port):
        """
        Sets the lrn_port of this PackageLrnGet.

        :param lrn_port: The lrn_port of this PackageLrnGet.
        :type: int
        """

        self._lrn_port = lrn_port

    @property
    def cps(self):
        """
        Gets the cps of this PackageLrnGet.

        :return: The cps of this PackageLrnGet.
        :rtype: int
        """
        return self._cps

    @cps.setter
    def cps(self, cps):
        """
        Sets the cps of this PackageLrnGet.

        :param cps: The cps of this PackageLrnGet.
        :type: int
        """

        self._cps = cps

    @property
    def amount(self):
        """
        Gets the amount of this PackageLrnGet.

        :return: The amount of this PackageLrnGet.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PackageLrnGet.

        :param amount: The amount of this PackageLrnGet.
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
        if not isinstance(other, PackageLrnGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
