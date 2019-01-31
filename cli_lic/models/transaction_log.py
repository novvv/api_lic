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


class TransactionLog(object):
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
        'transaction_id': 'str',
        'amount_total': 'float',
        'transaction_type': 'str',
        'amount_switch': 'float',
        'transaction_src': 'object',
        'transaction_time': 'datetime',
        'payment_uuid': 'str',
        'result': 'str',
        'status': 'int',
        'amount_lrn': 'float',
        'type': 'int',
        'license_lrn_uuid': 'str',
        'from_ip': 'str',
        'license_switch_uuid': 'str'
    }

    attribute_map = {
        'transaction_id': 'transaction_id',
        'amount_total': 'amount_total',
        'transaction_type': 'transaction_type',
        'amount_switch': 'amount_switch',
        'transaction_src': 'transaction_src',
        'transaction_time': 'transaction_time',
        'payment_uuid': 'payment_uuid',
        'result': 'result',
        'status': 'status',
        'amount_lrn': 'amount_lrn',
        'type': 'type',
        'license_lrn_uuid': 'license_lrn_uuid',
        'from_ip': 'from_ip',
        'license_switch_uuid': 'license_switch_uuid'
    }

    def __init__(self, transaction_id=None, amount_total=None, transaction_type=None, amount_switch=None, transaction_src=None, transaction_time=None, payment_uuid=None, result=None, status=None, amount_lrn=None, type=None, license_lrn_uuid=None, from_ip=None, license_switch_uuid=None):
        """
        TransactionLog - a model defined in Swagger
        """

        self._transaction_id = None
        self._amount_total = None
        self._transaction_type = None
        self._amount_switch = None
        self._transaction_src = None
        self._transaction_time = None
        self._payment_uuid = None
        self._result = None
        self._status = None
        self._amount_lrn = None
        self._type = None
        self._license_lrn_uuid = None
        self._from_ip = None
        self._license_switch_uuid = None

        if transaction_id is not None:
          self.transaction_id = transaction_id
        if amount_total is not None:
          self.amount_total = amount_total
        if transaction_type is not None:
          self.transaction_type = transaction_type
        if amount_switch is not None:
          self.amount_switch = amount_switch
        if transaction_src is not None:
          self.transaction_src = transaction_src
        if transaction_time is not None:
          self.transaction_time = transaction_time
        if payment_uuid is not None:
          self.payment_uuid = payment_uuid
        if result is not None:
          self.result = result
        if status is not None:
          self.status = status
        if amount_lrn is not None:
          self.amount_lrn = amount_lrn
        if type is not None:
          self.type = type
        if license_lrn_uuid is not None:
          self.license_lrn_uuid = license_lrn_uuid
        if from_ip is not None:
          self.from_ip = from_ip
        if license_switch_uuid is not None:
          self.license_switch_uuid = license_switch_uuid

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this TransactionLog.

        :return: The transaction_id of this TransactionLog.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this TransactionLog.

        :param transaction_id: The transaction_id of this TransactionLog.
        :type: str
        """
        if transaction_id is not None and len(transaction_id) > 255:
            raise ValueError("Invalid value for `transaction_id`, length must be less than or equal to `255`")

        self._transaction_id = transaction_id

    @property
    def amount_total(self):
        """
        Gets the amount_total of this TransactionLog.

        :return: The amount_total of this TransactionLog.
        :rtype: float
        """
        return self._amount_total

    @amount_total.setter
    def amount_total(self, amount_total):
        """
        Sets the amount_total of this TransactionLog.

        :param amount_total: The amount_total of this TransactionLog.
        :type: float
        """

        self._amount_total = amount_total

    @property
    def transaction_type(self):
        """
        Gets the transaction_type of this TransactionLog.

        :return: The transaction_type of this TransactionLog.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """
        Sets the transaction_type of this TransactionLog.

        :param transaction_type: The transaction_type of this TransactionLog.
        :type: str
        """
        if transaction_type is not None and len(transaction_type) > 255:
            raise ValueError("Invalid value for `transaction_type`, length must be less than or equal to `255`")

        self._transaction_type = transaction_type

    @property
    def amount_switch(self):
        """
        Gets the amount_switch of this TransactionLog.

        :return: The amount_switch of this TransactionLog.
        :rtype: float
        """
        return self._amount_switch

    @amount_switch.setter
    def amount_switch(self, amount_switch):
        """
        Sets the amount_switch of this TransactionLog.

        :param amount_switch: The amount_switch of this TransactionLog.
        :type: float
        """

        self._amount_switch = amount_switch

    @property
    def transaction_src(self):
        """
        Gets the transaction_src of this TransactionLog.

        :return: The transaction_src of this TransactionLog.
        :rtype: object
        """
        return self._transaction_src

    @transaction_src.setter
    def transaction_src(self, transaction_src):
        """
        Sets the transaction_src of this TransactionLog.

        :param transaction_src: The transaction_src of this TransactionLog.
        :type: object
        """

        self._transaction_src = transaction_src

    @property
    def transaction_time(self):
        """
        Gets the transaction_time of this TransactionLog.

        :return: The transaction_time of this TransactionLog.
        :rtype: datetime
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """
        Sets the transaction_time of this TransactionLog.

        :param transaction_time: The transaction_time of this TransactionLog.
        :type: datetime
        """

        self._transaction_time = transaction_time

    @property
    def payment_uuid(self):
        """
        Gets the payment_uuid of this TransactionLog.

        :return: The payment_uuid of this TransactionLog.
        :rtype: str
        """
        return self._payment_uuid

    @payment_uuid.setter
    def payment_uuid(self, payment_uuid):
        """
        Sets the payment_uuid of this TransactionLog.

        :param payment_uuid: The payment_uuid of this TransactionLog.
        :type: str
        """
        if payment_uuid is not None and len(payment_uuid) > 36:
            raise ValueError("Invalid value for `payment_uuid`, length must be less than or equal to `36`")

        self._payment_uuid = payment_uuid

    @property
    def result(self):
        """
        Gets the result of this TransactionLog.

        :return: The result of this TransactionLog.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this TransactionLog.

        :param result: The result of this TransactionLog.
        :type: str
        """

        self._result = result

    @property
    def status(self):
        """
        Gets the status of this TransactionLog.

        :return: The status of this TransactionLog.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TransactionLog.

        :param status: The status of this TransactionLog.
        :type: int
        """

        self._status = status

    @property
    def amount_lrn(self):
        """
        Gets the amount_lrn of this TransactionLog.

        :return: The amount_lrn of this TransactionLog.
        :rtype: float
        """
        return self._amount_lrn

    @amount_lrn.setter
    def amount_lrn(self, amount_lrn):
        """
        Sets the amount_lrn of this TransactionLog.

        :param amount_lrn: The amount_lrn of this TransactionLog.
        :type: float
        """

        self._amount_lrn = amount_lrn

    @property
    def type(self):
        """
        Gets the type of this TransactionLog.

        :return: The type of this TransactionLog.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TransactionLog.

        :param type: The type of this TransactionLog.
        :type: int
        """

        self._type = type

    @property
    def license_lrn_uuid(self):
        """
        Gets the license_lrn_uuid of this TransactionLog.

        :return: The license_lrn_uuid of this TransactionLog.
        :rtype: str
        """
        return self._license_lrn_uuid

    @license_lrn_uuid.setter
    def license_lrn_uuid(self, license_lrn_uuid):
        """
        Sets the license_lrn_uuid of this TransactionLog.

        :param license_lrn_uuid: The license_lrn_uuid of this TransactionLog.
        :type: str
        """
        if license_lrn_uuid is not None and len(license_lrn_uuid) > 36:
            raise ValueError("Invalid value for `license_lrn_uuid`, length must be less than or equal to `36`")

        self._license_lrn_uuid = license_lrn_uuid

    @property
    def from_ip(self):
        """
        Gets the from_ip of this TransactionLog.

        :return: The from_ip of this TransactionLog.
        :rtype: str
        """
        return self._from_ip

    @from_ip.setter
    def from_ip(self, from_ip):
        """
        Sets the from_ip of this TransactionLog.

        :param from_ip: The from_ip of this TransactionLog.
        :type: str
        """
        if from_ip is not None and len(from_ip) > 36:
            raise ValueError("Invalid value for `from_ip`, length must be less than or equal to `36`")

        self._from_ip = from_ip

    @property
    def license_switch_uuid(self):
        """
        Gets the license_switch_uuid of this TransactionLog.

        :return: The license_switch_uuid of this TransactionLog.
        :rtype: str
        """
        return self._license_switch_uuid

    @license_switch_uuid.setter
    def license_switch_uuid(self, license_switch_uuid):
        """
        Sets the license_switch_uuid of this TransactionLog.

        :param license_switch_uuid: The license_switch_uuid of this TransactionLog.
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
        if not isinstance(other, TransactionLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
