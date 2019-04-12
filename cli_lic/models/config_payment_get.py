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


class ConfigPaymentGet(object):
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
        'confirm_enabled': 'bool',
        'stripe_svc_charge': 'float',
        'stripe_pkey': 'str',
        'charge_type': 'str',
        'notification_enabled': 'bool',
        'stripe_test_mode': 'bool',
        'email_confirm_to': 'str',
        'paypal_email': 'str',
        'paypal_test_mode': 'bool',
        'paypal_client_id': 'str',
        'paypal_svc_charge': 'float',
        'email_cc_to': 'str'
    }

    attribute_map = {
        'confirm_enabled': 'confirm_enabled',
        'stripe_svc_charge': 'stripe_svc_charge',
        'stripe_pkey': 'stripe_pkey',
        'charge_type': 'charge_type',
        'notification_enabled': 'notification_enabled',
        'stripe_test_mode': 'stripe_test_mode',
        'email_confirm_to': 'email_confirm_to',
        'paypal_email': 'paypal_email',
        'paypal_test_mode': 'paypal_test_mode',
        'paypal_client_id': 'paypal_client_id',
        'paypal_svc_charge': 'paypal_svc_charge',
        'email_cc_to': 'email_cc_to'
    }

    def __init__(self, confirm_enabled=None, stripe_svc_charge=None, stripe_pkey=None, charge_type='actual received', notification_enabled=None, stripe_test_mode=None, email_confirm_to=None, paypal_email=None, paypal_test_mode=None, paypal_client_id=None, paypal_svc_charge=None, email_cc_to=None):
        """
        ConfigPaymentGet - a model defined in Swagger
        """

        self._confirm_enabled = None
        self._stripe_svc_charge = None
        self._stripe_pkey = None
        self._charge_type = None
        self._notification_enabled = None
        self._stripe_test_mode = None
        self._email_confirm_to = None
        self._paypal_email = None
        self._paypal_test_mode = None
        self._paypal_client_id = None
        self._paypal_svc_charge = None
        self._email_cc_to = None

        if confirm_enabled is not None:
          self.confirm_enabled = confirm_enabled
        if stripe_svc_charge is not None:
          self.stripe_svc_charge = stripe_svc_charge
        if stripe_pkey is not None:
          self.stripe_pkey = stripe_pkey
        if charge_type is not None:
          self.charge_type = charge_type
        if notification_enabled is not None:
          self.notification_enabled = notification_enabled
        if stripe_test_mode is not None:
          self.stripe_test_mode = stripe_test_mode
        if email_confirm_to is not None:
          self.email_confirm_to = email_confirm_to
        if paypal_email is not None:
          self.paypal_email = paypal_email
        if paypal_test_mode is not None:
          self.paypal_test_mode = paypal_test_mode
        if paypal_client_id is not None:
          self.paypal_client_id = paypal_client_id
        if paypal_svc_charge is not None:
          self.paypal_svc_charge = paypal_svc_charge
        if email_cc_to is not None:
          self.email_cc_to = email_cc_to

    @property
    def confirm_enabled(self):
        """
        Gets the confirm_enabled of this ConfigPaymentGet.

        :return: The confirm_enabled of this ConfigPaymentGet.
        :rtype: bool
        """
        return self._confirm_enabled

    @confirm_enabled.setter
    def confirm_enabled(self, confirm_enabled):
        """
        Sets the confirm_enabled of this ConfigPaymentGet.

        :param confirm_enabled: The confirm_enabled of this ConfigPaymentGet.
        :type: bool
        """

        self._confirm_enabled = confirm_enabled

    @property
    def stripe_svc_charge(self):
        """
        Gets the stripe_svc_charge of this ConfigPaymentGet.

        :return: The stripe_svc_charge of this ConfigPaymentGet.
        :rtype: float
        """
        return self._stripe_svc_charge

    @stripe_svc_charge.setter
    def stripe_svc_charge(self, stripe_svc_charge):
        """
        Sets the stripe_svc_charge of this ConfigPaymentGet.

        :param stripe_svc_charge: The stripe_svc_charge of this ConfigPaymentGet.
        :type: float
        """

        self._stripe_svc_charge = stripe_svc_charge

    @property
    def stripe_pkey(self):
        """
        Gets the stripe_pkey of this ConfigPaymentGet.

        :return: The stripe_pkey of this ConfigPaymentGet.
        :rtype: str
        """
        return self._stripe_pkey

    @stripe_pkey.setter
    def stripe_pkey(self, stripe_pkey):
        """
        Sets the stripe_pkey of this ConfigPaymentGet.

        :param stripe_pkey: The stripe_pkey of this ConfigPaymentGet.
        :type: str
        """
        if stripe_pkey is not None and len(stripe_pkey) > 64:
            raise ValueError("Invalid value for `stripe_pkey`, length must be less than or equal to `64`")

        self._stripe_pkey = stripe_pkey

    @property
    def charge_type(self):
        """
        Gets the charge_type of this ConfigPaymentGet.

        :return: The charge_type of this ConfigPaymentGet.
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """
        Sets the charge_type of this ConfigPaymentGet.

        :param charge_type: The charge_type of this ConfigPaymentGet.
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
    def notification_enabled(self):
        """
        Gets the notification_enabled of this ConfigPaymentGet.

        :return: The notification_enabled of this ConfigPaymentGet.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        """
        Sets the notification_enabled of this ConfigPaymentGet.

        :param notification_enabled: The notification_enabled of this ConfigPaymentGet.
        :type: bool
        """

        self._notification_enabled = notification_enabled

    @property
    def stripe_test_mode(self):
        """
        Gets the stripe_test_mode of this ConfigPaymentGet.

        :return: The stripe_test_mode of this ConfigPaymentGet.
        :rtype: bool
        """
        return self._stripe_test_mode

    @stripe_test_mode.setter
    def stripe_test_mode(self, stripe_test_mode):
        """
        Sets the stripe_test_mode of this ConfigPaymentGet.

        :param stripe_test_mode: The stripe_test_mode of this ConfigPaymentGet.
        :type: bool
        """

        self._stripe_test_mode = stripe_test_mode

    @property
    def email_confirm_to(self):
        """
        Gets the email_confirm_to of this ConfigPaymentGet.

        :return: The email_confirm_to of this ConfigPaymentGet.
        :rtype: str
        """
        return self._email_confirm_to

    @email_confirm_to.setter
    def email_confirm_to(self, email_confirm_to):
        """
        Sets the email_confirm_to of this ConfigPaymentGet.

        :param email_confirm_to: The email_confirm_to of this ConfigPaymentGet.
        :type: str
        """
        if email_confirm_to is not None and len(email_confirm_to) > 64:
            raise ValueError("Invalid value for `email_confirm_to`, length must be less than or equal to `64`")

        self._email_confirm_to = email_confirm_to

    @property
    def paypal_email(self):
        """
        Gets the paypal_email of this ConfigPaymentGet.

        :return: The paypal_email of this ConfigPaymentGet.
        :rtype: str
        """
        return self._paypal_email

    @paypal_email.setter
    def paypal_email(self, paypal_email):
        """
        Sets the paypal_email of this ConfigPaymentGet.

        :param paypal_email: The paypal_email of this ConfigPaymentGet.
        :type: str
        """
        if paypal_email is not None and len(paypal_email) > 64:
            raise ValueError("Invalid value for `paypal_email`, length must be less than or equal to `64`")

        self._paypal_email = paypal_email

    @property
    def paypal_test_mode(self):
        """
        Gets the paypal_test_mode of this ConfigPaymentGet.

        :return: The paypal_test_mode of this ConfigPaymentGet.
        :rtype: bool
        """
        return self._paypal_test_mode

    @paypal_test_mode.setter
    def paypal_test_mode(self, paypal_test_mode):
        """
        Sets the paypal_test_mode of this ConfigPaymentGet.

        :param paypal_test_mode: The paypal_test_mode of this ConfigPaymentGet.
        :type: bool
        """

        self._paypal_test_mode = paypal_test_mode

    @property
    def paypal_client_id(self):
        """
        Gets the paypal_client_id of this ConfigPaymentGet.

        :return: The paypal_client_id of this ConfigPaymentGet.
        :rtype: str
        """
        return self._paypal_client_id

    @paypal_client_id.setter
    def paypal_client_id(self, paypal_client_id):
        """
        Sets the paypal_client_id of this ConfigPaymentGet.

        :param paypal_client_id: The paypal_client_id of this ConfigPaymentGet.
        :type: str
        """
        if paypal_client_id is not None and len(paypal_client_id) > 128:
            raise ValueError("Invalid value for `paypal_client_id`, length must be less than or equal to `128`")

        self._paypal_client_id = paypal_client_id

    @property
    def paypal_svc_charge(self):
        """
        Gets the paypal_svc_charge of this ConfigPaymentGet.

        :return: The paypal_svc_charge of this ConfigPaymentGet.
        :rtype: float
        """
        return self._paypal_svc_charge

    @paypal_svc_charge.setter
    def paypal_svc_charge(self, paypal_svc_charge):
        """
        Sets the paypal_svc_charge of this ConfigPaymentGet.

        :param paypal_svc_charge: The paypal_svc_charge of this ConfigPaymentGet.
        :type: float
        """

        self._paypal_svc_charge = paypal_svc_charge

    @property
    def email_cc_to(self):
        """
        Gets the email_cc_to of this ConfigPaymentGet.

        :return: The email_cc_to of this ConfigPaymentGet.
        :rtype: str
        """
        return self._email_cc_to

    @email_cc_to.setter
    def email_cc_to(self, email_cc_to):
        """
        Sets the email_cc_to of this ConfigPaymentGet.

        :param email_cc_to: The email_cc_to of this ConfigPaymentGet.
        :type: str
        """
        if email_cc_to is not None and len(email_cc_to) > 64:
            raise ValueError("Invalid value for `email_cc_to`, length must be less than or equal to `64`")

        self._email_cc_to = email_cc_to

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
        if not isinstance(other, ConfigPaymentGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
