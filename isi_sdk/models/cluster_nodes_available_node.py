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


class ClusterNodesAvailableNode(object):
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
        'configuration_id': 'str',
        'description': 'str',
        'product': 'str',
        'serial_number': 'str',
        'status': 'str',
        'version': 'str'
    }

    attribute_map = {
        'configuration_id': 'configuration_id',
        'description': 'description',
        'product': 'product',
        'serial_number': 'serial_number',
        'status': 'status',
        'version': 'version'
    }

    def __init__(self, configuration_id=None, description=None, product=None, serial_number=None, status=None, version=None):  # noqa: E501
        """ClusterNodesAvailableNode - a model defined in Swagger"""  # noqa: E501

        self._configuration_id = None
        self._description = None
        self._product = None
        self._serial_number = None
        self._status = None
        self._version = None
        self.discriminator = None

        if configuration_id is not None:
            self.configuration_id = configuration_id
        if description is not None:
            self.description = description
        if product is not None:
            self.product = product
        if serial_number is not None:
            self.serial_number = serial_number
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version

    @property
    def configuration_id(self):
        """Gets the configuration_id of this ClusterNodesAvailableNode.  # noqa: E501

        Node configuration ID.  # noqa: E501

        :return: The configuration_id of this ClusterNodesAvailableNode.  # noqa: E501
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this ClusterNodesAvailableNode.

        Node configuration ID.  # noqa: E501

        :param configuration_id: The configuration_id of this ClusterNodesAvailableNode.  # noqa: E501
        :type: str
        """

        self._configuration_id = configuration_id

    @property
    def description(self):
        """Gets the description of this ClusterNodesAvailableNode.  # noqa: E501

        Human-readable description giving further detail on status (may be empty)  # noqa: E501

        :return: The description of this ClusterNodesAvailableNode.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterNodesAvailableNode.

        Human-readable description giving further detail on status (may be empty)  # noqa: E501

        :param description: The description of this ClusterNodesAvailableNode.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def product(self):
        """Gets the product of this ClusterNodesAvailableNode.  # noqa: E501

        Isilon product name.  # noqa: E501

        :return: The product of this ClusterNodesAvailableNode.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ClusterNodesAvailableNode.

        Isilon product name.  # noqa: E501

        :param product: The product of this ClusterNodesAvailableNode.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def serial_number(self):
        """Gets the serial_number of this ClusterNodesAvailableNode.  # noqa: E501

        Serial number of this node.  # noqa: E501

        :return: The serial_number of this ClusterNodesAvailableNode.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ClusterNodesAvailableNode.

        Serial number of this node.  # noqa: E501

        :param serial_number: The serial_number of this ClusterNodesAvailableNode.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def status(self):
        """Gets the status of this ClusterNodesAvailableNode.  # noqa: E501

        Availability of the node.  # noqa: E501

        :return: The status of this ClusterNodesAvailableNode.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterNodesAvailableNode.

        Availability of the node.  # noqa: E501

        :param status: The status of this ClusterNodesAvailableNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["available", "waiting", "error", "error_permanent", "working", "rebooting", "exiting"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def version(self):
        """Gets the version of this ClusterNodesAvailableNode.  # noqa: E501

        OneFS build version running on the node.  # noqa: E501

        :return: The version of this ClusterNodesAvailableNode.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterNodesAvailableNode.

        OneFS build version running on the node.  # noqa: E501

        :param version: The version of this ClusterNodesAvailableNode.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, ClusterNodesAvailableNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
