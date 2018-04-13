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

from isi_sdk_8_1_0.models.quota_notification import QuotaNotification  # noqa: F401,E501


class QuotaNotificationCreateParams(object):
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
        'action_alert': 'bool',
        'action_email_address': 'str',
        'action_email_owner': 'bool',
        'email_template': 'str',
        'holdoff': 'int',
        'schedule': 'str',
        'condition': 'str',
        'threshold': 'str'
    }

    attribute_map = {
        'action_alert': 'action_alert',
        'action_email_address': 'action_email_address',
        'action_email_owner': 'action_email_owner',
        'email_template': 'email_template',
        'holdoff': 'holdoff',
        'schedule': 'schedule',
        'condition': 'condition',
        'threshold': 'threshold'
    }

    def __init__(self, action_alert=None, action_email_address=None, action_email_owner=None, email_template=None, holdoff=None, schedule=None, condition=None, threshold=None):  # noqa: E501
        """QuotaNotificationCreateParams - a model defined in Swagger"""  # noqa: E501

        self._action_alert = None
        self._action_email_address = None
        self._action_email_owner = None
        self._email_template = None
        self._holdoff = None
        self._schedule = None
        self._condition = None
        self._threshold = None
        self.discriminator = None

        if action_alert is not None:
            self.action_alert = action_alert
        if action_email_address is not None:
            self.action_email_address = action_email_address
        if action_email_owner is not None:
            self.action_email_owner = action_email_owner
        if email_template is not None:
            self.email_template = email_template
        if holdoff is not None:
            self.holdoff = holdoff
        if schedule is not None:
            self.schedule = schedule
        self.condition = condition
        self.threshold = threshold

    @property
    def action_alert(self):
        """Gets the action_alert of this QuotaNotificationCreateParams.  # noqa: E501

        Send alert when rule matches.  # noqa: E501

        :return: The action_alert of this QuotaNotificationCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._action_alert

    @action_alert.setter
    def action_alert(self, action_alert):
        """Sets the action_alert of this QuotaNotificationCreateParams.

        Send alert when rule matches.  # noqa: E501

        :param action_alert: The action_alert of this QuotaNotificationCreateParams.  # noqa: E501
        :type: bool
        """

        self._action_alert = action_alert

    @property
    def action_email_address(self):
        """Gets the action_email_address of this QuotaNotificationCreateParams.  # noqa: E501

        Email a specific email address when rule matches.  # noqa: E501

        :return: The action_email_address of this QuotaNotificationCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._action_email_address

    @action_email_address.setter
    def action_email_address(self, action_email_address):
        """Sets the action_email_address of this QuotaNotificationCreateParams.

        Email a specific email address when rule matches.  # noqa: E501

        :param action_email_address: The action_email_address of this QuotaNotificationCreateParams.  # noqa: E501
        :type: str
        """

        self._action_email_address = action_email_address

    @property
    def action_email_owner(self):
        """Gets the action_email_owner of this QuotaNotificationCreateParams.  # noqa: E501

        Email quota domain owner when rule matches.  # noqa: E501

        :return: The action_email_owner of this QuotaNotificationCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._action_email_owner

    @action_email_owner.setter
    def action_email_owner(self, action_email_owner):
        """Sets the action_email_owner of this QuotaNotificationCreateParams.

        Email quota domain owner when rule matches.  # noqa: E501

        :param action_email_owner: The action_email_owner of this QuotaNotificationCreateParams.  # noqa: E501
        :type: bool
        """

        self._action_email_owner = action_email_owner

    @property
    def email_template(self):
        """Gets the email_template of this QuotaNotificationCreateParams.  # noqa: E501

        Path of optional /ifs template file used for email actions.  # noqa: E501

        :return: The email_template of this QuotaNotificationCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._email_template

    @email_template.setter
    def email_template(self, email_template):
        """Sets the email_template of this QuotaNotificationCreateParams.

        Path of optional /ifs template file used for email actions.  # noqa: E501

        :param email_template: The email_template of this QuotaNotificationCreateParams.  # noqa: E501
        :type: str
        """

        self._email_template = email_template

    @property
    def holdoff(self):
        """Gets the holdoff of this QuotaNotificationCreateParams.  # noqa: E501

        Time to wait between detections for rules triggered by user actions.  # noqa: E501

        :return: The holdoff of this QuotaNotificationCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._holdoff

    @holdoff.setter
    def holdoff(self, holdoff):
        """Sets the holdoff of this QuotaNotificationCreateParams.

        Time to wait between detections for rules triggered by user actions.  # noqa: E501

        :param holdoff: The holdoff of this QuotaNotificationCreateParams.  # noqa: E501
        :type: int
        """

        self._holdoff = holdoff

    @property
    def schedule(self):
        """Gets the schedule of this QuotaNotificationCreateParams.  # noqa: E501

        Schedule for rules that repeatedly notify.  # noqa: E501

        :return: The schedule of this QuotaNotificationCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this QuotaNotificationCreateParams.

        Schedule for rules that repeatedly notify.  # noqa: E501

        :param schedule: The schedule of this QuotaNotificationCreateParams.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def condition(self):
        """Gets the condition of this QuotaNotificationCreateParams.  # noqa: E501

        The condition detected.  # noqa: E501

        :return: The condition of this QuotaNotificationCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this QuotaNotificationCreateParams.

        The condition detected.  # noqa: E501

        :param condition: The condition of this QuotaNotificationCreateParams.  # noqa: E501
        :type: str
        """
        if condition is None:
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501
        allowed_values = ["exceeded", "denied", "violated", "expired"]  # noqa: E501
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def threshold(self):
        """Gets the threshold of this QuotaNotificationCreateParams.  # noqa: E501

        The quota threshold detected.  # noqa: E501

        :return: The threshold of this QuotaNotificationCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this QuotaNotificationCreateParams.

        The quota threshold detected.  # noqa: E501

        :param threshold: The threshold of this QuotaNotificationCreateParams.  # noqa: E501
        :type: str
        """
        if threshold is None:
            raise ValueError("Invalid value for `threshold`, must not be `None`")  # noqa: E501
        allowed_values = ["hard", "soft", "advisory"]  # noqa: E501
        if threshold not in allowed_values:
            raise ValueError(
                "Invalid value for `threshold` ({0}), must be one of {1}"  # noqa: E501
                .format(threshold, allowed_values)
            )

        self._threshold = threshold

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
        if not isinstance(other, QuotaNotificationCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
