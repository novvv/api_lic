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


class LicenseSwitchModify(object):
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
        'end_time': 'datetime',
        'cost': 'float',
        'user_uuid': 'str',
        'package_switch_uuid': 'str',
        'plan_uuid': 'str',
        'ordered_amount': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'cost': 'cost',
        'user_uuid': 'user_uuid',
        'package_switch_uuid': 'package_switch_uuid',
        'plan_uuid': 'plan_uuid',
        'ordered_amount': 'ordered_amount'
    }

    def __init__(self, start_time=None, end_time=None, cost=None, user_uuid=None, package_switch_uuid=None, plan_uuid=None, ordered_amount=None):
        """
        LicenseSwitchModify - a model defined in Swagger
        """

        self._start_time = None
        self._end_time = None
        self._cost = None
        self._user_uuid = None
        self._package_switch_uuid = None
        self._plan_uuid = None
        self._ordered_amount = None

        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if cost is not None:
          self.cost = cost
        if user_uuid is not None:
          self.user_uuid = user_uuid
        if package_switch_uuid is not None:
          self.package_switch_uuid = package_switch_uuid
        if plan_uuid is not None:
          self.plan_uuid = plan_uuid
        if ordered_amount is not None:
          self.ordered_amount = ordered_amount

    @property
    def start_time(self):
        """
        Gets the start_time of this LicenseSwitchModify.

        :return: The start_time of this LicenseSwitchModify.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this LicenseSwitchModify.

        :param start_time: The start_time of this LicenseSwitchModify.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this LicenseSwitchModify.

        :return: The end_time of this LicenseSwitchModify.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this LicenseSwitchModify.

        :param end_time: The end_time of this LicenseSwitchModify.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def cost(self):
        """
        Gets the cost of this LicenseSwitchModify.

        :return: The cost of this LicenseSwitchModify.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this LicenseSwitchModify.

        :param cost: The cost of this LicenseSwitchModify.
        :type: float
        """

        self._cost = cost

    @property
    def user_uuid(self):
        """
        Gets the user_uuid of this LicenseSwitchModify.

        :return: The user_uuid of this LicenseSwitchModify.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """
        Sets the user_uuid of this LicenseSwitchModify.

        :param user_uuid: The user_uuid of this LicenseSwitchModify.
        :type: str
        """
        if user_uuid is not None and len(user_uuid) > 36:
            raise ValueError("Invalid value for `user_uuid`, length must be less than or equal to `36`")

        self._user_uuid = user_uuid

    @property
    def package_switch_uuid(self):
        """
        Gets the package_switch_uuid of this LicenseSwitchModify.

        :return: The package_switch_uuid of this LicenseSwitchModify.
        :rtype: str
        """
        return self._package_switch_uuid

    @package_switch_uuid.setter
    def package_switch_uuid(self, package_switch_uuid):
        """
        Sets the package_switch_uuid of this LicenseSwitchModify.

        :param package_switch_uuid: The package_switch_uuid of this LicenseSwitchModify.
        :type: str
        """
        if package_switch_uuid is not None and len(package_switch_uuid) > 36:
            raise ValueError("Invalid value for `package_switch_uuid`, length must be less than or equal to `36`")

        self._package_switch_uuid = package_switch_uuid

    @property
    def plan_uuid(self):
        """
        Gets the plan_uuid of this LicenseSwitchModify.

        :return: The plan_uuid of this LicenseSwitchModify.
        :rtype: str
        """
        return self._plan_uuid

    @plan_uuid.setter
    def plan_uuid(self, plan_uuid):
        """
        Sets the plan_uuid of this LicenseSwitchModify.

        :param plan_uuid: The plan_uuid of this LicenseSwitchModify.
        :type: str
        """
        if plan_uuid is not None and len(plan_uuid) > 36:
            raise ValueError("Invalid value for `plan_uuid`, length must be less than or equal to `36`")

        self._plan_uuid = plan_uuid

    @property
    def ordered_amount(self):
        """
        Gets the ordered_amount of this LicenseSwitchModify.

        :return: The ordered_amount of this LicenseSwitchModify.
        :rtype: int
        """
        return self._ordered_amount

    @ordered_amount.setter
    def ordered_amount(self, ordered_amount):
        """
        Sets the ordered_amount of this LicenseSwitchModify.

        :param ordered_amount: The ordered_amount of this LicenseSwitchModify.
        :type: int
        """

        self._ordered_amount = ordered_amount

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
        if not isinstance(other, LicenseSwitchModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
