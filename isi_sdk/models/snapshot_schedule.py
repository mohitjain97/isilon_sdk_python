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


class SnapshotSchedule(object):
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
        'alias': 'str',
        'duration': 'int',
        'name': 'str',
        'path': 'str',
        'pattern': 'str',
        'schedule': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'duration': 'duration',
        'name': 'name',
        'path': 'path',
        'pattern': 'pattern',
        'schedule': 'schedule'
    }

    def __init__(self, alias=None, duration=None, name=None, path=None, pattern=None, schedule=None):  # noqa: E501
        """SnapshotSchedule - a model defined in Swagger"""  # noqa: E501

        self._alias = None
        self._duration = None
        self._name = None
        self._path = None
        self._pattern = None
        self._schedule = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if duration is not None:
            self.duration = duration
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if pattern is not None:
            self.pattern = pattern
        if schedule is not None:
            self.schedule = schedule

    @property
    def alias(self):
        """Gets the alias of this SnapshotSchedule.  # noqa: E501

        Alias name to create for each snapshot.  # noqa: E501

        :return: The alias of this SnapshotSchedule.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this SnapshotSchedule.

        Alias name to create for each snapshot.  # noqa: E501

        :param alias: The alias of this SnapshotSchedule.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def duration(self):
        """Gets the duration of this SnapshotSchedule.  # noqa: E501

        Time in seconds added to creation time to construction expiration time.  # noqa: E501

        :return: The duration of this SnapshotSchedule.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SnapshotSchedule.

        Time in seconds added to creation time to construction expiration time.  # noqa: E501

        :param duration: The duration of this SnapshotSchedule.  # noqa: E501
        :type: int
        """
        if duration is not None and duration < 0:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration = duration

    @property
    def name(self):
        """Gets the name of this SnapshotSchedule.  # noqa: E501

        The schedule name.  # noqa: E501

        :return: The name of this SnapshotSchedule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotSchedule.

        The schedule name.  # noqa: E501

        :param name: The name of this SnapshotSchedule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this SnapshotSchedule.  # noqa: E501

        The /ifs path snapshotted.  # noqa: E501

        :return: The path of this SnapshotSchedule.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SnapshotSchedule.

        The /ifs path snapshotted.  # noqa: E501

        :param path: The path of this SnapshotSchedule.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def pattern(self):
        """Gets the pattern of this SnapshotSchedule.  # noqa: E501

        Pattern expanded with strftime to create snapshot names.  # noqa: E501

        :return: The pattern of this SnapshotSchedule.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this SnapshotSchedule.

        Pattern expanded with strftime to create snapshot names.  # noqa: E501

        :param pattern: The pattern of this SnapshotSchedule.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def schedule(self):
        """Gets the schedule of this SnapshotSchedule.  # noqa: E501

        The isidate compatible natural language description of the schedule.  # noqa: E501

        :return: The schedule of this SnapshotSchedule.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this SnapshotSchedule.

        The isidate compatible natural language description of the schedule.  # noqa: E501

        :param schedule: The schedule of this SnapshotSchedule.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

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
        if not isinstance(other, SnapshotSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
