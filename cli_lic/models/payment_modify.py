# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PaymentModify(object):
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
        'type': 'str',
        'paid_time': 'datetime',
        'amount': 'float',
        'license_lrn_uuid': 'str',
        'license_switch_uuid': 'str'
    }

    attribute_map = {
        'type': 'type',
        'paid_time': 'paid_time',
        'amount': 'amount',
        'license_lrn_uuid': 'license_lrn_uuid',
        'license_switch_uuid': 'license_switch_uuid'
    }

    def __init__(self, type='paypal', paid_time=None, amount=None, license_lrn_uuid=None, license_switch_uuid=None):
        """
        PaymentModify - a model defined in Swagger
        """

        self._type = None
        self._paid_time = None
        self._amount = None
        self._license_lrn_uuid = None
        self._license_switch_uuid = None

        if type is not None:
          self.type = type
        if paid_time is not None:
          self.paid_time = paid_time
        if amount is not None:
          self.amount = amount
        if license_lrn_uuid is not None:
          self.license_lrn_uuid = license_lrn_uuid
        if license_switch_uuid is not None:
          self.license_switch_uuid = license_switch_uuid

    @property
    def type(self):
        """
        Gets the type of this PaymentModify.

        :return: The type of this PaymentModify.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PaymentModify.

        :param type: The type of this PaymentModify.
        :type: str
        """
        allowed_values = ["paypal", "strip"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def paid_time(self):
        """
        Gets the paid_time of this PaymentModify.

        :return: The paid_time of this PaymentModify.
        :rtype: datetime
        """
        return self._paid_time

    @paid_time.setter
    def paid_time(self, paid_time):
        """
        Sets the paid_time of this PaymentModify.

        :param paid_time: The paid_time of this PaymentModify.
        :type: datetime
        """

        self._paid_time = paid_time

    @property
    def amount(self):
        """
        Gets the amount of this PaymentModify.

        :return: The amount of this PaymentModify.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PaymentModify.

        :param amount: The amount of this PaymentModify.
        :type: float
        """

        self._amount = amount

    @property
    def license_lrn_uuid(self):
        """
        Gets the license_lrn_uuid of this PaymentModify.

        :return: The license_lrn_uuid of this PaymentModify.
        :rtype: str
        """
        return self._license_lrn_uuid

    @license_lrn_uuid.setter
    def license_lrn_uuid(self, license_lrn_uuid):
        """
        Sets the license_lrn_uuid of this PaymentModify.

        :param license_lrn_uuid: The license_lrn_uuid of this PaymentModify.
        :type: str
        """
        if license_lrn_uuid is not None and len(license_lrn_uuid) > 36:
            raise ValueError("Invalid value for `license_lrn_uuid`, length must be less than or equal to `36`")

        self._license_lrn_uuid = license_lrn_uuid

    @property
    def license_switch_uuid(self):
        """
        Gets the license_switch_uuid of this PaymentModify.

        :return: The license_switch_uuid of this PaymentModify.
        :rtype: str
        """
        return self._license_switch_uuid

    @license_switch_uuid.setter
    def license_switch_uuid(self, license_switch_uuid):
        """
        Sets the license_switch_uuid of this PaymentModify.

        :param license_switch_uuid: The license_switch_uuid of this PaymentModify.
        :type: str
        """
        if license_switch_uuid is not None and len(license_switch_uuid) > 36:
            raise ValueError("Invalid value for `license_switch_uuid`, length must be less than or equal to `36`")

        self._license_switch_uuid = license_switch_uuid

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
        if not isinstance(other, PaymentModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
