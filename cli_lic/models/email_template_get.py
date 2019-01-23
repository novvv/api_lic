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


class EmailTemplateGet(object):
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
        'email_from': 'str',
        'content_html': 'str',
        'subject': 'str',
        'name': 'str',
        'content_text': 'str',
        'email_cc': 'str',
        'hint': 'str'
    }

    attribute_map = {
        'email_from': 'email_from',
        'content_html': 'content_html',
        'subject': 'subject',
        'name': 'name',
        'content_text': 'content_text',
        'email_cc': 'email_cc',
        'hint': 'hint'
    }

    def __init__(self, email_from=None, content_html=None, subject=None, name=None, content_text=None, email_cc=None, hint=None):
        """
        EmailTemplateGet - a model defined in Swagger
        """

        self._email_from = None
        self._content_html = None
        self._subject = None
        self._name = None
        self._content_text = None
        self._email_cc = None
        self._hint = None

        if email_from is not None:
          self.email_from = email_from
        if content_html is not None:
          self.content_html = content_html
        if subject is not None:
          self.subject = subject
        if name is not None:
          self.name = name
        if content_text is not None:
          self.content_text = content_text
        if email_cc is not None:
          self.email_cc = email_cc
        if hint is not None:
          self.hint = hint

    @property
    def email_from(self):
        """
        Gets the email_from of this EmailTemplateGet.

        :return: The email_from of this EmailTemplateGet.
        :rtype: str
        """
        return self._email_from

    @email_from.setter
    def email_from(self, email_from):
        """
        Sets the email_from of this EmailTemplateGet.

        :param email_from: The email_from of this EmailTemplateGet.
        :type: str
        """

        self._email_from = email_from

    @property
    def content_html(self):
        """
        Gets the content_html of this EmailTemplateGet.

        :return: The content_html of this EmailTemplateGet.
        :rtype: str
        """
        return self._content_html

    @content_html.setter
    def content_html(self, content_html):
        """
        Sets the content_html of this EmailTemplateGet.

        :param content_html: The content_html of this EmailTemplateGet.
        :type: str
        """

        self._content_html = content_html

    @property
    def subject(self):
        """
        Gets the subject of this EmailTemplateGet.

        :return: The subject of this EmailTemplateGet.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this EmailTemplateGet.

        :param subject: The subject of this EmailTemplateGet.
        :type: str
        """

        self._subject = subject

    @property
    def name(self):
        """
        Gets the name of this EmailTemplateGet.

        :return: The name of this EmailTemplateGet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EmailTemplateGet.

        :param name: The name of this EmailTemplateGet.
        :type: str
        """

        self._name = name

    @property
    def content_text(self):
        """
        Gets the content_text of this EmailTemplateGet.

        :return: The content_text of this EmailTemplateGet.
        :rtype: str
        """
        return self._content_text

    @content_text.setter
    def content_text(self, content_text):
        """
        Sets the content_text of this EmailTemplateGet.

        :param content_text: The content_text of this EmailTemplateGet.
        :type: str
        """

        self._content_text = content_text

    @property
    def email_cc(self):
        """
        Gets the email_cc of this EmailTemplateGet.

        :return: The email_cc of this EmailTemplateGet.
        :rtype: str
        """
        return self._email_cc

    @email_cc.setter
    def email_cc(self, email_cc):
        """
        Sets the email_cc of this EmailTemplateGet.

        :param email_cc: The email_cc of this EmailTemplateGet.
        :type: str
        """

        self._email_cc = email_cc

    @property
    def hint(self):
        """
        Gets the hint of this EmailTemplateGet.

        :return: The hint of this EmailTemplateGet.
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """
        Sets the hint of this EmailTemplateGet.

        :param hint: The hint of this EmailTemplateGet.
        :type: str
        """

        self._hint = hint

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
        if not isinstance(other, EmailTemplateGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
