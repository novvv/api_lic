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


class PaymentGet(object):
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
        'amount_switch': 'float',
        'type': 'str',
        'payment_uuid': 'str',
        'switch_uuid': 'str',
        'description': 'str',
        'paid_time': 'datetime',
        'license_switch_uuid': 'str',
        'amount_total': 'str',
        'license_lrn_uuid': 'str',
        'amount_lrn': 'float',
        'switch_package_name': 'str',
        'user_uuid': 'str',
        'lrn_package_name': 'str',
        'user_email': 'str'
    }

    attribute_map = {
        'amount_switch': 'amount_switch',
        'type': 'type',
        'payment_uuid': 'payment_uuid',
        'switch_uuid': 'switch_uuid',
        'description': 'description',
        'paid_time': 'paid_time',
        'license_switch_uuid': 'license_switch_uuid',
        'amount_total': 'amount_total',
        'license_lrn_uuid': 'license_lrn_uuid',
        'amount_lrn': 'amount_lrn',
        'switch_package_name': 'switch_package_name',
        'user_uuid': 'user_uuid',
        'lrn_package_name': 'lrn_package_name',
        'user_email': 'user_email'
    }

    def __init__(self, amount_switch=None, type='paypal', payment_uuid=None, switch_uuid=None, description=None, paid_time=None, license_switch_uuid=None, amount_total=None, license_lrn_uuid=None, amount_lrn=None, switch_package_name=None, user_uuid=None, lrn_package_name=None, user_email=None):
        """
        PaymentGet - a model defined in Swagger
        """

        self._amount_switch = None
        self._type = None
        self._payment_uuid = None
        self._switch_uuid = None
        self._description = None
        self._paid_time = None
        self._license_switch_uuid = None
        self._amount_total = None
        self._license_lrn_uuid = None
        self._amount_lrn = None
        self._switch_package_name = None
        self._user_uuid = None
        self._lrn_package_name = None
        self._user_email = None

        if amount_switch is not None:
          self.amount_switch = amount_switch
        if type is not None:
          self.type = type
        if payment_uuid is not None:
          self.payment_uuid = payment_uuid
        if switch_uuid is not None:
          self.switch_uuid = switch_uuid
        if description is not None:
          self.description = description
        if paid_time is not None:
          self.paid_time = paid_time
        if license_switch_uuid is not None:
          self.license_switch_uuid = license_switch_uuid
        if amount_total is not None:
          self.amount_total = amount_total
        if license_lrn_uuid is not None:
          self.license_lrn_uuid = license_lrn_uuid
        if amount_lrn is not None:
          self.amount_lrn = amount_lrn
        if switch_package_name is not None:
          self.switch_package_name = switch_package_name
        if user_uuid is not None:
          self.user_uuid = user_uuid
        if lrn_package_name is not None:
          self.lrn_package_name = lrn_package_name
        if user_email is not None:
          self.user_email = user_email

    @property
    def amount_switch(self):
        """
        Gets the amount_switch of this PaymentGet.

        :return: The amount_switch of this PaymentGet.
        :rtype: float
        """
        return self._amount_switch

    @amount_switch.setter
    def amount_switch(self, amount_switch):
        """
        Sets the amount_switch of this PaymentGet.

        :param amount_switch: The amount_switch of this PaymentGet.
        :type: float
        """

        self._amount_switch = amount_switch

    @property
    def type(self):
        """
        Gets the type of this PaymentGet.

        :return: The type of this PaymentGet.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PaymentGet.

        :param type: The type of this PaymentGet.
        :type: str
        """
        allowed_values = ["paypal", "stripe"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def payment_uuid(self):
        """
        Gets the payment_uuid of this PaymentGet.

        :return: The payment_uuid of this PaymentGet.
        :rtype: str
        """
        return self._payment_uuid

    @payment_uuid.setter
    def payment_uuid(self, payment_uuid):
        """
        Sets the payment_uuid of this PaymentGet.

        :param payment_uuid: The payment_uuid of this PaymentGet.
        :type: str
        """
        if payment_uuid is not None and len(payment_uuid) > 36:
            raise ValueError("Invalid value for `payment_uuid`, length must be less than or equal to `36`")

        self._payment_uuid = payment_uuid

    @property
    def switch_uuid(self):
        """
        Gets the switch_uuid of this PaymentGet.

        :return: The switch_uuid of this PaymentGet.
        :rtype: str
        """
        return self._switch_uuid

    @switch_uuid.setter
    def switch_uuid(self, switch_uuid):
        """
        Sets the switch_uuid of this PaymentGet.

        :param switch_uuid: The switch_uuid of this PaymentGet.
        :type: str
        """
        if switch_uuid is not None and len(switch_uuid) > 64:
            raise ValueError("Invalid value for `switch_uuid`, length must be less than or equal to `64`")

        self._switch_uuid = switch_uuid

    @property
    def description(self):
        """
        Gets the description of this PaymentGet.

        :return: The description of this PaymentGet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PaymentGet.

        :param description: The description of this PaymentGet.
        :type: str
        """

        self._description = description

    @property
    def paid_time(self):
        """
        Gets the paid_time of this PaymentGet.

        :return: The paid_time of this PaymentGet.
        :rtype: datetime
        """
        return self._paid_time

    @paid_time.setter
    def paid_time(self, paid_time):
        """
        Sets the paid_time of this PaymentGet.

        :param paid_time: The paid_time of this PaymentGet.
        :type: datetime
        """

        self._paid_time = paid_time

    @property
    def license_switch_uuid(self):
        """
        Gets the license_switch_uuid of this PaymentGet.

        :return: The license_switch_uuid of this PaymentGet.
        :rtype: str
        """
        return self._license_switch_uuid

    @license_switch_uuid.setter
    def license_switch_uuid(self, license_switch_uuid):
        """
        Sets the license_switch_uuid of this PaymentGet.

        :param license_switch_uuid: The license_switch_uuid of this PaymentGet.
        :type: str
        """
        if license_switch_uuid is not None and len(license_switch_uuid) > 36:
            raise ValueError("Invalid value for `license_switch_uuid`, length must be less than or equal to `36`")

        self._license_switch_uuid = license_switch_uuid

    @property
    def amount_total(self):
        """
        Gets the amount_total of this PaymentGet.

        :return: The amount_total of this PaymentGet.
        :rtype: str
        """
        return self._amount_total

    @amount_total.setter
    def amount_total(self, amount_total):
        """
        Sets the amount_total of this PaymentGet.

        :param amount_total: The amount_total of this PaymentGet.
        :type: str
        """

        self._amount_total = amount_total

    @property
    def license_lrn_uuid(self):
        """
        Gets the license_lrn_uuid of this PaymentGet.

        :return: The license_lrn_uuid of this PaymentGet.
        :rtype: str
        """
        return self._license_lrn_uuid

    @license_lrn_uuid.setter
    def license_lrn_uuid(self, license_lrn_uuid):
        """
        Sets the license_lrn_uuid of this PaymentGet.

        :param license_lrn_uuid: The license_lrn_uuid of this PaymentGet.
        :type: str
        """
        if license_lrn_uuid is not None and len(license_lrn_uuid) > 36:
            raise ValueError("Invalid value for `license_lrn_uuid`, length must be less than or equal to `36`")

        self._license_lrn_uuid = license_lrn_uuid

    @property
    def amount_lrn(self):
        """
        Gets the amount_lrn of this PaymentGet.

        :return: The amount_lrn of this PaymentGet.
        :rtype: float
        """
        return self._amount_lrn

    @amount_lrn.setter
    def amount_lrn(self, amount_lrn):
        """
        Sets the amount_lrn of this PaymentGet.

        :param amount_lrn: The amount_lrn of this PaymentGet.
        :type: float
        """

        self._amount_lrn = amount_lrn

    @property
    def switch_package_name(self):
        """
        Gets the switch_package_name of this PaymentGet.

        :return: The switch_package_name of this PaymentGet.
        :rtype: str
        """
        return self._switch_package_name

    @switch_package_name.setter
    def switch_package_name(self, switch_package_name):
        """
        Sets the switch_package_name of this PaymentGet.

        :param switch_package_name: The switch_package_name of this PaymentGet.
        :type: str
        """

        self._switch_package_name = switch_package_name

    @property
    def user_uuid(self):
        """
        Gets the user_uuid of this PaymentGet.

        :return: The user_uuid of this PaymentGet.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """
        Sets the user_uuid of this PaymentGet.

        :param user_uuid: The user_uuid of this PaymentGet.
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def lrn_package_name(self):
        """
        Gets the lrn_package_name of this PaymentGet.

        :return: The lrn_package_name of this PaymentGet.
        :rtype: str
        """
        return self._lrn_package_name

    @lrn_package_name.setter
    def lrn_package_name(self, lrn_package_name):
        """
        Sets the lrn_package_name of this PaymentGet.

        :param lrn_package_name: The lrn_package_name of this PaymentGet.
        :type: str
        """

        self._lrn_package_name = lrn_package_name

    @property
    def user_email(self):
        """
        Gets the user_email of this PaymentGet.

        :return: The user_email of this PaymentGet.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """
        Sets the user_email of this PaymentGet.

        :param user_email: The user_email of this PaymentGet.
        :type: str
        """

        self._user_email = user_email

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
        if not isinstance(other, PaymentGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
