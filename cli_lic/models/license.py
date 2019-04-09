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


class License(object):
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
        'license_switch': 'LicenseSwitch',
        'license_lrn': 'LicenseLrn'
    }

    attribute_map = {
        'license_switch': 'license_switch',
        'license_lrn': 'license_lrn'
    }

    def __init__(self, license_switch=None, license_lrn=None):
        """
        License - a model defined in Swagger
        """

        self._license_switch = None
        self._license_lrn = None

        if license_switch is not None:
          self.license_switch = license_switch
        if license_lrn is not None:
          self.license_lrn = license_lrn

    @property
    def license_switch(self):
        """
        Gets the license_switch of this License.

        :return: The license_switch of this License.
        :rtype: LicenseSwitch
        """
        return self._license_switch

    @license_switch.setter
    def license_switch(self, license_switch):
        """
        Sets the license_switch of this License.

        :param license_switch: The license_switch of this License.
        :type: LicenseSwitch
        """

        self._license_switch = license_switch

    @property
    def license_lrn(self):
        """
        Gets the license_lrn of this License.

        :return: The license_lrn of this License.
        :rtype: LicenseLrn
        """
        return self._license_lrn

    @license_lrn.setter
    def license_lrn(self, license_lrn):
        """
        Sets the license_lrn of this License.

        :param license_lrn: The license_lrn of this License.
        :type: LicenseLrn
        """

        self._license_lrn = license_lrn

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
        if not isinstance(other, License):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
