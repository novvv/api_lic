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


class EmailTemplate(object):
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
        'email_cc': 'str',
        'name': 'str',
        'email_from': 'str',
        'subject': 'str',
        'content_html': 'str',
        'hint': 'str',
        'content_text': 'str'
    }

    attribute_map = {
        'email_cc': 'email_cc',
        'name': 'name',
        'email_from': 'email_from',
        'subject': 'subject',
        'content_html': 'content_html',
        'hint': 'hint',
        'content_text': 'content_text'
    }

    def __init__(self, email_cc=None, name=None, email_from=None, subject=None, content_html=None, hint=None, content_text=None):
        """
        EmailTemplate - a model defined in Swagger
        """

        self._email_cc = None
        self._name = None
        self._email_from = None
        self._subject = None
        self._content_html = None
        self._hint = None
        self._content_text = None

        if email_cc is not None:
          self.email_cc = email_cc
        if name is not None:
          self.name = name
        if email_from is not None:
          self.email_from = email_from
        if subject is not None:
          self.subject = subject
        if content_html is not None:
          self.content_html = content_html
        if hint is not None:
          self.hint = hint
        if content_text is not None:
          self.content_text = content_text

    @property
    def email_cc(self):
        """
        Gets the email_cc of this EmailTemplate.

        :return: The email_cc of this EmailTemplate.
        :rtype: str
        """
        return self._email_cc

    @email_cc.setter
    def email_cc(self, email_cc):
        """
        Sets the email_cc of this EmailTemplate.

        :param email_cc: The email_cc of this EmailTemplate.
        :type: str
        """

        self._email_cc = email_cc

    @property
    def name(self):
        """
        Gets the name of this EmailTemplate.

        :return: The name of this EmailTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EmailTemplate.

        :param name: The name of this EmailTemplate.
        :type: str
        """

        self._name = name

    @property
    def email_from(self):
        """
        Gets the email_from of this EmailTemplate.

        :return: The email_from of this EmailTemplate.
        :rtype: str
        """
        return self._email_from

    @email_from.setter
    def email_from(self, email_from):
        """
        Sets the email_from of this EmailTemplate.

        :param email_from: The email_from of this EmailTemplate.
        :type: str
        """

        self._email_from = email_from

    @property
    def subject(self):
        """
        Gets the subject of this EmailTemplate.

        :return: The subject of this EmailTemplate.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this EmailTemplate.

        :param subject: The subject of this EmailTemplate.
        :type: str
        """

        self._subject = subject

    @property
    def content_html(self):
        """
        Gets the content_html of this EmailTemplate.

        :return: The content_html of this EmailTemplate.
        :rtype: str
        """
        return self._content_html

    @content_html.setter
    def content_html(self, content_html):
        """
        Sets the content_html of this EmailTemplate.

        :param content_html: The content_html of this EmailTemplate.
        :type: str
        """

        self._content_html = content_html

    @property
    def hint(self):
        """
        Gets the hint of this EmailTemplate.

        :return: The hint of this EmailTemplate.
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """
        Sets the hint of this EmailTemplate.

        :param hint: The hint of this EmailTemplate.
        :type: str
        """

        self._hint = hint

    @property
    def content_text(self):
        """
        Gets the content_text of this EmailTemplate.

        :return: The content_text of this EmailTemplate.
        :rtype: str
        """
        return self._content_text

    @content_text.setter
    def content_text(self, content_text):
        """
        Sets the content_text of this EmailTemplate.

        :param content_text: The content_text of this EmailTemplate.
        :type: str
        """

        self._content_text = content_text

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
        if not isinstance(other, EmailTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
