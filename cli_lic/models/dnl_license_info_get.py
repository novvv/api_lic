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


class DnlLicenseInfoGet(object):
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
        'ss_bind_port': 'int',
        'max_cps': 'int',
        'switch_uuid': 'str',
        'create_user': 'int',
        'port_limit': 'int',
        'ss_name': 'str',
        'switch_ip': 'str',
        'expire_date': 'datetime',
        'id': 'int',
        'ss_bind_mac': 'str',
        'carrier_name': 'str',
        'ss_bind_ip': 'str',
        'recv_port': 'int',
        'status': 'bool',
        'expires': 'int',
        'plan_name': 'str',
        'start_date': 'datetime',
        'ss_type': 'int'
    }

    attribute_map = {
        'ss_bind_port': 'ss_bind_port',
        'max_cps': 'max_cps',
        'switch_uuid': 'switch_uuid',
        'create_user': 'create_user',
        'port_limit': 'port_limit',
        'ss_name': 'ss_name',
        'switch_ip': 'switch_ip',
        'expire_date': 'expire_date',
        'id': 'id',
        'ss_bind_mac': 'ss_bind_mac',
        'carrier_name': 'carrier_name',
        'ss_bind_ip': 'ss_bind_ip',
        'recv_port': 'recv_port',
        'status': 'status',
        'expires': 'expires',
        'plan_name': 'plan_name',
        'start_date': 'start_date',
        'ss_type': 'ss_type'
    }

    def __init__(self, ss_bind_port=None, max_cps=None, switch_uuid=None, create_user=None, port_limit=None, ss_name=None, switch_ip=None, expire_date=None, id=None, ss_bind_mac=None, carrier_name=None, ss_bind_ip=None, recv_port=None, status=None, expires=None, plan_name=None, start_date=None, ss_type=None):
        """
        DnlLicenseInfoGet - a model defined in Swagger
        """

        self._ss_bind_port = None
        self._max_cps = None
        self._switch_uuid = None
        self._create_user = None
        self._port_limit = None
        self._ss_name = None
        self._switch_ip = None
        self._expire_date = None
        self._id = None
        self._ss_bind_mac = None
        self._carrier_name = None
        self._ss_bind_ip = None
        self._recv_port = None
        self._status = None
        self._expires = None
        self._plan_name = None
        self._start_date = None
        self._ss_type = None

        if ss_bind_port is not None:
          self.ss_bind_port = ss_bind_port
        if max_cps is not None:
          self.max_cps = max_cps
        if switch_uuid is not None:
          self.switch_uuid = switch_uuid
        if create_user is not None:
          self.create_user = create_user
        if port_limit is not None:
          self.port_limit = port_limit
        if ss_name is not None:
          self.ss_name = ss_name
        if switch_ip is not None:
          self.switch_ip = switch_ip
        if expire_date is not None:
          self.expire_date = expire_date
        if id is not None:
          self.id = id
        if ss_bind_mac is not None:
          self.ss_bind_mac = ss_bind_mac
        if carrier_name is not None:
          self.carrier_name = carrier_name
        if ss_bind_ip is not None:
          self.ss_bind_ip = ss_bind_ip
        if recv_port is not None:
          self.recv_port = recv_port
        if status is not None:
          self.status = status
        if expires is not None:
          self.expires = expires
        if plan_name is not None:
          self.plan_name = plan_name
        if start_date is not None:
          self.start_date = start_date
        if ss_type is not None:
          self.ss_type = ss_type

    @property
    def ss_bind_port(self):
        """
        Gets the ss_bind_port of this DnlLicenseInfoGet.

        :return: The ss_bind_port of this DnlLicenseInfoGet.
        :rtype: int
        """
        return self._ss_bind_port

    @ss_bind_port.setter
    def ss_bind_port(self, ss_bind_port):
        """
        Sets the ss_bind_port of this DnlLicenseInfoGet.

        :param ss_bind_port: The ss_bind_port of this DnlLicenseInfoGet.
        :type: int
        """

        self._ss_bind_port = ss_bind_port

    @property
    def max_cps(self):
        """
        Gets the max_cps of this DnlLicenseInfoGet.

        :return: The max_cps of this DnlLicenseInfoGet.
        :rtype: int
        """
        return self._max_cps

    @max_cps.setter
    def max_cps(self, max_cps):
        """
        Sets the max_cps of this DnlLicenseInfoGet.

        :param max_cps: The max_cps of this DnlLicenseInfoGet.
        :type: int
        """

        self._max_cps = max_cps

    @property
    def switch_uuid(self):
        """
        Gets the switch_uuid of this DnlLicenseInfoGet.

        :return: The switch_uuid of this DnlLicenseInfoGet.
        :rtype: str
        """
        return self._switch_uuid

    @switch_uuid.setter
    def switch_uuid(self, switch_uuid):
        """
        Sets the switch_uuid of this DnlLicenseInfoGet.

        :param switch_uuid: The switch_uuid of this DnlLicenseInfoGet.
        :type: str
        """

        self._switch_uuid = switch_uuid

    @property
    def create_user(self):
        """
        Gets the create_user of this DnlLicenseInfoGet.

        :return: The create_user of this DnlLicenseInfoGet.
        :rtype: int
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """
        Sets the create_user of this DnlLicenseInfoGet.

        :param create_user: The create_user of this DnlLicenseInfoGet.
        :type: int
        """

        self._create_user = create_user

    @property
    def port_limit(self):
        """
        Gets the port_limit of this DnlLicenseInfoGet.

        :return: The port_limit of this DnlLicenseInfoGet.
        :rtype: int
        """
        return self._port_limit

    @port_limit.setter
    def port_limit(self, port_limit):
        """
        Sets the port_limit of this DnlLicenseInfoGet.

        :param port_limit: The port_limit of this DnlLicenseInfoGet.
        :type: int
        """

        self._port_limit = port_limit

    @property
    def ss_name(self):
        """
        Gets the ss_name of this DnlLicenseInfoGet.

        :return: The ss_name of this DnlLicenseInfoGet.
        :rtype: str
        """
        return self._ss_name

    @ss_name.setter
    def ss_name(self, ss_name):
        """
        Sets the ss_name of this DnlLicenseInfoGet.

        :param ss_name: The ss_name of this DnlLicenseInfoGet.
        :type: str
        """
        if ss_name is not None and len(ss_name) > 100:
            raise ValueError("Invalid value for `ss_name`, length must be less than or equal to `100`")

        self._ss_name = ss_name

    @property
    def switch_ip(self):
        """
        Gets the switch_ip of this DnlLicenseInfoGet.

        :return: The switch_ip of this DnlLicenseInfoGet.
        :rtype: str
        """
        return self._switch_ip

    @switch_ip.setter
    def switch_ip(self, switch_ip):
        """
        Sets the switch_ip of this DnlLicenseInfoGet.

        :param switch_ip: The switch_ip of this DnlLicenseInfoGet.
        :type: str
        """

        self._switch_ip = switch_ip

    @property
    def expire_date(self):
        """
        Gets the expire_date of this DnlLicenseInfoGet.

        :return: The expire_date of this DnlLicenseInfoGet.
        :rtype: datetime
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """
        Sets the expire_date of this DnlLicenseInfoGet.

        :param expire_date: The expire_date of this DnlLicenseInfoGet.
        :type: datetime
        """

        self._expire_date = expire_date

    @property
    def id(self):
        """
        Gets the id of this DnlLicenseInfoGet.

        :return: The id of this DnlLicenseInfoGet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DnlLicenseInfoGet.

        :param id: The id of this DnlLicenseInfoGet.
        :type: int
        """

        self._id = id

    @property
    def ss_bind_mac(self):
        """
        Gets the ss_bind_mac of this DnlLicenseInfoGet.

        :return: The ss_bind_mac of this DnlLicenseInfoGet.
        :rtype: str
        """
        return self._ss_bind_mac

    @ss_bind_mac.setter
    def ss_bind_mac(self, ss_bind_mac):
        """
        Sets the ss_bind_mac of this DnlLicenseInfoGet.

        :param ss_bind_mac: The ss_bind_mac of this DnlLicenseInfoGet.
        :type: str
        """
        if ss_bind_mac is not None and len(ss_bind_mac) > 18:
            raise ValueError("Invalid value for `ss_bind_mac`, length must be less than or equal to `18`")

        self._ss_bind_mac = ss_bind_mac

    @property
    def carrier_name(self):
        """
        Gets the carrier_name of this DnlLicenseInfoGet.

        :return: The carrier_name of this DnlLicenseInfoGet.
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """
        Sets the carrier_name of this DnlLicenseInfoGet.

        :param carrier_name: The carrier_name of this DnlLicenseInfoGet.
        :type: str
        """
        if carrier_name is not None and len(carrier_name) > 100:
            raise ValueError("Invalid value for `carrier_name`, length must be less than or equal to `100`")

        self._carrier_name = carrier_name

    @property
    def ss_bind_ip(self):
        """
        Gets the ss_bind_ip of this DnlLicenseInfoGet.

        :return: The ss_bind_ip of this DnlLicenseInfoGet.
        :rtype: str
        """
        return self._ss_bind_ip

    @ss_bind_ip.setter
    def ss_bind_ip(self, ss_bind_ip):
        """
        Sets the ss_bind_ip of this DnlLicenseInfoGet.

        :param ss_bind_ip: The ss_bind_ip of this DnlLicenseInfoGet.
        :type: str
        """
        if ss_bind_ip is not None and len(ss_bind_ip) > 16:
            raise ValueError("Invalid value for `ss_bind_ip`, length must be less than or equal to `16`")

        self._ss_bind_ip = ss_bind_ip

    @property
    def recv_port(self):
        """
        Gets the recv_port of this DnlLicenseInfoGet.

        :return: The recv_port of this DnlLicenseInfoGet.
        :rtype: int
        """
        return self._recv_port

    @recv_port.setter
    def recv_port(self, recv_port):
        """
        Sets the recv_port of this DnlLicenseInfoGet.

        :param recv_port: The recv_port of this DnlLicenseInfoGet.
        :type: int
        """

        self._recv_port = recv_port

    @property
    def status(self):
        """
        Gets the status of this DnlLicenseInfoGet.

        :return: The status of this DnlLicenseInfoGet.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DnlLicenseInfoGet.

        :param status: The status of this DnlLicenseInfoGet.
        :type: bool
        """

        self._status = status

    @property
    def expires(self):
        """
        Gets the expires of this DnlLicenseInfoGet.

        :return: The expires of this DnlLicenseInfoGet.
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this DnlLicenseInfoGet.

        :param expires: The expires of this DnlLicenseInfoGet.
        :type: int
        """

        self._expires = expires

    @property
    def plan_name(self):
        """
        Gets the plan_name of this DnlLicenseInfoGet.

        :return: The plan_name of this DnlLicenseInfoGet.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """
        Sets the plan_name of this DnlLicenseInfoGet.

        :param plan_name: The plan_name of this DnlLicenseInfoGet.
        :type: str
        """

        self._plan_name = plan_name

    @property
    def start_date(self):
        """
        Gets the start_date of this DnlLicenseInfoGet.

        :return: The start_date of this DnlLicenseInfoGet.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this DnlLicenseInfoGet.

        :param start_date: The start_date of this DnlLicenseInfoGet.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def ss_type(self):
        """
        Gets the ss_type of this DnlLicenseInfoGet.

        :return: The ss_type of this DnlLicenseInfoGet.
        :rtype: int
        """
        return self._ss_type

    @ss_type.setter
    def ss_type(self, ss_type):
        """
        Sets the ss_type of this DnlLicenseInfoGet.

        :param ss_type: The ss_type of this DnlLicenseInfoGet.
        :type: int
        """

        self._ss_type = ss_type

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
        if not isinstance(other, DnlLicenseInfoGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
