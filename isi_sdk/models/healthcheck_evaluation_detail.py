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

from isi_sdk_8_1_0.models.empty import Empty  # noqa: F401,E501


class HealthcheckEvaluationDetail(object):
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
        'details': 'Empty',
        'hash': 'str',
        'id': 'str',
        'node': 'str',
        'parameters': 'Empty',
        'status': 'str',
        'value': 'int'
    }

    attribute_map = {
        'details': 'details',
        'hash': 'hash',
        'id': 'id',
        'node': 'node',
        'parameters': 'parameters',
        'status': 'status',
        'value': 'value'
    }

    def __init__(self, details=None, hash=None, id=None, node=None, parameters=None, status=None, value=None):  # noqa: E501
        """HealthcheckEvaluationDetail - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._hash = None
        self._id = None
        self._node = None
        self._parameters = None
        self._status = None
        self._value = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if hash is not None:
            self.hash = hash
        if id is not None:
            self.id = id
        if node is not None:
            self.node = node
        if parameters is not None:
            self.parameters = parameters
        if status is not None:
            self.status = status
        if value is not None:
            self.value = value

    @property
    def details(self):
        """Gets the details of this HealthcheckEvaluationDetail.  # noqa: E501

        Optional details of the evaluation - raw data  # noqa: E501

        :return: The details of this HealthcheckEvaluationDetail.  # noqa: E501
        :rtype: Empty
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this HealthcheckEvaluationDetail.

        Optional details of the evaluation - raw data  # noqa: E501

        :param details: The details of this HealthcheckEvaluationDetail.  # noqa: E501
        :type: Empty
        """

        self._details = details

    @property
    def hash(self):
        """Gets the hash of this HealthcheckEvaluationDetail.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The hash of this HealthcheckEvaluationDetail.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this HealthcheckEvaluationDetail.

        Unique identifier  # noqa: E501

        :param hash: The hash of this HealthcheckEvaluationDetail.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def id(self):
        """Gets the id of this HealthcheckEvaluationDetail.  # noqa: E501

        Unique identifier of item  # noqa: E501

        :return: The id of this HealthcheckEvaluationDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthcheckEvaluationDetail.

        Unique identifier of item  # noqa: E501

        :param id: The id of this HealthcheckEvaluationDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def node(self):
        """Gets the node of this HealthcheckEvaluationDetail.  # noqa: E501

        Either 'cluster' or an lnn  # noqa: E501

        :return: The node of this HealthcheckEvaluationDetail.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this HealthcheckEvaluationDetail.

        Either 'cluster' or an lnn  # noqa: E501

        :param node: The node of this HealthcheckEvaluationDetail.  # noqa: E501
        :type: str
        """

        self._node = node

    @property
    def parameters(self):
        """Gets the parameters of this HealthcheckEvaluationDetail.  # noqa: E501

        The parameters used in this item evaluation  # noqa: E501

        :return: The parameters of this HealthcheckEvaluationDetail.  # noqa: E501
        :rtype: Empty
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this HealthcheckEvaluationDetail.

        The parameters used in this item evaluation  # noqa: E501

        :param parameters: The parameters of this HealthcheckEvaluationDetail.  # noqa: E501
        :type: Empty
        """

        self._parameters = parameters

    @property
    def status(self):
        """Gets the status of this HealthcheckEvaluationDetail.  # noqa: E501

        Health status based on default thresholds  # noqa: E501

        :return: The status of this HealthcheckEvaluationDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HealthcheckEvaluationDetail.

        Health status based on default thresholds  # noqa: E501

        :param status: The status of this HealthcheckEvaluationDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "WARNING", "CRITICAL", "EMERGENCY", "UNSUPPORTED", "ERROR"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def value(self):
        """Gets the value of this HealthcheckEvaluationDetail.  # noqa: E501

        Normalised measured value 0 (bad) to 100 (perfect)  # noqa: E501

        :return: The value of this HealthcheckEvaluationDetail.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this HealthcheckEvaluationDetail.

        Normalised measured value 0 (bad) to 100 (perfect)  # noqa: E501

        :param value: The value of this HealthcheckEvaluationDetail.  # noqa: E501
        :type: int
        """
        if value is not None and value > 100:  # noqa: E501
            raise ValueError("Invalid value for `value`, must be a value less than or equal to `100`")  # noqa: E501
        if value is not None and value < 0:  # noqa: E501
            raise ValueError("Invalid value for `value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, HealthcheckEvaluationDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
