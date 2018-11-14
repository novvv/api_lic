# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NotificationGet(object):
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
        'content': 'str',
        'notification_uuid': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'user_uuid': 'user_uuid',
        'content': 'content',
        'notification_uuid': 'notification_uuid',
        'subject': 'subject'
    }

    def __init__(self, user_uuid=None, content=None, notification_uuid=None, subject=None):
        """
        NotificationGet - a model defined in Swagger
        """

        self._user_uuid = None
        self._content = None
        self._notification_uuid = None
        self._subject = None

        if user_uuid is not None:
          self.user_uuid = user_uuid
        if content is not None:
          self.content = content
        if notification_uuid is not None:
          self.notification_uuid = notification_uuid
        if subject is not None:
          self.subject = subject

    @property
    def user_uuid(self):
        """
        Gets the user_uuid of this NotificationGet.

        :return: The user_uuid of this NotificationGet.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """
        Sets the user_uuid of this NotificationGet.

        :param user_uuid: The user_uuid of this NotificationGet.
        :type: str
        """
        if user_uuid is not None and len(user_uuid) > 36:
            raise ValueError("Invalid value for `user_uuid`, length must be less than or equal to `36`")

        self._user_uuid = user_uuid

    @property
    def content(self):
        """
        Gets the content of this NotificationGet.

        :return: The content of this NotificationGet.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this NotificationGet.

        :param content: The content of this NotificationGet.
        :type: str
        """

        self._content = content

    @property
    def notification_uuid(self):
        """
        Gets the notification_uuid of this NotificationGet.

        :return: The notification_uuid of this NotificationGet.
        :rtype: str
        """
        return self._notification_uuid

    @notification_uuid.setter
    def notification_uuid(self, notification_uuid):
        """
        Sets the notification_uuid of this NotificationGet.

        :param notification_uuid: The notification_uuid of this NotificationGet.
        :type: str
        """
        if notification_uuid is not None and len(notification_uuid) > 36:
            raise ValueError("Invalid value for `notification_uuid`, length must be less than or equal to `36`")

        self._notification_uuid = notification_uuid

    @property
    def subject(self):
        """
        Gets the subject of this NotificationGet.

        :return: The subject of this NotificationGet.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this NotificationGet.

        :param subject: The subject of this NotificationGet.
        :type: str
        """
        if subject is not None and len(subject) > 64:
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `64`")

        self._subject = subject

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
        if not isinstance(other, NotificationGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
