# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LicensePeriodGet(object):
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
        'license_uuid': 'str',
        'start_time': 'datetime',
        'user_uuid': 'str',
        'license_period_uuid': 'str',
        'end_time': 'datetime'
    }

    attribute_map = {
        'license_uuid': 'license_uuid',
        'start_time': 'start_time',
        'user_uuid': 'user_uuid',
        'license_period_uuid': 'license_period_uuid',
        'end_time': 'end_time'
    }

    def __init__(self, license_uuid=None, start_time=None, user_uuid=None, license_period_uuid=None, end_time=None):
        """
        LicensePeriodGet - a model defined in Swagger
        """

        self._license_uuid = None
        self._start_time = None
        self._user_uuid = None
        self._license_period_uuid = None
        self._end_time = None

        if license_uuid is not None:
          self.license_uuid = license_uuid
        if start_time is not None:
          self.start_time = start_time
        if user_uuid is not None:
          self.user_uuid = user_uuid
        if license_period_uuid is not None:
          self.license_period_uuid = license_period_uuid
        if end_time is not None:
          self.end_time = end_time

    @property
    def license_uuid(self):
        """
        Gets the license_uuid of this LicensePeriodGet.

        :return: The license_uuid of this LicensePeriodGet.
        :rtype: str
        """
        return self._license_uuid

    @license_uuid.setter
    def license_uuid(self, license_uuid):
        """
        Sets the license_uuid of this LicensePeriodGet.

        :param license_uuid: The license_uuid of this LicensePeriodGet.
        :type: str
        """
        if license_uuid is not None and len(license_uuid) > 36:
            raise ValueError("Invalid value for `license_uuid`, length must be less than or equal to `36`")

        self._license_uuid = license_uuid

    @property
    def start_time(self):
        """
        Gets the start_time of this LicensePeriodGet.

        :return: The start_time of this LicensePeriodGet.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this LicensePeriodGet.

        :param start_time: The start_time of this LicensePeriodGet.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def user_uuid(self):
        """
        Gets the user_uuid of this LicensePeriodGet.

        :return: The user_uuid of this LicensePeriodGet.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """
        Sets the user_uuid of this LicensePeriodGet.

        :param user_uuid: The user_uuid of this LicensePeriodGet.
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def license_period_uuid(self):
        """
        Gets the license_period_uuid of this LicensePeriodGet.

        :return: The license_period_uuid of this LicensePeriodGet.
        :rtype: str
        """
        return self._license_period_uuid

    @license_period_uuid.setter
    def license_period_uuid(self, license_period_uuid):
        """
        Sets the license_period_uuid of this LicensePeriodGet.

        :param license_period_uuid: The license_period_uuid of this LicensePeriodGet.
        :type: str
        """
        if license_period_uuid is not None and len(license_period_uuid) > 36:
            raise ValueError("Invalid value for `license_period_uuid`, length must be less than or equal to `36`")

        self._license_period_uuid = license_period_uuid

    @property
    def end_time(self):
        """
        Gets the end_time of this LicensePeriodGet.

        :return: The end_time of this LicensePeriodGet.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this LicensePeriodGet.

        :param end_time: The end_time of this LicensePeriodGet.
        :type: datetime
        """

        self._end_time = end_time

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
        if not isinstance(other, LicensePeriodGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
