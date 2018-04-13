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


class LicenseLicenseTierEntitlementsExceededAlert(object):
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
        'current': 'int',
        'issue_type': 'str',
        'licensed': 'int'
    }

    attribute_map = {
        'current': 'current',
        'issue_type': 'issue_type',
        'licensed': 'licensed'
    }

    def __init__(self, current=None, issue_type=None, licensed=None):  # noqa: E501
        """LicenseLicenseTierEntitlementsExceededAlert - a model defined in Swagger"""  # noqa: E501

        self._current = None
        self._issue_type = None
        self._licensed = None
        self.discriminator = None

        if current is not None:
            self.current = current
        self.issue_type = issue_type
        if licensed is not None:
            self.licensed = licensed

    @property
    def current(self):
        """Gets the current of this LicenseLicenseTierEntitlementsExceededAlert.  # noqa: E501

        Current usage.  # noqa: E501

        :return: The current of this LicenseLicenseTierEntitlementsExceededAlert.  # noqa: E501
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this LicenseLicenseTierEntitlementsExceededAlert.

        Current usage.  # noqa: E501

        :param current: The current of this LicenseLicenseTierEntitlementsExceededAlert.  # noqa: E501
        :type: int
        """
        if current is not None and current > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `current`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if current is not None and current < 0:  # noqa: E501
            raise ValueError("Invalid value for `current`, must be a value greater than or equal to `0`")  # noqa: E501

        self._current = current

    @property
    def issue_type(self):
        """Gets the issue_type of this LicenseLicenseTierEntitlementsExceededAlert.  # noqa: E501

        Alert type. The unit of measure for the current and licensed fields for capacity is terabytes. For nodes_with_seds_count, it is the number of nodes that have one or more self-encrypting drives.  # noqa: E501

        :return: The issue_type of this LicenseLicenseTierEntitlementsExceededAlert.  # noqa: E501
        :rtype: str
        """
        return self._issue_type

    @issue_type.setter
    def issue_type(self, issue_type):
        """Sets the issue_type of this LicenseLicenseTierEntitlementsExceededAlert.

        Alert type. The unit of measure for the current and licensed fields for capacity is terabytes. For nodes_with_seds_count, it is the number of nodes that have one or more self-encrypting drives.  # noqa: E501

        :param issue_type: The issue_type of this LicenseLicenseTierEntitlementsExceededAlert.  # noqa: E501
        :type: str
        """
        if issue_type is None:
            raise ValueError("Invalid value for `issue_type`, must not be `None`")  # noqa: E501
        allowed_values = ["capacity", "node_count", "nodes_with_seds_count"]  # noqa: E501
        if issue_type not in allowed_values:
            raise ValueError(
                "Invalid value for `issue_type` ({0}), must be one of {1}"  # noqa: E501
                .format(issue_type, allowed_values)
            )

        self._issue_type = issue_type

    @property
    def licensed(self):
        """Gets the licensed of this LicenseLicenseTierEntitlementsExceededAlert.  # noqa: E501

        Licensed amount.  # noqa: E501

        :return: The licensed of this LicenseLicenseTierEntitlementsExceededAlert.  # noqa: E501
        :rtype: int
        """
        return self._licensed

    @licensed.setter
    def licensed(self, licensed):
        """Sets the licensed of this LicenseLicenseTierEntitlementsExceededAlert.

        Licensed amount.  # noqa: E501

        :param licensed: The licensed of this LicenseLicenseTierEntitlementsExceededAlert.  # noqa: E501
        :type: int
        """
        if licensed is not None and licensed > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `licensed`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if licensed is not None and licensed < 0:  # noqa: E501
            raise ValueError("Invalid value for `licensed`, must be a value greater than or equal to `0`")  # noqa: E501

        self._licensed = licensed

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
        if not isinstance(other, LicenseLicenseTierEntitlementsExceededAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
