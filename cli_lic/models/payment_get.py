# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.4
    
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
        'amount': 'float',
        'license_switch_uuid': 'str',
        'paid_time': 'datetime',
        'payment_uuid': 'str',
        'user_uuid': 'str',
        'license_lrn_uuid': 'str',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'license_switch_uuid': 'license_switch_uuid',
        'paid_time': 'paid_time',
        'payment_uuid': 'payment_uuid',
        'user_uuid': 'user_uuid',
        'license_lrn_uuid': 'license_lrn_uuid',
        'type': 'type'
    }

    def __init__(self, amount=None, license_switch_uuid=None, paid_time=None, payment_uuid=None, user_uuid=None, license_lrn_uuid=None, type='paypal'):
        """
        PaymentGet - a model defined in Swagger
        """

        self._amount = None
        self._license_switch_uuid = None
        self._paid_time = None
        self._payment_uuid = None
        self._user_uuid = None
        self._license_lrn_uuid = None
        self._type = None

        if amount is not None:
          self.amount = amount
        if license_switch_uuid is not None:
          self.license_switch_uuid = license_switch_uuid
        if paid_time is not None:
          self.paid_time = paid_time
        if payment_uuid is not None:
          self.payment_uuid = payment_uuid
        if user_uuid is not None:
          self.user_uuid = user_uuid
        if license_lrn_uuid is not None:
          self.license_lrn_uuid = license_lrn_uuid
        if type is not None:
          self.type = type

    @property
    def amount(self):
        """
        Gets the amount of this PaymentGet.

        :return: The amount of this PaymentGet.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PaymentGet.

        :param amount: The amount of this PaymentGet.
        :type: float
        """

        self._amount = amount

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
        allowed_values = ["paypal", "strip"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

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
        if not isinstance(other, PaymentGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
