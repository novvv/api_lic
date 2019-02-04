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


class Notification(object):
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
        'user_uuid': 'str',
        'created_on': 'datetime',
        'subject': 'str',
        'content': 'str'
    }

    attribute_map = {
        'user_uuid': 'user_uuid',
        'created_on': 'created_on',
        'subject': 'subject',
        'content': 'content'
    }

    def __init__(self, user_uuid=None, created_on=None, subject=None, content=None):
        """
        Notification - a model defined in Swagger
        """

        self._user_uuid = None
        self._created_on = None
        self._subject = None
        self._content = None

        if user_uuid is not None:
          self.user_uuid = user_uuid
        if created_on is not None:
          self.created_on = created_on
        if subject is not None:
          self.subject = subject
        if content is not None:
          self.content = content

    @property
    def user_uuid(self):
        """
        Gets the user_uuid of this Notification.

        :return: The user_uuid of this Notification.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """
        Sets the user_uuid of this Notification.

        :param user_uuid: The user_uuid of this Notification.
        :type: str
        """
        if user_uuid is not None and len(user_uuid) > 36:
            raise ValueError("Invalid value for `user_uuid`, length must be less than or equal to `36`")

        self._user_uuid = user_uuid

    @property
    def created_on(self):
        """
        Gets the created_on of this Notification.

        :return: The created_on of this Notification.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this Notification.

        :param created_on: The created_on of this Notification.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def subject(self):
        """
        Gets the subject of this Notification.

        :return: The subject of this Notification.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this Notification.

        :param subject: The subject of this Notification.
        :type: str
        """
        if subject is not None and len(subject) > 64:
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `64`")

        self._subject = subject

    @property
    def content(self):
        """
        Gets the content of this Notification.

        :return: The content of this Notification.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this Notification.

        :param content: The content of this Notification.
        :type: str
        """

        self._content = content

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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
