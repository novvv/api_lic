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


class ConfigPaymentModify(object):
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
        'stripe_email': 'str',
        'confirm_enabled': 'bool',
        'email_confirm_to': 'str',
        'stripe_pkey': 'str',
        'email_cc_to': 'str',
        'stripe_test_mode': 'bool',
        'stripe_skey': 'str',
        'notification_enabled': 'bool',
        'stripe_svc_charge': 'int',
        'charge_type': 'str'
    }

    attribute_map = {
        'stripe_email': 'stripe_email',
        'confirm_enabled': 'confirm_enabled',
        'email_confirm_to': 'email_confirm_to',
        'stripe_pkey': 'stripe_pkey',
        'email_cc_to': 'email_cc_to',
        'stripe_test_mode': 'stripe_test_mode',
        'stripe_skey': 'stripe_skey',
        'notification_enabled': 'notification_enabled',
        'stripe_svc_charge': 'stripe_svc_charge',
        'charge_type': 'charge_type'
    }

    def __init__(self, stripe_email=None, confirm_enabled=None, email_confirm_to=None, stripe_pkey=None, email_cc_to=None, stripe_test_mode=None, stripe_skey=None, notification_enabled=None, stripe_svc_charge=None, charge_type='actual received'):
        """
        ConfigPaymentModify - a model defined in Swagger
        """

        self._stripe_email = None
        self._confirm_enabled = None
        self._email_confirm_to = None
        self._stripe_pkey = None
        self._email_cc_to = None
        self._stripe_test_mode = None
        self._stripe_skey = None
        self._notification_enabled = None
        self._stripe_svc_charge = None
        self._charge_type = None

        if stripe_email is not None:
          self.stripe_email = stripe_email
        if confirm_enabled is not None:
          self.confirm_enabled = confirm_enabled
        if email_confirm_to is not None:
          self.email_confirm_to = email_confirm_to
        if stripe_pkey is not None:
          self.stripe_pkey = stripe_pkey
        if email_cc_to is not None:
          self.email_cc_to = email_cc_to
        if stripe_test_mode is not None:
          self.stripe_test_mode = stripe_test_mode
        if stripe_skey is not None:
          self.stripe_skey = stripe_skey
        if notification_enabled is not None:
          self.notification_enabled = notification_enabled
        if stripe_svc_charge is not None:
          self.stripe_svc_charge = stripe_svc_charge
        if charge_type is not None:
          self.charge_type = charge_type

    @property
    def stripe_email(self):
        """
        Gets the stripe_email of this ConfigPaymentModify.

        :return: The stripe_email of this ConfigPaymentModify.
        :rtype: str
        """
        return self._stripe_email

    @stripe_email.setter
    def stripe_email(self, stripe_email):
        """
        Sets the stripe_email of this ConfigPaymentModify.

        :param stripe_email: The stripe_email of this ConfigPaymentModify.
        :type: str
        """
        if stripe_email is not None and len(stripe_email) > 64:
            raise ValueError("Invalid value for `stripe_email`, length must be less than or equal to `64`")

        self._stripe_email = stripe_email

    @property
    def confirm_enabled(self):
        """
        Gets the confirm_enabled of this ConfigPaymentModify.

        :return: The confirm_enabled of this ConfigPaymentModify.
        :rtype: bool
        """
        return self._confirm_enabled

    @confirm_enabled.setter
    def confirm_enabled(self, confirm_enabled):
        """
        Sets the confirm_enabled of this ConfigPaymentModify.

        :param confirm_enabled: The confirm_enabled of this ConfigPaymentModify.
        :type: bool
        """

        self._confirm_enabled = confirm_enabled

    @property
    def email_confirm_to(self):
        """
        Gets the email_confirm_to of this ConfigPaymentModify.

        :return: The email_confirm_to of this ConfigPaymentModify.
        :rtype: str
        """
        return self._email_confirm_to

    @email_confirm_to.setter
    def email_confirm_to(self, email_confirm_to):
        """
        Sets the email_confirm_to of this ConfigPaymentModify.

        :param email_confirm_to: The email_confirm_to of this ConfigPaymentModify.
        :type: str
        """
        if email_confirm_to is not None and len(email_confirm_to) > 64:
            raise ValueError("Invalid value for `email_confirm_to`, length must be less than or equal to `64`")

        self._email_confirm_to = email_confirm_to

    @property
    def stripe_pkey(self):
        """
        Gets the stripe_pkey of this ConfigPaymentModify.

        :return: The stripe_pkey of this ConfigPaymentModify.
        :rtype: str
        """
        return self._stripe_pkey

    @stripe_pkey.setter
    def stripe_pkey(self, stripe_pkey):
        """
        Sets the stripe_pkey of this ConfigPaymentModify.

        :param stripe_pkey: The stripe_pkey of this ConfigPaymentModify.
        :type: str
        """
        if stripe_pkey is not None and len(stripe_pkey) > 64:
            raise ValueError("Invalid value for `stripe_pkey`, length must be less than or equal to `64`")

        self._stripe_pkey = stripe_pkey

    @property
    def email_cc_to(self):
        """
        Gets the email_cc_to of this ConfigPaymentModify.

        :return: The email_cc_to of this ConfigPaymentModify.
        :rtype: str
        """
        return self._email_cc_to

    @email_cc_to.setter
    def email_cc_to(self, email_cc_to):
        """
        Sets the email_cc_to of this ConfigPaymentModify.

        :param email_cc_to: The email_cc_to of this ConfigPaymentModify.
        :type: str
        """
        if email_cc_to is not None and len(email_cc_to) > 64:
            raise ValueError("Invalid value for `email_cc_to`, length must be less than or equal to `64`")

        self._email_cc_to = email_cc_to

    @property
    def stripe_test_mode(self):
        """
        Gets the stripe_test_mode of this ConfigPaymentModify.

        :return: The stripe_test_mode of this ConfigPaymentModify.
        :rtype: bool
        """
        return self._stripe_test_mode

    @stripe_test_mode.setter
    def stripe_test_mode(self, stripe_test_mode):
        """
        Sets the stripe_test_mode of this ConfigPaymentModify.

        :param stripe_test_mode: The stripe_test_mode of this ConfigPaymentModify.
        :type: bool
        """

        self._stripe_test_mode = stripe_test_mode

    @property
    def stripe_skey(self):
        """
        Gets the stripe_skey of this ConfigPaymentModify.

        :return: The stripe_skey of this ConfigPaymentModify.
        :rtype: str
        """
        return self._stripe_skey

    @stripe_skey.setter
    def stripe_skey(self, stripe_skey):
        """
        Sets the stripe_skey of this ConfigPaymentModify.

        :param stripe_skey: The stripe_skey of this ConfigPaymentModify.
        :type: str
        """
        if stripe_skey is not None and len(stripe_skey) > 64:
            raise ValueError("Invalid value for `stripe_skey`, length must be less than or equal to `64`")

        self._stripe_skey = stripe_skey

    @property
    def notification_enabled(self):
        """
        Gets the notification_enabled of this ConfigPaymentModify.

        :return: The notification_enabled of this ConfigPaymentModify.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        """
        Sets the notification_enabled of this ConfigPaymentModify.

        :param notification_enabled: The notification_enabled of this ConfigPaymentModify.
        :type: bool
        """

        self._notification_enabled = notification_enabled

    @property
    def stripe_svc_charge(self):
        """
        Gets the stripe_svc_charge of this ConfigPaymentModify.

        :return: The stripe_svc_charge of this ConfigPaymentModify.
        :rtype: int
        """
        return self._stripe_svc_charge

    @stripe_svc_charge.setter
    def stripe_svc_charge(self, stripe_svc_charge):
        """
        Sets the stripe_svc_charge of this ConfigPaymentModify.

        :param stripe_svc_charge: The stripe_svc_charge of this ConfigPaymentModify.
        :type: int
        """

        self._stripe_svc_charge = stripe_svc_charge

    @property
    def charge_type(self):
        """
        Gets the charge_type of this ConfigPaymentModify.

        :return: The charge_type of this ConfigPaymentModify.
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """
        Sets the charge_type of this ConfigPaymentModify.

        :param charge_type: The charge_type of this ConfigPaymentModify.
        :type: str
        """
        allowed_values = ["actual received", "credit total"]
        if charge_type not in allowed_values:
            raise ValueError(
                "Invalid value for `charge_type` ({0}), must be one of {1}"
                .format(charge_type, allowed_values)
            )

        self._charge_type = charge_type

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
        if not isinstance(other, ConfigPaymentModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
