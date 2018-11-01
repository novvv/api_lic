# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FalconRestContribFilesFileTmp(object):
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
        'uuid': 'str',
        'uploaded_on': 'datetime',
        'belongs_to_field': 'str',
        'belongs_to_table': 'str',
        'path': 'str',
        'public': 'bool'
    }

    attribute_map = {
        'uuid': 'uuid',
        'uploaded_on': 'uploaded_on',
        'belongs_to_field': 'belongs_to_field',
        'belongs_to_table': 'belongs_to_table',
        'path': 'path',
        'public': 'public'
    }

    def __init__(self, uuid=None, uploaded_on=None, belongs_to_field=None, belongs_to_table=None, path=None, public=None):
        """
        FalconRestContribFilesFileTmp - a model defined in Swagger
        """

        self._uuid = None
        self._uploaded_on = None
        self._belongs_to_field = None
        self._belongs_to_table = None
        self._path = None
        self._public = None

        if uuid is not None:
          self.uuid = uuid
        if uploaded_on is not None:
          self.uploaded_on = uploaded_on
        self.belongs_to_field = belongs_to_field
        self.belongs_to_table = belongs_to_table
        self.path = path
        if public is not None:
          self.public = public

    @property
    def uuid(self):
        """
        Gets the uuid of this FalconRestContribFilesFileTmp.

        :return: The uuid of this FalconRestContribFilesFileTmp.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this FalconRestContribFilesFileTmp.

        :param uuid: The uuid of this FalconRestContribFilesFileTmp.
        :type: str
        """
        if uuid is not None and len(uuid) > 36:
            raise ValueError("Invalid value for `uuid`, length must be less than or equal to `36`")

        self._uuid = uuid

    @property
    def uploaded_on(self):
        """
        Gets the uploaded_on of this FalconRestContribFilesFileTmp.

        :return: The uploaded_on of this FalconRestContribFilesFileTmp.
        :rtype: datetime
        """
        return self._uploaded_on

    @uploaded_on.setter
    def uploaded_on(self, uploaded_on):
        """
        Sets the uploaded_on of this FalconRestContribFilesFileTmp.

        :param uploaded_on: The uploaded_on of this FalconRestContribFilesFileTmp.
        :type: datetime
        """

        self._uploaded_on = uploaded_on

    @property
    def belongs_to_field(self):
        """
        Gets the belongs_to_field of this FalconRestContribFilesFileTmp.

        :return: The belongs_to_field of this FalconRestContribFilesFileTmp.
        :rtype: str
        """
        return self._belongs_to_field

    @belongs_to_field.setter
    def belongs_to_field(self, belongs_to_field):
        """
        Sets the belongs_to_field of this FalconRestContribFilesFileTmp.

        :param belongs_to_field: The belongs_to_field of this FalconRestContribFilesFileTmp.
        :type: str
        """
        if belongs_to_field is None:
            raise ValueError("Invalid value for `belongs_to_field`, must not be `None`")
        if belongs_to_field is not None and len(belongs_to_field) > 255:
            raise ValueError("Invalid value for `belongs_to_field`, length must be less than or equal to `255`")

        self._belongs_to_field = belongs_to_field

    @property
    def belongs_to_table(self):
        """
        Gets the belongs_to_table of this FalconRestContribFilesFileTmp.

        :return: The belongs_to_table of this FalconRestContribFilesFileTmp.
        :rtype: str
        """
        return self._belongs_to_table

    @belongs_to_table.setter
    def belongs_to_table(self, belongs_to_table):
        """
        Sets the belongs_to_table of this FalconRestContribFilesFileTmp.

        :param belongs_to_table: The belongs_to_table of this FalconRestContribFilesFileTmp.
        :type: str
        """
        if belongs_to_table is None:
            raise ValueError("Invalid value for `belongs_to_table`, must not be `None`")
        if belongs_to_table is not None and len(belongs_to_table) > 255:
            raise ValueError("Invalid value for `belongs_to_table`, length must be less than or equal to `255`")

        self._belongs_to_table = belongs_to_table

    @property
    def path(self):
        """
        Gets the path of this FalconRestContribFilesFileTmp.

        :return: The path of this FalconRestContribFilesFileTmp.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this FalconRestContribFilesFileTmp.

        :param path: The path of this FalconRestContribFilesFileTmp.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")
        if path is not None and len(path) > 1024:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `1024`")

        self._path = path

    @property
    def public(self):
        """
        Gets the public of this FalconRestContribFilesFileTmp.

        :return: The public of this FalconRestContribFilesFileTmp.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this FalconRestContribFilesFileTmp.

        :param public: The public of this FalconRestContribFilesFileTmp.
        :type: bool
        """

        self._public = public

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
        if not isinstance(other, FalconRestContribFilesFileTmp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
