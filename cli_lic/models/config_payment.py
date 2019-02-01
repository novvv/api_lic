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


class ConfigPayment(object):
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
        'charge_type': 'str',
        'stripe_skey': 'str',
        'stripe_svc_charge': 'float',
        'paypal_skey': 'str',
        'paypal_email': 'str',
        'paypal_test_mode': 'bool',
        'confirm_enabled': 'bool',
        'email_cc_to': 'str',
        'stripe_pkey': 'str',
        'stripe_email': 'str',
        'paypal_svc_charge': 'float',
        'email_confirm_to': 'str',
        'stripe_test_mode': 'bool',
        'paypal_pkey': 'str',
        'notification_enabled': 'bool'
    }

    attribute_map = {
        'charge_type': 'charge_type',
        'stripe_skey': 'stripe_skey',
        'stripe_svc_charge': 'stripe_svc_charge',
        'paypal_skey': 'paypal_skey',
        'paypal_email': 'paypal_email',
        'paypal_test_mode': 'paypal_test_mode',
        'confirm_enabled': 'confirm_enabled',
        'email_cc_to': 'email_cc_to',
        'stripe_pkey': 'stripe_pkey',
        'stripe_email': 'stripe_email',
        'paypal_svc_charge': 'paypal_svc_charge',
        'email_confirm_to': 'email_confirm_to',
        'stripe_test_mode': 'stripe_test_mode',
        'paypal_pkey': 'paypal_pkey',
        'notification_enabled': 'notification_enabled'
    }

    def __init__(self, charge_type='actual received', stripe_skey=None, stripe_svc_charge=None, paypal_skey=None, paypal_email=None, paypal_test_mode=None, confirm_enabled=None, email_cc_to=None, stripe_pkey=None, stripe_email=None, paypal_svc_charge=None, email_confirm_to=None, stripe_test_mode=None, paypal_pkey=None, notification_enabled=None):
        """
        ConfigPayment - a model defined in Swagger
        """

        self._charge_type = None
        self._stripe_skey = None
        self._stripe_svc_charge = None
        self._paypal_skey = None
        self._paypal_email = None
        self._paypal_test_mode = None
        self._confirm_enabled = None
        self._email_cc_to = None
        self._stripe_pkey = None
        self._stripe_email = None
        self._paypal_svc_charge = None
        self._email_confirm_to = None
        self._stripe_test_mode = None
        self._paypal_pkey = None
        self._notification_enabled = None

        if charge_type is not None:
          self.charge_type = charge_type
        if stripe_skey is not None:
          self.stripe_skey = stripe_skey
        if stripe_svc_charge is not None:
          self.stripe_svc_charge = stripe_svc_charge
        if paypal_skey is not None:
          self.paypal_skey = paypal_skey
        if paypal_email is not None:
          self.paypal_email = paypal_email
        if paypal_test_mode is not None:
          self.paypal_test_mode = paypal_test_mode
        if confirm_enabled is not None:
          self.confirm_enabled = confirm_enabled
        if email_cc_to is not None:
          self.email_cc_to = email_cc_to
        if stripe_pkey is not None:
          self.stripe_pkey = stripe_pkey
        if stripe_email is not None:
          self.stripe_email = stripe_email
        if paypal_svc_charge is not None:
          self.paypal_svc_charge = paypal_svc_charge
        if email_confirm_to is not None:
          self.email_confirm_to = email_confirm_to
        if stripe_test_mode is not None:
          self.stripe_test_mode = stripe_test_mode
        if paypal_pkey is not None:
          self.paypal_pkey = paypal_pkey
        if notification_enabled is not None:
          self.notification_enabled = notification_enabled

    @property
    def charge_type(self):
        """
        Gets the charge_type of this ConfigPayment.

        :return: The charge_type of this ConfigPayment.
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """
        Sets the charge_type of this ConfigPayment.

        :param charge_type: The charge_type of this ConfigPayment.
        :type: str
        """
        allowed_values = ["actual received", "credit total"]
        if charge_type not in allowed_values:
            raise ValueError(
                "Invalid value for `charge_type` ({0}), must be one of {1}"
                .format(charge_type, allowed_values)
            )

        self._charge_type = charge_type

    @property
    def stripe_skey(self):
        """
        Gets the stripe_skey of this ConfigPayment.

        :return: The stripe_skey of this ConfigPayment.
        :rtype: str
        """
        return self._stripe_skey

    @stripe_skey.setter
    def stripe_skey(self, stripe_skey):
        """
        Sets the stripe_skey of this ConfigPayment.

        :param stripe_skey: The stripe_skey of this ConfigPayment.
        :type: str
        """
        if stripe_skey is not None and len(stripe_skey) > 64:
            raise ValueError("Invalid value for `stripe_skey`, length must be less than or equal to `64`")

        self._stripe_skey = stripe_skey

    @property
    def stripe_svc_charge(self):
        """
        Gets the stripe_svc_charge of this ConfigPayment.

        :return: The stripe_svc_charge of this ConfigPayment.
        :rtype: float
        """
        return self._stripe_svc_charge

    @stripe_svc_charge.setter
    def stripe_svc_charge(self, stripe_svc_charge):
        """
        Sets the stripe_svc_charge of this ConfigPayment.

        :param stripe_svc_charge: The stripe_svc_charge of this ConfigPayment.
        :type: float
        """

        self._stripe_svc_charge = stripe_svc_charge

    @property
    def paypal_skey(self):
        """
        Gets the paypal_skey of this ConfigPayment.

        :return: The paypal_skey of this ConfigPayment.
        :rtype: str
        """
        return self._paypal_skey

    @paypal_skey.setter
    def paypal_skey(self, paypal_skey):
        """
        Sets the paypal_skey of this ConfigPayment.

        :param paypal_skey: The paypal_skey of this ConfigPayment.
        :type: str
        """
        if paypal_skey is not None and len(paypal_skey) > 128:
            raise ValueError("Invalid value for `paypal_skey`, length must be less than or equal to `128`")

        self._paypal_skey = paypal_skey

    @property
    def paypal_email(self):
        """
        Gets the paypal_email of this ConfigPayment.

        :return: The paypal_email of this ConfigPayment.
        :rtype: str
        """
        return self._paypal_email

    @paypal_email.setter
    def paypal_email(self, paypal_email):
        """
        Sets the paypal_email of this ConfigPayment.

        :param paypal_email: The paypal_email of this ConfigPayment.
        :type: str
        """
        if paypal_email is not None and len(paypal_email) > 64:
            raise ValueError("Invalid value for `paypal_email`, length must be less than or equal to `64`")

        self._paypal_email = paypal_email

    @property
    def paypal_test_mode(self):
        """
        Gets the paypal_test_mode of this ConfigPayment.

        :return: The paypal_test_mode of this ConfigPayment.
        :rtype: bool
        """
        return self._paypal_test_mode

    @paypal_test_mode.setter
    def paypal_test_mode(self, paypal_test_mode):
        """
        Sets the paypal_test_mode of this ConfigPayment.

        :param paypal_test_mode: The paypal_test_mode of this ConfigPayment.
        :type: bool
        """

        self._paypal_test_mode = paypal_test_mode

    @property
    def confirm_enabled(self):
        """
        Gets the confirm_enabled of this ConfigPayment.

        :return: The confirm_enabled of this ConfigPayment.
        :rtype: bool
        """
        return self._confirm_enabled

    @confirm_enabled.setter
    def confirm_enabled(self, confirm_enabled):
        """
        Sets the confirm_enabled of this ConfigPayment.

        :param confirm_enabled: The confirm_enabled of this ConfigPayment.
        :type: bool
        """

        self._confirm_enabled = confirm_enabled

    @property
    def email_cc_to(self):
        """
        Gets the email_cc_to of this ConfigPayment.

        :return: The email_cc_to of this ConfigPayment.
        :rtype: str
        """
        return self._email_cc_to

    @email_cc_to.setter
    def email_cc_to(self, email_cc_to):
        """
        Sets the email_cc_to of this ConfigPayment.

        :param email_cc_to: The email_cc_to of this ConfigPayment.
        :type: str
        """
        if email_cc_to is not None and len(email_cc_to) > 64:
            raise ValueError("Invalid value for `email_cc_to`, length must be less than or equal to `64`")

        self._email_cc_to = email_cc_to

    @property
    def stripe_pkey(self):
        """
        Gets the stripe_pkey of this ConfigPayment.

        :return: The stripe_pkey of this ConfigPayment.
        :rtype: str
        """
        return self._stripe_pkey

    @stripe_pkey.setter
    def stripe_pkey(self, stripe_pkey):
        """
        Sets the stripe_pkey of this ConfigPayment.

        :param stripe_pkey: The stripe_pkey of this ConfigPayment.
        :type: str
        """
        if stripe_pkey is not None and len(stripe_pkey) > 64:
            raise ValueError("Invalid value for `stripe_pkey`, length must be less than or equal to `64`")

        self._stripe_pkey = stripe_pkey

    @property
    def stripe_email(self):
        """
        Gets the stripe_email of this ConfigPayment.

        :return: The stripe_email of this ConfigPayment.
        :rtype: str
        """
        return self._stripe_email

    @stripe_email.setter
    def stripe_email(self, stripe_email):
        """
        Sets the stripe_email of this ConfigPayment.

        :param stripe_email: The stripe_email of this ConfigPayment.
        :type: str
        """
        if stripe_email is not None and len(stripe_email) > 64:
            raise ValueError("Invalid value for `stripe_email`, length must be less than or equal to `64`")

        self._stripe_email = stripe_email

    @property
    def paypal_svc_charge(self):
        """
        Gets the paypal_svc_charge of this ConfigPayment.

        :return: The paypal_svc_charge of this ConfigPayment.
        :rtype: float
        """
        return self._paypal_svc_charge

    @paypal_svc_charge.setter
    def paypal_svc_charge(self, paypal_svc_charge):
        """
        Sets the paypal_svc_charge of this ConfigPayment.

        :param paypal_svc_charge: The paypal_svc_charge of this ConfigPayment.
        :type: float
        """

        self._paypal_svc_charge = paypal_svc_charge

    @property
    def email_confirm_to(self):
        """
        Gets the email_confirm_to of this ConfigPayment.

        :return: The email_confirm_to of this ConfigPayment.
        :rtype: str
        """
        return self._email_confirm_to

    @email_confirm_to.setter
    def email_confirm_to(self, email_confirm_to):
        """
        Sets the email_confirm_to of this ConfigPayment.

        :param email_confirm_to: The email_confirm_to of this ConfigPayment.
        :type: str
        """
        if email_confirm_to is not None and len(email_confirm_to) > 64:
            raise ValueError("Invalid value for `email_confirm_to`, length must be less than or equal to `64`")

        self._email_confirm_to = email_confirm_to

    @property
    def stripe_test_mode(self):
        """
        Gets the stripe_test_mode of this ConfigPayment.

        :return: The stripe_test_mode of this ConfigPayment.
        :rtype: bool
        """
        return self._stripe_test_mode

    @stripe_test_mode.setter
    def stripe_test_mode(self, stripe_test_mode):
        """
        Sets the stripe_test_mode of this ConfigPayment.

        :param stripe_test_mode: The stripe_test_mode of this ConfigPayment.
        :type: bool
        """

        self._stripe_test_mode = stripe_test_mode

    @property
    def paypal_pkey(self):
        """
        Gets the paypal_pkey of this ConfigPayment.

        :return: The paypal_pkey of this ConfigPayment.
        :rtype: str
        """
        return self._paypal_pkey

    @paypal_pkey.setter
    def paypal_pkey(self, paypal_pkey):
        """
        Sets the paypal_pkey of this ConfigPayment.

        :param paypal_pkey: The paypal_pkey of this ConfigPayment.
        :type: str
        """
        if paypal_pkey is not None and len(paypal_pkey) > 128:
            raise ValueError("Invalid value for `paypal_pkey`, length must be less than or equal to `128`")

        self._paypal_pkey = paypal_pkey

    @property
    def notification_enabled(self):
        """
        Gets the notification_enabled of this ConfigPayment.

        :return: The notification_enabled of this ConfigPayment.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        """
        Sets the notification_enabled of this ConfigPayment.

        :param notification_enabled: The notification_enabled of this ConfigPayment.
        :type: bool
        """

        self._notification_enabled = notification_enabled

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
        if not isinstance(other, ConfigPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
