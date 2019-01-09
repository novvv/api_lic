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


class DnlLicenseInfo(object):
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
        'carrier_name': 'str',
        'ss_bind_port': 'int',
        'ss_name': 'str',
        'ss_bind_mac': 'str',
        'update_time': 'datetime',
        'ss_bind_ip': 'str',
        'uuid': 'str',
        'ss_type': 'int',
        'end_time': 'datetime',
        'max_cps': 'int',
        'start_time': 'datetime',
        'recv_ip': 'str',
        'create_time': 'datetime',
        'expires': 'int',
        'create_user': 'int',
        'recv_port': 'int',
        'status': 'int',
        'max_cap': 'int'
    }

    attribute_map = {
        'carrier_name': 'carrier_name',
        'ss_bind_port': 'ss_bind_port',
        'ss_name': 'ss_name',
        'ss_bind_mac': 'ss_bind_mac',
        'update_time': 'update_time',
        'ss_bind_ip': 'ss_bind_ip',
        'uuid': 'uuid',
        'ss_type': 'ss_type',
        'end_time': 'end_time',
        'max_cps': 'max_cps',
        'start_time': 'start_time',
        'recv_ip': 'recv_ip',
        'create_time': 'create_time',
        'expires': 'expires',
        'create_user': 'create_user',
        'recv_port': 'recv_port',
        'status': 'status',
        'max_cap': 'max_cap'
    }

    def __init__(self, carrier_name=None, ss_bind_port=None, ss_name=None, ss_bind_mac=None, update_time=None, ss_bind_ip=None, uuid=None, ss_type=None, end_time=None, max_cps=None, start_time=None, recv_ip=None, create_time=None, expires=None, create_user=None, recv_port=None, status=None, max_cap=None):
        """
        DnlLicenseInfo - a model defined in Swagger
        """

        self._carrier_name = None
        self._ss_bind_port = None
        self._ss_name = None
        self._ss_bind_mac = None
        self._update_time = None
        self._ss_bind_ip = None
        self._uuid = None
        self._ss_type = None
        self._end_time = None
        self._max_cps = None
        self._start_time = None
        self._recv_ip = None
        self._create_time = None
        self._expires = None
        self._create_user = None
        self._recv_port = None
        self._status = None
        self._max_cap = None

        if carrier_name is not None:
          self.carrier_name = carrier_name
        if ss_bind_port is not None:
          self.ss_bind_port = ss_bind_port
        if ss_name is not None:
          self.ss_name = ss_name
        if ss_bind_mac is not None:
          self.ss_bind_mac = ss_bind_mac
        if update_time is not None:
          self.update_time = update_time
        if ss_bind_ip is not None:
          self.ss_bind_ip = ss_bind_ip
        if uuid is not None:
          self.uuid = uuid
        if ss_type is not None:
          self.ss_type = ss_type
        if end_time is not None:
          self.end_time = end_time
        if max_cps is not None:
          self.max_cps = max_cps
        if start_time is not None:
          self.start_time = start_time
        if recv_ip is not None:
          self.recv_ip = recv_ip
        if create_time is not None:
          self.create_time = create_time
        if expires is not None:
          self.expires = expires
        if create_user is not None:
          self.create_user = create_user
        if recv_port is not None:
          self.recv_port = recv_port
        if status is not None:
          self.status = status
        if max_cap is not None:
          self.max_cap = max_cap

    @property
    def carrier_name(self):
        """
        Gets the carrier_name of this DnlLicenseInfo.

        :return: The carrier_name of this DnlLicenseInfo.
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """
        Sets the carrier_name of this DnlLicenseInfo.

        :param carrier_name: The carrier_name of this DnlLicenseInfo.
        :type: str
        """
        if carrier_name is not None and len(carrier_name) > 100:
            raise ValueError("Invalid value for `carrier_name`, length must be less than or equal to `100`")

        self._carrier_name = carrier_name

    @property
    def ss_bind_port(self):
        """
        Gets the ss_bind_port of this DnlLicenseInfo.

        :return: The ss_bind_port of this DnlLicenseInfo.
        :rtype: int
        """
        return self._ss_bind_port

    @ss_bind_port.setter
    def ss_bind_port(self, ss_bind_port):
        """
        Sets the ss_bind_port of this DnlLicenseInfo.

        :param ss_bind_port: The ss_bind_port of this DnlLicenseInfo.
        :type: int
        """

        self._ss_bind_port = ss_bind_port

    @property
    def ss_name(self):
        """
        Gets the ss_name of this DnlLicenseInfo.

        :return: The ss_name of this DnlLicenseInfo.
        :rtype: str
        """
        return self._ss_name

    @ss_name.setter
    def ss_name(self, ss_name):
        """
        Sets the ss_name of this DnlLicenseInfo.

        :param ss_name: The ss_name of this DnlLicenseInfo.
        :type: str
        """
        if ss_name is not None and len(ss_name) > 100:
            raise ValueError("Invalid value for `ss_name`, length must be less than or equal to `100`")

        self._ss_name = ss_name

    @property
    def ss_bind_mac(self):
        """
        Gets the ss_bind_mac of this DnlLicenseInfo.

        :return: The ss_bind_mac of this DnlLicenseInfo.
        :rtype: str
        """
        return self._ss_bind_mac

    @ss_bind_mac.setter
    def ss_bind_mac(self, ss_bind_mac):
        """
        Sets the ss_bind_mac of this DnlLicenseInfo.

        :param ss_bind_mac: The ss_bind_mac of this DnlLicenseInfo.
        :type: str
        """
        if ss_bind_mac is not None and len(ss_bind_mac) > 18:
            raise ValueError("Invalid value for `ss_bind_mac`, length must be less than or equal to `18`")

        self._ss_bind_mac = ss_bind_mac

    @property
    def update_time(self):
        """
        Gets the update_time of this DnlLicenseInfo.

        :return: The update_time of this DnlLicenseInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """
        Sets the update_time of this DnlLicenseInfo.

        :param update_time: The update_time of this DnlLicenseInfo.
        :type: datetime
        """

        self._update_time = update_time

    @property
    def ss_bind_ip(self):
        """
        Gets the ss_bind_ip of this DnlLicenseInfo.

        :return: The ss_bind_ip of this DnlLicenseInfo.
        :rtype: str
        """
        return self._ss_bind_ip

    @ss_bind_ip.setter
    def ss_bind_ip(self, ss_bind_ip):
        """
        Sets the ss_bind_ip of this DnlLicenseInfo.

        :param ss_bind_ip: The ss_bind_ip of this DnlLicenseInfo.
        :type: str
        """
        if ss_bind_ip is not None and len(ss_bind_ip) > 16:
            raise ValueError("Invalid value for `ss_bind_ip`, length must be less than or equal to `16`")

        self._ss_bind_ip = ss_bind_ip

    @property
    def uuid(self):
        """
        Gets the uuid of this DnlLicenseInfo.

        :return: The uuid of this DnlLicenseInfo.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this DnlLicenseInfo.

        :param uuid: The uuid of this DnlLicenseInfo.
        :type: str
        """
        if uuid is not None and len(uuid) > 128:
            raise ValueError("Invalid value for `uuid`, length must be less than or equal to `128`")

        self._uuid = uuid

    @property
    def ss_type(self):
        """
        Gets the ss_type of this DnlLicenseInfo.

        :return: The ss_type of this DnlLicenseInfo.
        :rtype: int
        """
        return self._ss_type

    @ss_type.setter
    def ss_type(self, ss_type):
        """
        Sets the ss_type of this DnlLicenseInfo.

        :param ss_type: The ss_type of this DnlLicenseInfo.
        :type: int
        """

        self._ss_type = ss_type

    @property
    def end_time(self):
        """
        Gets the end_time of this DnlLicenseInfo.

        :return: The end_time of this DnlLicenseInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this DnlLicenseInfo.

        :param end_time: The end_time of this DnlLicenseInfo.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def max_cps(self):
        """
        Gets the max_cps of this DnlLicenseInfo.

        :return: The max_cps of this DnlLicenseInfo.
        :rtype: int
        """
        return self._max_cps

    @max_cps.setter
    def max_cps(self, max_cps):
        """
        Sets the max_cps of this DnlLicenseInfo.

        :param max_cps: The max_cps of this DnlLicenseInfo.
        :type: int
        """

        self._max_cps = max_cps

    @property
    def start_time(self):
        """
        Gets the start_time of this DnlLicenseInfo.

        :return: The start_time of this DnlLicenseInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this DnlLicenseInfo.

        :param start_time: The start_time of this DnlLicenseInfo.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def recv_ip(self):
        """
        Gets the recv_ip of this DnlLicenseInfo.

        :return: The recv_ip of this DnlLicenseInfo.
        :rtype: str
        """
        return self._recv_ip

    @recv_ip.setter
    def recv_ip(self, recv_ip):
        """
        Sets the recv_ip of this DnlLicenseInfo.

        :param recv_ip: The recv_ip of this DnlLicenseInfo.
        :type: str
        """
        if recv_ip is not None and len(recv_ip) > 16:
            raise ValueError("Invalid value for `recv_ip`, length must be less than or equal to `16`")

        self._recv_ip = recv_ip

    @property
    def create_time(self):
        """
        Gets the create_time of this DnlLicenseInfo.

        :return: The create_time of this DnlLicenseInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this DnlLicenseInfo.

        :param create_time: The create_time of this DnlLicenseInfo.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def expires(self):
        """
        Gets the expires of this DnlLicenseInfo.

        :return: The expires of this DnlLicenseInfo.
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this DnlLicenseInfo.

        :param expires: The expires of this DnlLicenseInfo.
        :type: int
        """

        self._expires = expires

    @property
    def create_user(self):
        """
        Gets the create_user of this DnlLicenseInfo.

        :return: The create_user of this DnlLicenseInfo.
        :rtype: int
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """
        Sets the create_user of this DnlLicenseInfo.

        :param create_user: The create_user of this DnlLicenseInfo.
        :type: int
        """

        self._create_user = create_user

    @property
    def recv_port(self):
        """
        Gets the recv_port of this DnlLicenseInfo.

        :return: The recv_port of this DnlLicenseInfo.
        :rtype: int
        """
        return self._recv_port

    @recv_port.setter
    def recv_port(self, recv_port):
        """
        Sets the recv_port of this DnlLicenseInfo.

        :param recv_port: The recv_port of this DnlLicenseInfo.
        :type: int
        """

        self._recv_port = recv_port

    @property
    def status(self):
        """
        Gets the status of this DnlLicenseInfo.

        :return: The status of this DnlLicenseInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DnlLicenseInfo.

        :param status: The status of this DnlLicenseInfo.
        :type: int
        """

        self._status = status

    @property
    def max_cap(self):
        """
        Gets the max_cap of this DnlLicenseInfo.

        :return: The max_cap of this DnlLicenseInfo.
        :rtype: int
        """
        return self._max_cap

    @max_cap.setter
    def max_cap(self, max_cap):
        """
        Sets the max_cap of this DnlLicenseInfo.

        :param max_cap: The max_cap of this DnlLicenseInfo.
        :type: int
        """

        self._max_cap = max_cap

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
        if not isinstance(other, DnlLicenseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
