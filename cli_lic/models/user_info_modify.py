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


class UserInfoModify(object):
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
        'first_name': 'str',
        'email': 'str',
        'alert_payment_received': 'bool',
        'alert_license_purchased': 'bool',
        'last_name': 'str',
        'passwd': 'str',
        'logo_file_uuid': 'str',
        'alert_license_will_expired': 'bool',
        'alert_license_expired': 'bool'
    }

    attribute_map = {
        'first_name': 'first_name',
        'email': 'email',
        'alert_payment_received': 'alert_payment_received',
        'alert_license_purchased': 'alert_license_purchased',
        'last_name': 'last_name',
        'passwd': 'passwd',
        'logo_file_uuid': 'logo_file_uuid',
        'alert_license_will_expired': 'alert_license_will_expired',
        'alert_license_expired': 'alert_license_expired'
    }

    def __init__(self, first_name=None, email=None, alert_payment_received=None, alert_license_purchased=None, last_name=None, passwd=None, logo_file_uuid=None, alert_license_will_expired=None, alert_license_expired=None):
        """
        UserInfoModify - a model defined in Swagger
        """

        self._first_name = None
        self._email = None
        self._alert_payment_received = None
        self._alert_license_purchased = None
        self._last_name = None
        self._passwd = None
        self._logo_file_uuid = None
        self._alert_license_will_expired = None
        self._alert_license_expired = None

        if first_name is not None:
          self.first_name = first_name
        if email is not None:
          self.email = email
        if alert_payment_received is not None:
          self.alert_payment_received = alert_payment_received
        if alert_license_purchased is not None:
          self.alert_license_purchased = alert_license_purchased
        if last_name is not None:
          self.last_name = last_name
        if passwd is not None:
          self.passwd = passwd
        if logo_file_uuid is not None:
          self.logo_file_uuid = logo_file_uuid
        if alert_license_will_expired is not None:
          self.alert_license_will_expired = alert_license_will_expired
        if alert_license_expired is not None:
          self.alert_license_expired = alert_license_expired

    @property
    def first_name(self):
        """
        Gets the first_name of this UserInfoModify.

        :return: The first_name of this UserInfoModify.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserInfoModify.

        :param first_name: The first_name of this UserInfoModify.
        :type: str
        """
        if first_name is not None and len(first_name) > 32:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `32`")

        self._first_name = first_name

    @property
    def email(self):
        """
        Gets the email of this UserInfoModify.

        :return: The email of this UserInfoModify.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserInfoModify.

        :param email: The email of this UserInfoModify.
        :type: str
        """

        self._email = email

    @property
    def alert_payment_received(self):
        """
        Gets the alert_payment_received of this UserInfoModify.

        :return: The alert_payment_received of this UserInfoModify.
        :rtype: bool
        """
        return self._alert_payment_received

    @alert_payment_received.setter
    def alert_payment_received(self, alert_payment_received):
        """
        Sets the alert_payment_received of this UserInfoModify.

        :param alert_payment_received: The alert_payment_received of this UserInfoModify.
        :type: bool
        """

        self._alert_payment_received = alert_payment_received

    @property
    def alert_license_purchased(self):
        """
        Gets the alert_license_purchased of this UserInfoModify.

        :return: The alert_license_purchased of this UserInfoModify.
        :rtype: bool
        """
        return self._alert_license_purchased

    @alert_license_purchased.setter
    def alert_license_purchased(self, alert_license_purchased):
        """
        Sets the alert_license_purchased of this UserInfoModify.

        :param alert_license_purchased: The alert_license_purchased of this UserInfoModify.
        :type: bool
        """

        self._alert_license_purchased = alert_license_purchased

    @property
    def last_name(self):
        """
        Gets the last_name of this UserInfoModify.

        :return: The last_name of this UserInfoModify.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserInfoModify.

        :param last_name: The last_name of this UserInfoModify.
        :type: str
        """
        if last_name is not None and len(last_name) > 32:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `32`")

        self._last_name = last_name

    @property
    def passwd(self):
        """
        Gets the passwd of this UserInfoModify.

        :return: The passwd of this UserInfoModify.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """
        Sets the passwd of this UserInfoModify.

        :param passwd: The passwd of this UserInfoModify.
        :type: str
        """

        self._passwd = passwd

    @property
    def logo_file_uuid(self):
        """
        Gets the logo_file_uuid of this UserInfoModify.

        :return: The logo_file_uuid of this UserInfoModify.
        :rtype: str
        """
        return self._logo_file_uuid

    @logo_file_uuid.setter
    def logo_file_uuid(self, logo_file_uuid):
        """
        Sets the logo_file_uuid of this UserInfoModify.

        :param logo_file_uuid: The logo_file_uuid of this UserInfoModify.
        :type: str
        """

        self._logo_file_uuid = logo_file_uuid

    @property
    def alert_license_will_expired(self):
        """
        Gets the alert_license_will_expired of this UserInfoModify.

        :return: The alert_license_will_expired of this UserInfoModify.
        :rtype: bool
        """
        return self._alert_license_will_expired

    @alert_license_will_expired.setter
    def alert_license_will_expired(self, alert_license_will_expired):
        """
        Sets the alert_license_will_expired of this UserInfoModify.

        :param alert_license_will_expired: The alert_license_will_expired of this UserInfoModify.
        :type: bool
        """

        self._alert_license_will_expired = alert_license_will_expired

    @property
    def alert_license_expired(self):
        """
        Gets the alert_license_expired of this UserInfoModify.

        :return: The alert_license_expired of this UserInfoModify.
        :rtype: bool
        """
        return self._alert_license_expired

    @alert_license_expired.setter
    def alert_license_expired(self, alert_license_expired):
        """
        Sets the alert_license_expired of this UserInfoModify.

        :param alert_license_expired: The alert_license_expired of this UserInfoModify.
        :type: bool
        """

        self._alert_license_expired = alert_license_expired

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
        if not isinstance(other, UserInfoModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
