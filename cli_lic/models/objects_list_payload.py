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


class ObjectsListPayload(object):
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
        'page': 'int',
        'total': 'int',
        'items': 'object',
        'per_page': 'int'
    }

    attribute_map = {
        'page': 'page',
        'total': 'total',
        'items': 'items',
        'per_page': 'per_page'
    }

    def __init__(self, page=None, total=None, items=None, per_page=None):
        """
        ObjectsListPayload - a model defined in Swagger
        """

        self._page = None
        self._total = None
        self._items = None
        self._per_page = None

        if page is not None:
          self.page = page
        if total is not None:
          self.total = total
        if items is not None:
          self.items = items
        if per_page is not None:
          self.per_page = per_page

    @property
    def page(self):
        """
        Gets the page of this ObjectsListPayload.

        :return: The page of this ObjectsListPayload.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page of this ObjectsListPayload.

        :param page: The page of this ObjectsListPayload.
        :type: int
        """

        self._page = page

    @property
    def total(self):
        """
        Gets the total of this ObjectsListPayload.

        :return: The total of this ObjectsListPayload.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this ObjectsListPayload.

        :param total: The total of this ObjectsListPayload.
        :type: int
        """

        self._total = total

    @property
    def items(self):
        """
        Gets the items of this ObjectsListPayload.

        :return: The items of this ObjectsListPayload.
        :rtype: object
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ObjectsListPayload.

        :param items: The items of this ObjectsListPayload.
        :type: object
        """

        self._items = items

    @property
    def per_page(self):
        """
        Gets the per_page of this ObjectsListPayload.

        :return: The per_page of this ObjectsListPayload.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """
        Sets the per_page of this ObjectsListPayload.

        :param per_page: The per_page of this ObjectsListPayload.
        :type: int
        """

        self._per_page = per_page

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
        if not isinstance(other, ObjectsListPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
