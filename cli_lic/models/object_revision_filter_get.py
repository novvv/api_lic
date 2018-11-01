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


class ObjectRevisionFilterGet(object):
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
        'restored_from_revision_id': 'int',
        'id': 'int',
        'revision_number': 'int',
        'user_id': 'int',
        'entity_pk': 'str',
        'revision_time': 'datetime',
        'entity_name': 'str',
        'action': 'str',
        'changes': 'list[ObjectRevisionRecordGet]'
    }

    attribute_map = {
        'restored_from_revision_id': 'restored_from_revision_id',
        'id': 'id',
        'revision_number': 'revision_number',
        'user_id': 'user_id',
        'entity_pk': 'entity_pk',
        'revision_time': 'revision_time',
        'entity_name': 'entity_name',
        'action': 'action',
        'changes': 'changes'
    }

    def __init__(self, restored_from_revision_id=None, id=None, revision_number=None, user_id=None, entity_pk=None, revision_time=None, entity_name=None, action=None, changes=None):
        """
        ObjectRevisionFilterGet - a model defined in Swagger
        """

        self._restored_from_revision_id = None
        self._id = None
        self._revision_number = None
        self._user_id = None
        self._entity_pk = None
        self._revision_time = None
        self._entity_name = None
        self._action = None
        self._changes = None

        if restored_from_revision_id is not None:
          self.restored_from_revision_id = restored_from_revision_id
        if id is not None:
          self.id = id
        self.revision_number = revision_number
        self.user_id = user_id
        self.entity_pk = entity_pk
        if revision_time is not None:
          self.revision_time = revision_time
        self.entity_name = entity_name
        if action is not None:
          self.action = action
        if changes is not None:
          self.changes = changes

    @property
    def restored_from_revision_id(self):
        """
        Gets the restored_from_revision_id of this ObjectRevisionFilterGet.

        :return: The restored_from_revision_id of this ObjectRevisionFilterGet.
        :rtype: int
        """
        return self._restored_from_revision_id

    @restored_from_revision_id.setter
    def restored_from_revision_id(self, restored_from_revision_id):
        """
        Sets the restored_from_revision_id of this ObjectRevisionFilterGet.

        :param restored_from_revision_id: The restored_from_revision_id of this ObjectRevisionFilterGet.
        :type: int
        """

        self._restored_from_revision_id = restored_from_revision_id

    @property
    def id(self):
        """
        Gets the id of this ObjectRevisionFilterGet.

        :return: The id of this ObjectRevisionFilterGet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ObjectRevisionFilterGet.

        :param id: The id of this ObjectRevisionFilterGet.
        :type: int
        """

        self._id = id

    @property
    def revision_number(self):
        """
        Gets the revision_number of this ObjectRevisionFilterGet.

        :return: The revision_number of this ObjectRevisionFilterGet.
        :rtype: int
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """
        Sets the revision_number of this ObjectRevisionFilterGet.

        :param revision_number: The revision_number of this ObjectRevisionFilterGet.
        :type: int
        """
        if revision_number is None:
            raise ValueError("Invalid value for `revision_number`, must not be `None`")

        self._revision_number = revision_number

    @property
    def user_id(self):
        """
        Gets the user_id of this ObjectRevisionFilterGet.

        :return: The user_id of this ObjectRevisionFilterGet.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ObjectRevisionFilterGet.

        :param user_id: The user_id of this ObjectRevisionFilterGet.
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id

    @property
    def entity_pk(self):
        """
        Gets the entity_pk of this ObjectRevisionFilterGet.

        :return: The entity_pk of this ObjectRevisionFilterGet.
        :rtype: str
        """
        return self._entity_pk

    @entity_pk.setter
    def entity_pk(self, entity_pk):
        """
        Sets the entity_pk of this ObjectRevisionFilterGet.

        :param entity_pk: The entity_pk of this ObjectRevisionFilterGet.
        :type: str
        """
        if entity_pk is None:
            raise ValueError("Invalid value for `entity_pk`, must not be `None`")
        if entity_pk is not None and len(entity_pk) > 64:
            raise ValueError("Invalid value for `entity_pk`, length must be less than or equal to `64`")

        self._entity_pk = entity_pk

    @property
    def revision_time(self):
        """
        Gets the revision_time of this ObjectRevisionFilterGet.

        :return: The revision_time of this ObjectRevisionFilterGet.
        :rtype: datetime
        """
        return self._revision_time

    @revision_time.setter
    def revision_time(self, revision_time):
        """
        Sets the revision_time of this ObjectRevisionFilterGet.

        :param revision_time: The revision_time of this ObjectRevisionFilterGet.
        :type: datetime
        """

        self._revision_time = revision_time

    @property
    def entity_name(self):
        """
        Gets the entity_name of this ObjectRevisionFilterGet.

        :return: The entity_name of this ObjectRevisionFilterGet.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this ObjectRevisionFilterGet.

        :param entity_name: The entity_name of this ObjectRevisionFilterGet.
        :type: str
        """
        if entity_name is None:
            raise ValueError("Invalid value for `entity_name`, must not be `None`")
        if entity_name is not None and len(entity_name) > 64:
            raise ValueError("Invalid value for `entity_name`, length must be less than or equal to `64`")

        self._entity_name = entity_name

    @property
    def action(self):
        """
        Gets the action of this ObjectRevisionFilterGet.

        :return: The action of this ObjectRevisionFilterGet.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ObjectRevisionFilterGet.

        :param action: The action of this ObjectRevisionFilterGet.
        :type: str
        """
        allowed_values = ["create", "update", "delete", "restore"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def changes(self):
        """
        Gets the changes of this ObjectRevisionFilterGet.

        :return: The changes of this ObjectRevisionFilterGet.
        :rtype: list[ObjectRevisionRecordGet]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """
        Sets the changes of this ObjectRevisionFilterGet.

        :param changes: The changes of this ObjectRevisionFilterGet.
        :type: list[ObjectRevisionRecordGet]
        """

        self._changes = changes

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
        if not isinstance(other, ObjectRevisionFilterGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
