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


class Payment(object):
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
        'switch_uuid': 'str',
        'license_lrn_uuid': 'str',
        'paid_time': 'datetime',
        'license_switch_uuid': 'str',
        'type': 'str',
        'amount_lrn': 'float'
    }

    attribute_map = {
        'amount_switch': 'amount_switch',
        'switch_uuid': 'switch_uuid',
        'license_lrn_uuid': 'license_lrn_uuid',
        'paid_time': 'paid_time',
        'license_switch_uuid': 'license_switch_uuid',
        'type': 'type',
        'amount_lrn': 'amount_lrn'
    }

    def __init__(self, amount_switch=None, switch_uuid=None, license_lrn_uuid=None, paid_time=None, license_switch_uuid=None, type='paypal', amount_lrn=None):
        """
        Payment - a model defined in Swagger
        """

        self._amount_switch = None
        self._switch_uuid = None
        self._license_lrn_uuid = None
        self._paid_time = None
        self._license_switch_uuid = None
        self._type = None
        self._amount_lrn = None

        if amount_switch is not None:
          self.amount_switch = amount_switch
        if switch_uuid is not None:
          self.switch_uuid = switch_uuid
        if license_lrn_uuid is not None:
          self.license_lrn_uuid = license_lrn_uuid
        if paid_time is not None:
          self.paid_time = paid_time
        if license_switch_uuid is not None:
          self.license_switch_uuid = license_switch_uuid
        if type is not None:
          self.type = type
        if amount_lrn is not None:
          self.amount_lrn = amount_lrn

    @property
    def amount_switch(self):
        """
        Gets the amount_switch of this Payment.

        :return: The amount_switch of this Payment.
        :rtype: float
        """
        return self._amount_switch

    @amount_switch.setter
    def amount_switch(self, amount_switch):
        """
        Sets the amount_switch of this Payment.

        :param amount_switch: The amount_switch of this Payment.
        :type: float
        """

        self._amount_switch = amount_switch

    @property
    def switch_uuid(self):
        """
        Gets the switch_uuid of this Payment.

        :return: The switch_uuid of this Payment.
        :rtype: str
        """
        return self._switch_uuid

    @switch_uuid.setter
    def switch_uuid(self, switch_uuid):
        """
        Sets the switch_uuid of this Payment.

        :param switch_uuid: The switch_uuid of this Payment.
        :type: str
        """
        if switch_uuid is not None and len(switch_uuid) > 64:
            raise ValueError("Invalid value for `switch_uuid`, length must be less than or equal to `64`")

        self._switch_uuid = switch_uuid

    @property
    def license_lrn_uuid(self):
        """
        Gets the license_lrn_uuid of this Payment.

        :return: The license_lrn_uuid of this Payment.
        :rtype: str
        """
        return self._license_lrn_uuid

    @license_lrn_uuid.setter
    def license_lrn_uuid(self, license_lrn_uuid):
        """
        Sets the license_lrn_uuid of this Payment.

        :param license_lrn_uuid: The license_lrn_uuid of this Payment.
        :type: str
        """
        if license_lrn_uuid is not None and len(license_lrn_uuid) > 36:
            raise ValueError("Invalid value for `license_lrn_uuid`, length must be less than or equal to `36`")

        self._license_lrn_uuid = license_lrn_uuid

    @property
    def paid_time(self):
        """
        Gets the paid_time of this Payment.

        :return: The paid_time of this Payment.
        :rtype: datetime
        """
        return self._paid_time

    @paid_time.setter
    def paid_time(self, paid_time):
        """
        Sets the paid_time of this Payment.

        :param paid_time: The paid_time of this Payment.
        :type: datetime
        """

        self._paid_time = paid_time

    @property
    def license_switch_uuid(self):
        """
        Gets the license_switch_uuid of this Payment.

        :return: The license_switch_uuid of this Payment.
        :rtype: str
        """
        return self._license_switch_uuid

    @license_switch_uuid.setter
    def license_switch_uuid(self, license_switch_uuid):
        """
        Sets the license_switch_uuid of this Payment.

        :param license_switch_uuid: The license_switch_uuid of this Payment.
        :type: str
        """
        if license_switch_uuid is not None and len(license_switch_uuid) > 36:
            raise ValueError("Invalid value for `license_switch_uuid`, length must be less than or equal to `36`")

        self._license_switch_uuid = license_switch_uuid

    @property
    def type(self):
        """
        Gets the type of this Payment.

        :return: The type of this Payment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Payment.

        :param type: The type of this Payment.
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
    def amount_lrn(self):
        """
        Gets the amount_lrn of this Payment.

        :return: The amount_lrn of this Payment.
        :rtype: float
        """
        return self._amount_lrn

    @amount_lrn.setter
    def amount_lrn(self, amount_lrn):
        """
        Sets the amount_lrn of this Payment.

        :param amount_lrn: The amount_lrn of this Payment.
        :type: float
        """

        self._amount_lrn = amount_lrn

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
        if not isinstance(other, Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
