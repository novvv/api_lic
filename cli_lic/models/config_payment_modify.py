# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.19
    
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
        'paypal_client_id': 'str',
        'paypal_email': 'str',
        'email_confirm_to': 'str',
        'stripe_test_mode': 'bool',
        'charge_type': 'str',
        'notification_enabled': 'bool',
        'stripe_skey': 'str',
        'email_cc_to': 'str',
        'paypal_skey': 'str',
        'confirm_enabled': 'bool',
        'stripe_svc_charge': 'float',
        'stripe_pkey': 'str',
        'paypal_test_mode': 'bool',
        'paypal_svc_charge': 'float'
    }

    attribute_map = {
        'paypal_client_id': 'paypal_client_id',
        'paypal_email': 'paypal_email',
        'email_confirm_to': 'email_confirm_to',
        'stripe_test_mode': 'stripe_test_mode',
        'charge_type': 'charge_type',
        'notification_enabled': 'notification_enabled',
        'stripe_skey': 'stripe_skey',
        'email_cc_to': 'email_cc_to',
        'paypal_skey': 'paypal_skey',
        'confirm_enabled': 'confirm_enabled',
        'stripe_svc_charge': 'stripe_svc_charge',
        'stripe_pkey': 'stripe_pkey',
        'paypal_test_mode': 'paypal_test_mode',
        'paypal_svc_charge': 'paypal_svc_charge'
    }

    def __init__(self, paypal_client_id=None, paypal_email=None, email_confirm_to=None, stripe_test_mode=None, charge_type='actual received', notification_enabled=None, stripe_skey=None, email_cc_to=None, paypal_skey=None, confirm_enabled=None, stripe_svc_charge=None, stripe_pkey=None, paypal_test_mode=None, paypal_svc_charge=None):
        """
        ConfigPaymentModify - a model defined in Swagger
        """

        self._paypal_client_id = None
        self._paypal_email = None
        self._email_confirm_to = None
        self._stripe_test_mode = None
        self._charge_type = None
        self._notification_enabled = None
        self._stripe_skey = None
        self._email_cc_to = None
        self._paypal_skey = None
        self._confirm_enabled = None
        self._stripe_svc_charge = None
        self._stripe_pkey = None
        self._paypal_test_mode = None
        self._paypal_svc_charge = None

        if paypal_client_id is not None:
          self.paypal_client_id = paypal_client_id
        if paypal_email is not None:
          self.paypal_email = paypal_email
        if email_confirm_to is not None:
          self.email_confirm_to = email_confirm_to
        if stripe_test_mode is not None:
          self.stripe_test_mode = stripe_test_mode
        if charge_type is not None:
          self.charge_type = charge_type
        if notification_enabled is not None:
          self.notification_enabled = notification_enabled
        if stripe_skey is not None:
          self.stripe_skey = stripe_skey
        if email_cc_to is not None:
          self.email_cc_to = email_cc_to
        if paypal_skey is not None:
          self.paypal_skey = paypal_skey
        if confirm_enabled is not None:
          self.confirm_enabled = confirm_enabled
        if stripe_svc_charge is not None:
          self.stripe_svc_charge = stripe_svc_charge
        if stripe_pkey is not None:
          self.stripe_pkey = stripe_pkey
        if paypal_test_mode is not None:
          self.paypal_test_mode = paypal_test_mode
        if paypal_svc_charge is not None:
          self.paypal_svc_charge = paypal_svc_charge

    @property
    def paypal_client_id(self):
        """
        Gets the paypal_client_id of this ConfigPaymentModify.

        :return: The paypal_client_id of this ConfigPaymentModify.
        :rtype: str
        """
        return self._paypal_client_id

    @paypal_client_id.setter
    def paypal_client_id(self, paypal_client_id):
        """
        Sets the paypal_client_id of this ConfigPaymentModify.

        :param paypal_client_id: The paypal_client_id of this ConfigPaymentModify.
        :type: str
        """
        if paypal_client_id is not None and len(paypal_client_id) > 128:
            raise ValueError("Invalid value for `paypal_client_id`, length must be less than or equal to `128`")

        self._paypal_client_id = paypal_client_id

    @property
    def paypal_email(self):
        """
        Gets the paypal_email of this ConfigPaymentModify.

        :return: The paypal_email of this ConfigPaymentModify.
        :rtype: str
        """
        return self._paypal_email

    @paypal_email.setter
    def paypal_email(self, paypal_email):
        """
        Sets the paypal_email of this ConfigPaymentModify.

        :param paypal_email: The paypal_email of this ConfigPaymentModify.
        :type: str
        """
        if paypal_email is not None and len(paypal_email) > 64:
            raise ValueError("Invalid value for `paypal_email`, length must be less than or equal to `64`")

        self._paypal_email = paypal_email

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
    def paypal_skey(self):
        """
        Gets the paypal_skey of this ConfigPaymentModify.

        :return: The paypal_skey of this ConfigPaymentModify.
        :rtype: str
        """
        return self._paypal_skey

    @paypal_skey.setter
    def paypal_skey(self, paypal_skey):
        """
        Sets the paypal_skey of this ConfigPaymentModify.

        :param paypal_skey: The paypal_skey of this ConfigPaymentModify.
        :type: str
        """
        if paypal_skey is not None and len(paypal_skey) > 128:
            raise ValueError("Invalid value for `paypal_skey`, length must be less than or equal to `128`")

        self._paypal_skey = paypal_skey

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
    def stripe_svc_charge(self):
        """
        Gets the stripe_svc_charge of this ConfigPaymentModify.

        :return: The stripe_svc_charge of this ConfigPaymentModify.
        :rtype: float
        """
        return self._stripe_svc_charge

    @stripe_svc_charge.setter
    def stripe_svc_charge(self, stripe_svc_charge):
        """
        Sets the stripe_svc_charge of this ConfigPaymentModify.

        :param stripe_svc_charge: The stripe_svc_charge of this ConfigPaymentModify.
        :type: float
        """

        self._stripe_svc_charge = stripe_svc_charge

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
    def paypal_test_mode(self):
        """
        Gets the paypal_test_mode of this ConfigPaymentModify.

        :return: The paypal_test_mode of this ConfigPaymentModify.
        :rtype: bool
        """
        return self._paypal_test_mode

    @paypal_test_mode.setter
    def paypal_test_mode(self, paypal_test_mode):
        """
        Sets the paypal_test_mode of this ConfigPaymentModify.

        :param paypal_test_mode: The paypal_test_mode of this ConfigPaymentModify.
        :type: bool
        """

        self._paypal_test_mode = paypal_test_mode

    @property
    def paypal_svc_charge(self):
        """
        Gets the paypal_svc_charge of this ConfigPaymentModify.

        :return: The paypal_svc_charge of this ConfigPaymentModify.
        :rtype: float
        """
        return self._paypal_svc_charge

    @paypal_svc_charge.setter
    def paypal_svc_charge(self, paypal_svc_charge):
        """
        Sets the paypal_svc_charge of this ConfigPaymentModify.

        :param paypal_svc_charge: The paypal_svc_charge of this ConfigPaymentModify.
        :type: float
        """

        self._paypal_svc_charge = paypal_svc_charge

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
