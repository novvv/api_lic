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


class TransactionLogGet(object):
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
        'amount_lrn': 'float',
        'license_switch_uuid': 'str',
        'result': 'str',
        'type': 'int',
        'transaction_src': 'object',
        'amount_switch': 'float',
        'amount_total': 'float',
        'status': 'int',
        'from_ip': 'str',
        'transaction_type': 'str',
        'transaction_time': 'datetime',
        'license_lrn_uuid': 'str',
        'transaction_id': 'str',
        'payment_uuid': 'str'
    }

    attribute_map = {
        'amount_lrn': 'amount_lrn',
        'license_switch_uuid': 'license_switch_uuid',
        'result': 'result',
        'type': 'type',
        'transaction_src': 'transaction_src',
        'amount_switch': 'amount_switch',
        'amount_total': 'amount_total',
        'status': 'status',
        'from_ip': 'from_ip',
        'transaction_type': 'transaction_type',
        'transaction_time': 'transaction_time',
        'license_lrn_uuid': 'license_lrn_uuid',
        'transaction_id': 'transaction_id',
        'payment_uuid': 'payment_uuid'
    }

    def __init__(self, amount_lrn=None, license_switch_uuid=None, result=None, type=None, transaction_src=None, amount_switch=None, amount_total=None, status=None, from_ip=None, transaction_type=None, transaction_time=None, license_lrn_uuid=None, transaction_id=None, payment_uuid=None):
        """
        TransactionLogGet - a model defined in Swagger
        """

        self._amount_lrn = None
        self._license_switch_uuid = None
        self._result = None
        self._type = None
        self._transaction_src = None
        self._amount_switch = None
        self._amount_total = None
        self._status = None
        self._from_ip = None
        self._transaction_type = None
        self._transaction_time = None
        self._license_lrn_uuid = None
        self._transaction_id = None
        self._payment_uuid = None

        if amount_lrn is not None:
          self.amount_lrn = amount_lrn
        if license_switch_uuid is not None:
          self.license_switch_uuid = license_switch_uuid
        if result is not None:
          self.result = result
        if type is not None:
          self.type = type
        if transaction_src is not None:
          self.transaction_src = transaction_src
        if amount_switch is not None:
          self.amount_switch = amount_switch
        if amount_total is not None:
          self.amount_total = amount_total
        if status is not None:
          self.status = status
        if from_ip is not None:
          self.from_ip = from_ip
        if transaction_type is not None:
          self.transaction_type = transaction_type
        if transaction_time is not None:
          self.transaction_time = transaction_time
        if license_lrn_uuid is not None:
          self.license_lrn_uuid = license_lrn_uuid
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if payment_uuid is not None:
          self.payment_uuid = payment_uuid

    @property
    def amount_lrn(self):
        """
        Gets the amount_lrn of this TransactionLogGet.

        :return: The amount_lrn of this TransactionLogGet.
        :rtype: float
        """
        return self._amount_lrn

    @amount_lrn.setter
    def amount_lrn(self, amount_lrn):
        """
        Sets the amount_lrn of this TransactionLogGet.

        :param amount_lrn: The amount_lrn of this TransactionLogGet.
        :type: float
        """

        self._amount_lrn = amount_lrn

    @property
    def license_switch_uuid(self):
        """
        Gets the license_switch_uuid of this TransactionLogGet.

        :return: The license_switch_uuid of this TransactionLogGet.
        :rtype: str
        """
        return self._license_switch_uuid

    @license_switch_uuid.setter
    def license_switch_uuid(self, license_switch_uuid):
        """
        Sets the license_switch_uuid of this TransactionLogGet.

        :param license_switch_uuid: The license_switch_uuid of this TransactionLogGet.
        :type: str
        """
        if license_switch_uuid is not None and len(license_switch_uuid) > 36:
            raise ValueError("Invalid value for `license_switch_uuid`, length must be less than or equal to `36`")

        self._license_switch_uuid = license_switch_uuid

    @property
    def result(self):
        """
        Gets the result of this TransactionLogGet.

        :return: The result of this TransactionLogGet.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this TransactionLogGet.

        :param result: The result of this TransactionLogGet.
        :type: str
        """

        self._result = result

    @property
    def type(self):
        """
        Gets the type of this TransactionLogGet.

        :return: The type of this TransactionLogGet.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TransactionLogGet.

        :param type: The type of this TransactionLogGet.
        :type: int
        """

        self._type = type

    @property
    def transaction_src(self):
        """
        Gets the transaction_src of this TransactionLogGet.

        :return: The transaction_src of this TransactionLogGet.
        :rtype: object
        """
        return self._transaction_src

    @transaction_src.setter
    def transaction_src(self, transaction_src):
        """
        Sets the transaction_src of this TransactionLogGet.

        :param transaction_src: The transaction_src of this TransactionLogGet.
        :type: object
        """

        self._transaction_src = transaction_src

    @property
    def amount_switch(self):
        """
        Gets the amount_switch of this TransactionLogGet.

        :return: The amount_switch of this TransactionLogGet.
        :rtype: float
        """
        return self._amount_switch

    @amount_switch.setter
    def amount_switch(self, amount_switch):
        """
        Sets the amount_switch of this TransactionLogGet.

        :param amount_switch: The amount_switch of this TransactionLogGet.
        :type: float
        """

        self._amount_switch = amount_switch

    @property
    def amount_total(self):
        """
        Gets the amount_total of this TransactionLogGet.

        :return: The amount_total of this TransactionLogGet.
        :rtype: float
        """
        return self._amount_total

    @amount_total.setter
    def amount_total(self, amount_total):
        """
        Sets the amount_total of this TransactionLogGet.

        :param amount_total: The amount_total of this TransactionLogGet.
        :type: float
        """

        self._amount_total = amount_total

    @property
    def status(self):
        """
        Gets the status of this TransactionLogGet.

        :return: The status of this TransactionLogGet.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TransactionLogGet.

        :param status: The status of this TransactionLogGet.
        :type: int
        """

        self._status = status

    @property
    def from_ip(self):
        """
        Gets the from_ip of this TransactionLogGet.

        :return: The from_ip of this TransactionLogGet.
        :rtype: str
        """
        return self._from_ip

    @from_ip.setter
    def from_ip(self, from_ip):
        """
        Sets the from_ip of this TransactionLogGet.

        :param from_ip: The from_ip of this TransactionLogGet.
        :type: str
        """
        if from_ip is not None and len(from_ip) > 36:
            raise ValueError("Invalid value for `from_ip`, length must be less than or equal to `36`")

        self._from_ip = from_ip

    @property
    def transaction_type(self):
        """
        Gets the transaction_type of this TransactionLogGet.

        :return: The transaction_type of this TransactionLogGet.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """
        Sets the transaction_type of this TransactionLogGet.

        :param transaction_type: The transaction_type of this TransactionLogGet.
        :type: str
        """
        if transaction_type is not None and len(transaction_type) > 255:
            raise ValueError("Invalid value for `transaction_type`, length must be less than or equal to `255`")

        self._transaction_type = transaction_type

    @property
    def transaction_time(self):
        """
        Gets the transaction_time of this TransactionLogGet.

        :return: The transaction_time of this TransactionLogGet.
        :rtype: datetime
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """
        Sets the transaction_time of this TransactionLogGet.

        :param transaction_time: The transaction_time of this TransactionLogGet.
        :type: datetime
        """

        self._transaction_time = transaction_time

    @property
    def license_lrn_uuid(self):
        """
        Gets the license_lrn_uuid of this TransactionLogGet.

        :return: The license_lrn_uuid of this TransactionLogGet.
        :rtype: str
        """
        return self._license_lrn_uuid

    @license_lrn_uuid.setter
    def license_lrn_uuid(self, license_lrn_uuid):
        """
        Sets the license_lrn_uuid of this TransactionLogGet.

        :param license_lrn_uuid: The license_lrn_uuid of this TransactionLogGet.
        :type: str
        """
        if license_lrn_uuid is not None and len(license_lrn_uuid) > 36:
            raise ValueError("Invalid value for `license_lrn_uuid`, length must be less than or equal to `36`")

        self._license_lrn_uuid = license_lrn_uuid

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this TransactionLogGet.

        :return: The transaction_id of this TransactionLogGet.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this TransactionLogGet.

        :param transaction_id: The transaction_id of this TransactionLogGet.
        :type: str
        """
        if transaction_id is not None and len(transaction_id) > 255:
            raise ValueError("Invalid value for `transaction_id`, length must be less than or equal to `255`")

        self._transaction_id = transaction_id

    @property
    def payment_uuid(self):
        """
        Gets the payment_uuid of this TransactionLogGet.

        :return: The payment_uuid of this TransactionLogGet.
        :rtype: str
        """
        return self._payment_uuid

    @payment_uuid.setter
    def payment_uuid(self, payment_uuid):
        """
        Sets the payment_uuid of this TransactionLogGet.

        :param payment_uuid: The payment_uuid of this TransactionLogGet.
        :type: str
        """
        if payment_uuid is not None and len(payment_uuid) > 36:
            raise ValueError("Invalid value for `payment_uuid`, length must be less than or equal to `36`")

        self._payment_uuid = payment_uuid

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
        if not isinstance(other, TransactionLogGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
