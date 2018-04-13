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


class NodeStateServicelightNode(object):
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
        'enabled': 'bool',
        'error': 'str',
        'id': 'int',
        'lnn': 'int',
        'present': 'bool',
        'status': 'int',
        'supported': 'bool',
        'valid': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'error': 'error',
        'id': 'id',
        'lnn': 'lnn',
        'present': 'present',
        'status': 'status',
        'supported': 'supported',
        'valid': 'valid'
    }

    def __init__(self, enabled=None, error=None, id=None, lnn=None, present=None, status=None, supported=None, valid=None):  # noqa: E501
        """NodeStateServicelightNode - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._error = None
        self._id = None
        self._lnn = None
        self._present = None
        self._status = None
        self._supported = None
        self._valid = None
        self.discriminator = None

        self.enabled = enabled
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if present is not None:
            self.present = present
        if status is not None:
            self.status = status
        if supported is not None:
            self.supported = supported
        if valid is not None:
            self.valid = valid

    @property
    def enabled(self):
        """Gets the enabled of this NodeStateServicelightNode.  # noqa: E501

        The node service light state (True = on).  # noqa: E501

        :return: The enabled of this NodeStateServicelightNode.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NodeStateServicelightNode.

        The node service light state (True = on).  # noqa: E501

        :param enabled: The enabled of this NodeStateServicelightNode.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def error(self):
        """Gets the error of this NodeStateServicelightNode.  # noqa: E501

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :return: The error of this NodeStateServicelightNode.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this NodeStateServicelightNode.

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :param error: The error of this NodeStateServicelightNode.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """Gets the id of this NodeStateServicelightNode.  # noqa: E501

        Node ID of the node reporting this information.  # noqa: E501

        :return: The id of this NodeStateServicelightNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeStateServicelightNode.

        Node ID of the node reporting this information.  # noqa: E501

        :param id: The id of this NodeStateServicelightNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this NodeStateServicelightNode.  # noqa: E501

        Logical node number of the node reporting this information.  # noqa: E501

        :return: The lnn of this NodeStateServicelightNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeStateServicelightNode.

        Logical node number of the node reporting this information.  # noqa: E501

        :param lnn: The lnn of this NodeStateServicelightNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if lnn is not None and lnn < 0:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lnn = lnn

    @property
    def present(self):
        """Gets the present of this NodeStateServicelightNode.  # noqa: E501

        This node has a service light.  # noqa: E501

        :return: The present of this NodeStateServicelightNode.  # noqa: E501
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """Sets the present of this NodeStateServicelightNode.

        This node has a service light.  # noqa: E501

        :param present: The present of this NodeStateServicelightNode.  # noqa: E501
        :type: bool
        """

        self._present = present

    @property
    def status(self):
        """Gets the status of this NodeStateServicelightNode.  # noqa: E501

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :return: The status of this NodeStateServicelightNode.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeStateServicelightNode.

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :param status: The status of this NodeStateServicelightNode.  # noqa: E501
        :type: int
        """
        if status is not None and status > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if status is not None and status < 0:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `0`")  # noqa: E501

        self._status = status

    @property
    def supported(self):
        """Gets the supported of this NodeStateServicelightNode.  # noqa: E501

        This node supports a service light.  # noqa: E501

        :return: The supported of this NodeStateServicelightNode.  # noqa: E501
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """Sets the supported of this NodeStateServicelightNode.

        This node supports a service light.  # noqa: E501

        :param supported: The supported of this NodeStateServicelightNode.  # noqa: E501
        :type: bool
        """

        self._supported = supported

    @property
    def valid(self):
        """Gets the valid of this NodeStateServicelightNode.  # noqa: E501

        The node service light state is valid (False = Error).  # noqa: E501

        :return: The valid of this NodeStateServicelightNode.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this NodeStateServicelightNode.

        The node service light state is valid (False = Error).  # noqa: E501

        :param valid: The valid of this NodeStateServicelightNode.  # noqa: E501
        :type: bool
        """

        self._valid = valid

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
        if not isinstance(other, NodeStateServicelightNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
