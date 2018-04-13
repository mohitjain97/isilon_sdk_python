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

from isi_sdk_8_1_0.models.debug_stats_handler import DebugStatsHandler  # noqa: F401,E501
from isi_sdk_8_1_0.models.debug_stats_unknown import DebugStatsUnknown  # noqa: F401,E501


class DebugStats(object):
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
        'describe': 'DebugStatsUnknown',
        'unknown': 'DebugStatsUnknown',
        'handlers': 'list[DebugStatsHandler]'
    }

    attribute_map = {
        'describe': 'DESCRIBE',
        'unknown': 'UNKNOWN',
        'handlers': 'handlers'
    }

    def __init__(self, describe=None, unknown=None, handlers=None):  # noqa: E501
        """DebugStats - a model defined in Swagger"""  # noqa: E501

        self._describe = None
        self._unknown = None
        self._handlers = None
        self.discriminator = None

        if describe is not None:
            self.describe = describe
        if unknown is not None:
            self.unknown = unknown
        if handlers is not None:
            self.handlers = handlers

    @property
    def describe(self):
        """Gets the describe of this DebugStats.  # noqa: E501

        Per-method statistics.  # noqa: E501

        :return: The describe of this DebugStats.  # noqa: E501
        :rtype: DebugStatsUnknown
        """
        return self._describe

    @describe.setter
    def describe(self, describe):
        """Sets the describe of this DebugStats.

        Per-method statistics.  # noqa: E501

        :param describe: The describe of this DebugStats.  # noqa: E501
        :type: DebugStatsUnknown
        """

        self._describe = describe

    @property
    def unknown(self):
        """Gets the unknown of this DebugStats.  # noqa: E501

        Per-method statistics.  # noqa: E501

        :return: The unknown of this DebugStats.  # noqa: E501
        :rtype: DebugStatsUnknown
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this DebugStats.

        Per-method statistics.  # noqa: E501

        :param unknown: The unknown of this DebugStats.  # noqa: E501
        :type: DebugStatsUnknown
        """

        self._unknown = unknown

    @property
    def handlers(self):
        """Gets the handlers of this DebugStats.  # noqa: E501


        :return: The handlers of this DebugStats.  # noqa: E501
        :rtype: list[DebugStatsHandler]
        """
        return self._handlers

    @handlers.setter
    def handlers(self, handlers):
        """Sets the handlers of this DebugStats.


        :param handlers: The handlers of this DebugStats.  # noqa: E501
        :type: list[DebugStatsHandler]
        """

        self._handlers = handlers

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
        if not isinstance(other, DebugStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
