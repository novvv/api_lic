# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserInfoGet(object):
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
        'last_login': 'datetime',
        'passwd': 'str',
        'first_name': 'str',
        'user_uuid': 'str',
        'alert_license_will_expired': 'bool',
        'email': 'str',
        'user_type': 'str',
        'last_name': 'str',
        'alert_license_purchased': 'bool',
        'alert_license_expired': 'bool',
        'alert_payment_received': 'bool',
        'logo_file_uuid': 'str'
    }

    attribute_map = {
        'last_login': 'last_login',
        'passwd': 'passwd',
        'first_name': 'first_name',
        'user_uuid': 'user_uuid',
        'alert_license_will_expired': 'alert_license_will_expired',
        'email': 'email',
        'user_type': 'user_type',
        'last_name': 'last_name',
        'alert_license_purchased': 'alert_license_purchased',
        'alert_license_expired': 'alert_license_expired',
        'alert_payment_received': 'alert_payment_received',
        'logo_file_uuid': 'logo_file_uuid'
    }

    def __init__(self, last_login=None, passwd=None, first_name=None, user_uuid=None, alert_license_will_expired=None, email=None, user_type=None, last_name=None, alert_license_purchased=None, alert_license_expired=None, alert_payment_received=None, logo_file_uuid=None):
        """
        UserInfoGet - a model defined in Swagger
        """

        self._last_login = None
        self._passwd = None
        self._first_name = None
        self._user_uuid = None
        self._alert_license_will_expired = None
        self._email = None
        self._user_type = None
        self._last_name = None
        self._alert_license_purchased = None
        self._alert_license_expired = None
        self._alert_payment_received = None
        self._logo_file_uuid = None

        if last_login is not None:
          self.last_login = last_login
        self.passwd = passwd
        if first_name is not None:
          self.first_name = first_name
        if user_uuid is not None:
          self.user_uuid = user_uuid
        if alert_license_will_expired is not None:
          self.alert_license_will_expired = alert_license_will_expired
        if email is not None:
          self.email = email
        if user_type is not None:
          self.user_type = user_type
        if last_name is not None:
          self.last_name = last_name
        if alert_license_purchased is not None:
          self.alert_license_purchased = alert_license_purchased
        if alert_license_expired is not None:
          self.alert_license_expired = alert_license_expired
        if alert_payment_received is not None:
          self.alert_payment_received = alert_payment_received
        if logo_file_uuid is not None:
          self.logo_file_uuid = logo_file_uuid

    @property
    def last_login(self):
        """
        Gets the last_login of this UserInfoGet.

        :return: The last_login of this UserInfoGet.
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """
        Sets the last_login of this UserInfoGet.

        :param last_login: The last_login of this UserInfoGet.
        :type: datetime
        """

        self._last_login = last_login

    @property
    def passwd(self):
        """
        Gets the passwd of this UserInfoGet.

        :return: The passwd of this UserInfoGet.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """
        Sets the passwd of this UserInfoGet.

        :param passwd: The passwd of this UserInfoGet.
        :type: str
        """
        if passwd is None:
            raise ValueError("Invalid value for `passwd`, must not be `None`")

        self._passwd = passwd

    @property
    def first_name(self):
        """
        Gets the first_name of this UserInfoGet.

        :return: The first_name of this UserInfoGet.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserInfoGet.

        :param first_name: The first_name of this UserInfoGet.
        :type: str
        """

        self._first_name = first_name

    @property
    def user_uuid(self):
        """
        Gets the user_uuid of this UserInfoGet.

        :return: The user_uuid of this UserInfoGet.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """
        Sets the user_uuid of this UserInfoGet.

        :param user_uuid: The user_uuid of this UserInfoGet.
        :type: str
        """
        if user_uuid is not None and len(user_uuid) > 36:
            raise ValueError("Invalid value for `user_uuid`, length must be less than or equal to `36`")

        self._user_uuid = user_uuid

    @property
    def alert_license_will_expired(self):
        """
        Gets the alert_license_will_expired of this UserInfoGet.

        :return: The alert_license_will_expired of this UserInfoGet.
        :rtype: bool
        """
        return self._alert_license_will_expired

    @alert_license_will_expired.setter
    def alert_license_will_expired(self, alert_license_will_expired):
        """
        Sets the alert_license_will_expired of this UserInfoGet.

        :param alert_license_will_expired: The alert_license_will_expired of this UserInfoGet.
        :type: bool
        """

        self._alert_license_will_expired = alert_license_will_expired

    @property
    def email(self):
        """
        Gets the email of this UserInfoGet.

        :return: The email of this UserInfoGet.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserInfoGet.

        :param email: The email of this UserInfoGet.
        :type: str
        """

        self._email = email

    @property
    def user_type(self):
        """
        Gets the user_type of this UserInfoGet.

        :return: The user_type of this UserInfoGet.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """
        Sets the user_type of this UserInfoGet.

        :param user_type: The user_type of this UserInfoGet.
        :type: str
        """

        self._user_type = user_type

    @property
    def last_name(self):
        """
        Gets the last_name of this UserInfoGet.

        :return: The last_name of this UserInfoGet.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserInfoGet.

        :param last_name: The last_name of this UserInfoGet.
        :type: str
        """

        self._last_name = last_name

    @property
    def alert_license_purchased(self):
        """
        Gets the alert_license_purchased of this UserInfoGet.

        :return: The alert_license_purchased of this UserInfoGet.
        :rtype: bool
        """
        return self._alert_license_purchased

    @alert_license_purchased.setter
    def alert_license_purchased(self, alert_license_purchased):
        """
        Sets the alert_license_purchased of this UserInfoGet.

        :param alert_license_purchased: The alert_license_purchased of this UserInfoGet.
        :type: bool
        """

        self._alert_license_purchased = alert_license_purchased

    @property
    def alert_license_expired(self):
        """
        Gets the alert_license_expired of this UserInfoGet.

        :return: The alert_license_expired of this UserInfoGet.
        :rtype: bool
        """
        return self._alert_license_expired

    @alert_license_expired.setter
    def alert_license_expired(self, alert_license_expired):
        """
        Sets the alert_license_expired of this UserInfoGet.

        :param alert_license_expired: The alert_license_expired of this UserInfoGet.
        :type: bool
        """

        self._alert_license_expired = alert_license_expired

    @property
    def alert_payment_received(self):
        """
        Gets the alert_payment_received of this UserInfoGet.

        :return: The alert_payment_received of this UserInfoGet.
        :rtype: bool
        """
        return self._alert_payment_received

    @alert_payment_received.setter
    def alert_payment_received(self, alert_payment_received):
        """
        Sets the alert_payment_received of this UserInfoGet.

        :param alert_payment_received: The alert_payment_received of this UserInfoGet.
        :type: bool
        """

        self._alert_payment_received = alert_payment_received

    @property
    def logo_file_uuid(self):
        """
        Gets the logo_file_uuid of this UserInfoGet.

        :return: The logo_file_uuid of this UserInfoGet.
        :rtype: str
        """
        return self._logo_file_uuid

    @logo_file_uuid.setter
    def logo_file_uuid(self, logo_file_uuid):
        """
        Sets the logo_file_uuid of this UserInfoGet.

        :param logo_file_uuid: The logo_file_uuid of this UserInfoGet.
        :type: str
        """

        self._logo_file_uuid = logo_file_uuid

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
        if not isinstance(other, UserInfoGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
