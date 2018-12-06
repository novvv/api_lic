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


class UserInfo(object):
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
        'alert_license_expired': 'bool',
        'alert_license_will_expired': 'bool',
        'passwd': 'str',
        'email': 'str',
        'alert_license_purchased': 'bool',
        'alert_payment_received': 'bool'
    }

    attribute_map = {
        'alert_license_expired': 'alert_license_expired',
        'alert_license_will_expired': 'alert_license_will_expired',
        'passwd': 'passwd',
        'email': 'email',
        'alert_license_purchased': 'alert_license_purchased',
        'alert_payment_received': 'alert_payment_received'
    }

    def __init__(self, alert_license_expired=None, alert_license_will_expired=None, passwd=None, email=None, alert_license_purchased=None, alert_payment_received=None):
        """
        UserInfo - a model defined in Swagger
        """

        self._alert_license_expired = None
        self._alert_license_will_expired = None
        self._passwd = None
        self._email = None
        self._alert_license_purchased = None
        self._alert_payment_received = None

        if alert_license_expired is not None:
          self.alert_license_expired = alert_license_expired
        if alert_license_will_expired is not None:
          self.alert_license_will_expired = alert_license_will_expired
        self.passwd = passwd
        if email is not None:
          self.email = email
        if alert_license_purchased is not None:
          self.alert_license_purchased = alert_license_purchased
        if alert_payment_received is not None:
          self.alert_payment_received = alert_payment_received

    @property
    def alert_license_expired(self):
        """
        Gets the alert_license_expired of this UserInfo.

        :return: The alert_license_expired of this UserInfo.
        :rtype: bool
        """
        return self._alert_license_expired

    @alert_license_expired.setter
    def alert_license_expired(self, alert_license_expired):
        """
        Sets the alert_license_expired of this UserInfo.

        :param alert_license_expired: The alert_license_expired of this UserInfo.
        :type: bool
        """

        self._alert_license_expired = alert_license_expired

    @property
    def alert_license_will_expired(self):
        """
        Gets the alert_license_will_expired of this UserInfo.

        :return: The alert_license_will_expired of this UserInfo.
        :rtype: bool
        """
        return self._alert_license_will_expired

    @alert_license_will_expired.setter
    def alert_license_will_expired(self, alert_license_will_expired):
        """
        Sets the alert_license_will_expired of this UserInfo.

        :param alert_license_will_expired: The alert_license_will_expired of this UserInfo.
        :type: bool
        """

        self._alert_license_will_expired = alert_license_will_expired

    @property
    def passwd(self):
        """
        Gets the passwd of this UserInfo.

        :return: The passwd of this UserInfo.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """
        Sets the passwd of this UserInfo.

        :param passwd: The passwd of this UserInfo.
        :type: str
        """
        if passwd is None:
            raise ValueError("Invalid value for `passwd`, must not be `None`")

        self._passwd = passwd

    @property
    def email(self):
        """
        Gets the email of this UserInfo.

        :return: The email of this UserInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserInfo.

        :param email: The email of this UserInfo.
        :type: str
        """

        self._email = email

    @property
    def alert_license_purchased(self):
        """
        Gets the alert_license_purchased of this UserInfo.

        :return: The alert_license_purchased of this UserInfo.
        :rtype: bool
        """
        return self._alert_license_purchased

    @alert_license_purchased.setter
    def alert_license_purchased(self, alert_license_purchased):
        """
        Sets the alert_license_purchased of this UserInfo.

        :param alert_license_purchased: The alert_license_purchased of this UserInfo.
        :type: bool
        """

        self._alert_license_purchased = alert_license_purchased

    @property
    def alert_payment_received(self):
        """
        Gets the alert_payment_received of this UserInfo.

        :return: The alert_payment_received of this UserInfo.
        :rtype: bool
        """
        return self._alert_payment_received

    @alert_payment_received.setter
    def alert_payment_received(self, alert_payment_received):
        """
        Sets the alert_payment_received of this UserInfo.

        :param alert_payment_received: The alert_payment_received of this UserInfo.
        :type: bool
        """

        self._alert_payment_received = alert_payment_received

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
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
