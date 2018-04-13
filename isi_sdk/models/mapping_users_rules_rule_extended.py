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

from isi_sdk_8_1_0.models.mapping_users_rules_rule_options_default_user import MappingUsersRulesRuleOptionsDefaultUser  # noqa: F401,E501
from isi_sdk_8_1_0.models.mapping_users_rules_rule_options_extended import MappingUsersRulesRuleOptionsExtended  # noqa: F401,E501
from isi_sdk_8_1_0.models.mapping_users_rules_rule_user2_extended import MappingUsersRulesRuleUser2Extended  # noqa: F401,E501


class MappingUsersRulesRuleExtended(object):
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
        'operator': 'str',
        'options': 'MappingUsersRulesRuleOptionsExtended',
        'user1': 'MappingUsersRulesRuleOptionsDefaultUser',
        'user2': 'MappingUsersRulesRuleUser2Extended'
    }

    attribute_map = {
        'operator': 'operator',
        'options': 'options',
        'user1': 'user1',
        'user2': 'user2'
    }

    def __init__(self, operator=None, options=None, user1=None, user2=None):  # noqa: E501
        """MappingUsersRulesRuleExtended - a model defined in Swagger"""  # noqa: E501

        self._operator = None
        self._options = None
        self._user1 = None
        self._user2 = None
        self.discriminator = None

        if operator is not None:
            self.operator = operator
        if options is not None:
            self.options = options
        self.user1 = user1
        if user2 is not None:
            self.user2 = user2

    @property
    def operator(self):
        """Gets the operator of this MappingUsersRulesRuleExtended.  # noqa: E501

        Specifies the operator to make rules on specified users or groups.  # noqa: E501

        :return: The operator of this MappingUsersRulesRuleExtended.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this MappingUsersRulesRuleExtended.

        Specifies the operator to make rules on specified users or groups.  # noqa: E501

        :param operator: The operator of this MappingUsersRulesRuleExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["append", "insert", "replace", "trim", "union"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"  # noqa: E501
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def options(self):
        """Gets the options of this MappingUsersRulesRuleExtended.  # noqa: E501

        Specifies the properties for user mapping rules.  # noqa: E501

        :return: The options of this MappingUsersRulesRuleExtended.  # noqa: E501
        :rtype: MappingUsersRulesRuleOptionsExtended
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this MappingUsersRulesRuleExtended.

        Specifies the properties for user mapping rules.  # noqa: E501

        :param options: The options of this MappingUsersRulesRuleExtended.  # noqa: E501
        :type: MappingUsersRulesRuleOptionsExtended
        """

        self._options = options

    @property
    def user1(self):
        """Gets the user1 of this MappingUsersRulesRuleExtended.  # noqa: E501

          # noqa: E501

        :return: The user1 of this MappingUsersRulesRuleExtended.  # noqa: E501
        :rtype: MappingUsersRulesRuleOptionsDefaultUser
        """
        return self._user1

    @user1.setter
    def user1(self, user1):
        """Sets the user1 of this MappingUsersRulesRuleExtended.

          # noqa: E501

        :param user1: The user1 of this MappingUsersRulesRuleExtended.  # noqa: E501
        :type: MappingUsersRulesRuleOptionsDefaultUser
        """
        if user1 is None:
            raise ValueError("Invalid value for `user1`, must not be `None`")  # noqa: E501

        self._user1 = user1

    @property
    def user2(self):
        """Gets the user2 of this MappingUsersRulesRuleExtended.  # noqa: E501

          # noqa: E501

        :return: The user2 of this MappingUsersRulesRuleExtended.  # noqa: E501
        :rtype: MappingUsersRulesRuleUser2Extended
        """
        return self._user2

    @user2.setter
    def user2(self, user2):
        """Sets the user2 of this MappingUsersRulesRuleExtended.

          # noqa: E501

        :param user2: The user2 of this MappingUsersRulesRuleExtended.  # noqa: E501
        :type: MappingUsersRulesRuleUser2Extended
        """

        self._user2 = user2

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
        if not isinstance(other, MappingUsersRulesRuleExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
