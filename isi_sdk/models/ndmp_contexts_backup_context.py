# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 5
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NdmpContextsBackupContext(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'context_id': 'str',
        'id': 'str',
        'path': 'str',
        'snapid': 'int',
        'start_time': 'int',
        'status': 'str',
        'total_sessions': 'int',
        'type': 'str'
    }

    attribute_map = {
        'context_id': 'context_id',
        'id': 'id',
        'path': 'path',
        'snapid': 'snapid',
        'start_time': 'start_time',
        'status': 'status',
        'total_sessions': 'total_sessions',
        'type': 'type'
    }

    def __init__(self, context_id=None, id=None, path=None, snapid=None, start_time=None, status=None, total_sessions=None, type=None):  # noqa: E501
        """NdmpContextsBackupContext - a model defined in Swagger"""  # noqa: E501

        self._context_id = None
        self._id = None
        self._path = None
        self._snapid = None
        self._start_time = None
        self._status = None
        self._total_sessions = None
        self._type = None
        self.discriminator = None

        if context_id is not None:
            self.context_id = context_id
        if id is not None:
            self.id = id
        if path is not None:
            self.path = path
        if snapid is not None:
            self.snapid = snapid
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if total_sessions is not None:
            self.total_sessions = total_sessions
        if type is not None:
            self.type = type

    @property
    def context_id(self):
        """Gets the context_id of this NdmpContextsBackupContext.  # noqa: E501

        Context ID  # noqa: E501

        :return: The context_id of this NdmpContextsBackupContext.  # noqa: E501
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """Sets the context_id of this NdmpContextsBackupContext.

        Context ID  # noqa: E501

        :param context_id: The context_id of this NdmpContextsBackupContext.  # noqa: E501
        :type: str
        """

        self._context_id = context_id

    @property
    def id(self):
        """Gets the id of this NdmpContextsBackupContext.  # noqa: E501

        Unique display id.  # noqa: E501

        :return: The id of this NdmpContextsBackupContext.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NdmpContextsBackupContext.

        Unique display id.  # noqa: E501

        :param id: The id of this NdmpContextsBackupContext.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this NdmpContextsBackupContext.  # noqa: E501

        The directory of the backup. This is not applicable to restore contexts.  # noqa: E501

        :return: The path of this NdmpContextsBackupContext.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NdmpContextsBackupContext.

        The directory of the backup. This is not applicable to restore contexts.  # noqa: E501

        :param path: The path of this NdmpContextsBackupContext.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def snapid(self):
        """Gets the snapid of this NdmpContextsBackupContext.  # noqa: E501

        Snapshot ID reserved for the context. This is not applicable to restore contexts.  # noqa: E501

        :return: The snapid of this NdmpContextsBackupContext.  # noqa: E501
        :rtype: int
        """
        return self._snapid

    @snapid.setter
    def snapid(self, snapid):
        """Sets the snapid of this NdmpContextsBackupContext.

        Snapshot ID reserved for the context. This is not applicable to restore contexts.  # noqa: E501

        :param snapid: The snapid of this NdmpContextsBackupContext.  # noqa: E501
        :type: int
        """

        self._snapid = snapid

    @property
    def start_time(self):
        """Gets the start_time of this NdmpContextsBackupContext.  # noqa: E501

        Context creation time  # noqa: E501

        :return: The start_time of this NdmpContextsBackupContext.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this NdmpContextsBackupContext.

        Context creation time  # noqa: E501

        :param start_time: The start_time of this NdmpContextsBackupContext.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this NdmpContextsBackupContext.  # noqa: E501

        Whether the context is active.  # noqa: E501

        :return: The status of this NdmpContextsBackupContext.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NdmpContextsBackupContext.

        Whether the context is active.  # noqa: E501

        :param status: The status of this NdmpContextsBackupContext.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def total_sessions(self):
        """Gets the total_sessions of this NdmpContextsBackupContext.  # noqa: E501

        The number of sessions in the context  # noqa: E501

        :return: The total_sessions of this NdmpContextsBackupContext.  # noqa: E501
        :rtype: int
        """
        return self._total_sessions

    @total_sessions.setter
    def total_sessions(self, total_sessions):
        """Sets the total_sessions of this NdmpContextsBackupContext.

        The number of sessions in the context  # noqa: E501

        :param total_sessions: The total_sessions of this NdmpContextsBackupContext.  # noqa: E501
        :type: int
        """

        self._total_sessions = total_sessions

    @property
    def type(self):
        """Gets the type of this NdmpContextsBackupContext.  # noqa: E501

        Type of context; It can be bre, backup, and restore  # noqa: E501

        :return: The type of this NdmpContextsBackupContext.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NdmpContextsBackupContext.

        Type of context; It can be bre, backup, and restore  # noqa: E501

        :param type: The type of this NdmpContextsBackupContext.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NdmpContextsBackupContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
