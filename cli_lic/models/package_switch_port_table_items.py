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


class PackageSwitchPortTableItems(object):
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
        'on_premise': 'PackageSwitchPort',
        'switch_port': 'int',
        'hosted_switch': 'PackageSwitchPort',
        'one_time': 'PackageSwitchPort'
    }

    attribute_map = {
        'on_premise': 'on_premise',
        'switch_port': 'switch_port',
        'hosted_switch': 'hosted_switch',
        'one_time': 'one_time'
    }

    def __init__(self, on_premise=None, switch_port=None, hosted_switch=None, one_time=None):
        """
        PackageSwitchPortTableItems - a model defined in Swagger
        """

        self._on_premise = None
        self._switch_port = None
        self._hosted_switch = None
        self._one_time = None

        if on_premise is not None:
          self.on_premise = on_premise
        if switch_port is not None:
          self.switch_port = switch_port
        if hosted_switch is not None:
          self.hosted_switch = hosted_switch
        if one_time is not None:
          self.one_time = one_time

    @property
    def on_premise(self):
        """
        Gets the on_premise of this PackageSwitchPortTableItems.

        :return: The on_premise of this PackageSwitchPortTableItems.
        :rtype: PackageSwitchPort
        """
        return self._on_premise

    @on_premise.setter
    def on_premise(self, on_premise):
        """
        Sets the on_premise of this PackageSwitchPortTableItems.

        :param on_premise: The on_premise of this PackageSwitchPortTableItems.
        :type: PackageSwitchPort
        """

        self._on_premise = on_premise

    @property
    def switch_port(self):
        """
        Gets the switch_port of this PackageSwitchPortTableItems.

        :return: The switch_port of this PackageSwitchPortTableItems.
        :rtype: int
        """
        return self._switch_port

    @switch_port.setter
    def switch_port(self, switch_port):
        """
        Sets the switch_port of this PackageSwitchPortTableItems.

        :param switch_port: The switch_port of this PackageSwitchPortTableItems.
        :type: int
        """

        self._switch_port = switch_port

    @property
    def hosted_switch(self):
        """
        Gets the hosted_switch of this PackageSwitchPortTableItems.

        :return: The hosted_switch of this PackageSwitchPortTableItems.
        :rtype: PackageSwitchPort
        """
        return self._hosted_switch

    @hosted_switch.setter
    def hosted_switch(self, hosted_switch):
        """
        Sets the hosted_switch of this PackageSwitchPortTableItems.

        :param hosted_switch: The hosted_switch of this PackageSwitchPortTableItems.
        :type: PackageSwitchPort
        """

        self._hosted_switch = hosted_switch

    @property
    def one_time(self):
        """
        Gets the one_time of this PackageSwitchPortTableItems.

        :return: The one_time of this PackageSwitchPortTableItems.
        :rtype: PackageSwitchPort
        """
        return self._one_time

    @one_time.setter
    def one_time(self, one_time):
        """
        Sets the one_time of this PackageSwitchPortTableItems.

        :param one_time: The one_time of this PackageSwitchPortTableItems.
        :type: PackageSwitchPort
        """

        self._one_time = one_time

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
        if not isinstance(other, PackageSwitchPortTableItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
