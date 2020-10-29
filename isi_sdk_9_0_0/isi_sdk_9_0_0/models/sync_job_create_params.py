# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SyncJobCreateParams(object):
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
        'action': 'str',
        'id': 'str',
        'log_level': 'str',
        'service_policy': 'bool',
        'skip_copy': 'bool',
        'skip_failover': 'bool',
        'skip_map': 'bool',
        'source_snapshot': 'str',
        'tgt_path': 'str',
        'timestamp': 'int',
        'workers_per_node': 'int'
    }

    attribute_map = {
        'action': 'action',
        'id': 'id',
        'log_level': 'log_level',
        'service_policy': 'service_policy',
        'skip_copy': 'skip_copy',
        'skip_failover': 'skip_failover',
        'skip_map': 'skip_map',
        'source_snapshot': 'source_snapshot',
        'tgt_path': 'tgt_path',
        'timestamp': 'timestamp',
        'workers_per_node': 'workers_per_node'
    }

    def __init__(self, action=None, id=None, log_level=None, service_policy=None, skip_copy=None, skip_failover=None, skip_map=None, source_snapshot=None, tgt_path=None, timestamp=None, workers_per_node=None):  # noqa: E501
        """SyncJobCreateParams - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._id = None
        self._log_level = None
        self._service_policy = None
        self._skip_copy = None
        self._skip_failover = None
        self._skip_map = None
        self._source_snapshot = None
        self._tgt_path = None
        self._timestamp = None
        self._workers_per_node = None
        self.discriminator = None

        if action is not None:
            self.action = action
        self.id = id
        if log_level is not None:
            self.log_level = log_level
        if service_policy is not None:
            self.service_policy = service_policy
        if skip_copy is not None:
            self.skip_copy = skip_copy
        if skip_failover is not None:
            self.skip_failover = skip_failover
        if skip_map is not None:
            self.skip_map = skip_map
        if source_snapshot is not None:
            self.source_snapshot = source_snapshot
        if tgt_path is not None:
            self.tgt_path = tgt_path
        if timestamp is not None:
            self.timestamp = timestamp
        if workers_per_node is not None:
            self.workers_per_node = workers_per_node

    @property
    def action(self):
        """Gets the action of this SyncJobCreateParams.  # noqa: E501

        The action to be taken by this job.  # noqa: E501

        :return: The action of this SyncJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this SyncJobCreateParams.

        The action to be taken by this job.  # noqa: E501

        :param action: The action of this SyncJobCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["resync_prep", "allow_write", "allow_write_revert", "test"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def id(self):
        """Gets the id of this SyncJobCreateParams.  # noqa: E501

        The ID or Name of the policy  # noqa: E501

        :return: The id of this SyncJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SyncJobCreateParams.

        The ID or Name of the policy  # noqa: E501

        :param id: The id of this SyncJobCreateParams.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def log_level(self):
        """Gets the log_level of this SyncJobCreateParams.  # noqa: E501

        Only valid for allow_write, and allow_write_revert; specify the desired logging level, will be stored in the logs for isi_migrate, defaults to 'info'.  # noqa: E501

        :return: The log_level of this SyncJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this SyncJobCreateParams.

        Only valid for allow_write, and allow_write_revert; specify the desired logging level, will be stored in the logs for isi_migrate, defaults to 'info'.  # noqa: E501

        :param log_level: The log_level of this SyncJobCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["fatal", "error", "notice", "info", "copy", "debug", "trace"]  # noqa: E501
        if log_level not in allowed_values:
            raise ValueError(
                "Invalid value for `log_level` ({0}), must be one of {1}"  # noqa: E501
                .format(log_level, allowed_values)
            )

        self._log_level = log_level

    @property
    def service_policy(self):
        """Gets the service_policy of this SyncJobCreateParams.  # noqa: E501

        If true, this is a service replication policy.  # noqa: E501

        :return: The service_policy of this SyncJobCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._service_policy

    @service_policy.setter
    def service_policy(self, service_policy):
        """Sets the service_policy of this SyncJobCreateParams.

        If true, this is a service replication policy.  # noqa: E501

        :param service_policy: The service_policy of this SyncJobCreateParams.  # noqa: E501
        :type: bool
        """

        self._service_policy = service_policy

    @property
    def skip_copy(self):
        """Gets the skip_copy of this SyncJobCreateParams.  # noqa: E501

        Skips the copy phase of the service replication allow-write operation.  # noqa: E501

        :return: The skip_copy of this SyncJobCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._skip_copy

    @skip_copy.setter
    def skip_copy(self, skip_copy):
        """Sets the skip_copy of this SyncJobCreateParams.

        Skips the copy phase of the service replication allow-write operation.  # noqa: E501

        :param skip_copy: The skip_copy of this SyncJobCreateParams.  # noqa: E501
        :type: bool
        """

        self._skip_copy = skip_copy

    @property
    def skip_failover(self):
        """Gets the skip_failover of this SyncJobCreateParams.  # noqa: E501

        Skips the data failover phase of the service replication allow-write operation.  # noqa: E501

        :return: The skip_failover of this SyncJobCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._skip_failover

    @skip_failover.setter
    def skip_failover(self, skip_failover):
        """Sets the skip_failover of this SyncJobCreateParams.

        Skips the data failover phase of the service replication allow-write operation.  # noqa: E501

        :param skip_failover: The skip_failover of this SyncJobCreateParams.  # noqa: E501
        :type: bool
        """

        self._skip_failover = skip_failover

    @property
    def skip_map(self):
        """Gets the skip_map of this SyncJobCreateParams.  # noqa: E501

        Skips the mapping phase of the service replication allow-write operation.  # noqa: E501

        :return: The skip_map of this SyncJobCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._skip_map

    @skip_map.setter
    def skip_map(self, skip_map):
        """Sets the skip_map of this SyncJobCreateParams.

        Skips the mapping phase of the service replication allow-write operation.  # noqa: E501

        :param skip_map: The skip_map of this SyncJobCreateParams.  # noqa: E501
        :type: bool
        """

        self._skip_map = skip_map

    @property
    def source_snapshot(self):
        """Gets the source_snapshot of this SyncJobCreateParams.  # noqa: E501

        An optional snapshot to copy/sync from.  # noqa: E501

        :return: The source_snapshot of this SyncJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._source_snapshot

    @source_snapshot.setter
    def source_snapshot(self, source_snapshot):
        """Sets the source_snapshot of this SyncJobCreateParams.

        An optional snapshot to copy/sync from.  # noqa: E501

        :param source_snapshot: The source_snapshot of this SyncJobCreateParams.  # noqa: E501
        :type: str
        """
        if source_snapshot is not None and len(source_snapshot) > 255:
            raise ValueError("Invalid value for `source_snapshot`, length must be less than or equal to `255`")  # noqa: E501
        if source_snapshot is not None and len(source_snapshot) < 0:
            raise ValueError("Invalid value for `source_snapshot`, length must be greater than or equal to `0`")  # noqa: E501

        self._source_snapshot = source_snapshot

    @property
    def tgt_path(self):
        """Gets the tgt_path of this SyncJobCreateParams.  # noqa: E501

        Specifies the directory to output the service replication files for restoration.  # noqa: E501

        :return: The tgt_path of this SyncJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._tgt_path

    @tgt_path.setter
    def tgt_path(self, tgt_path):
        """Sets the tgt_path of this SyncJobCreateParams.

        Specifies the directory to output the service replication files for restoration.  # noqa: E501

        :param tgt_path: The tgt_path of this SyncJobCreateParams.  # noqa: E501
        :type: str
        """
        if tgt_path is not None and len(tgt_path) > 255:
            raise ValueError("Invalid value for `tgt_path`, length must be less than or equal to `255`")  # noqa: E501
        if tgt_path is not None and len(tgt_path) < 0:
            raise ValueError("Invalid value for `tgt_path`, length must be greater than or equal to `0`")  # noqa: E501

        self._tgt_path = tgt_path

    @property
    def timestamp(self):
        """Gets the timestamp of this SyncJobCreateParams.  # noqa: E501

        Specifies the timestamp of a service replication policy backup to restore from.  # noqa: E501

        :return: The timestamp of this SyncJobCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SyncJobCreateParams.

        Specifies the timestamp of a service replication policy backup to restore from.  # noqa: E501

        :param timestamp: The timestamp of this SyncJobCreateParams.  # noqa: E501
        :type: int
        """
        if timestamp is not None and timestamp > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if timestamp is not None and timestamp < 0:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a value greater than or equal to `0`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def workers_per_node(self):
        """Gets the workers_per_node of this SyncJobCreateParams.  # noqa: E501

        Only valid for allow_write, and allow_write_revert; specify the desired workers per node, defaults to 3.  # noqa: E501

        :return: The workers_per_node of this SyncJobCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._workers_per_node

    @workers_per_node.setter
    def workers_per_node(self, workers_per_node):
        """Sets the workers_per_node of this SyncJobCreateParams.

        Only valid for allow_write, and allow_write_revert; specify the desired workers per node, defaults to 3.  # noqa: E501

        :param workers_per_node: The workers_per_node of this SyncJobCreateParams.  # noqa: E501
        :type: int
        """

        self._workers_per_node = workers_per_node

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
        if not isinstance(other, SyncJobCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other