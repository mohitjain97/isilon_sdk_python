# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 9
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobJobPrepairParams(object):
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
        'mapping_type': 'str',
        'mode': 'str',
        'template': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'mapping_type': 'mapping_type',
        'mode': 'mode',
        'template': 'template',
        'zone': 'zone'
    }

    def __init__(self, mapping_type=None, mode=None, template=None, zone=None):  # noqa: E501
        """JobJobPrepairParams - a model defined in Swagger"""  # noqa: E501

        self._mapping_type = None
        self._mode = None
        self._template = None
        self._zone = None
        self.discriminator = None

        if mapping_type is not None:
            self.mapping_type = mapping_type
        self.mode = mode
        if template is not None:
            self.template = template
        if zone is not None:
            self.zone = zone

    @property
    def mapping_type(self):
        """Gets the mapping_type of this JobJobPrepairParams.  # noqa: E501

        Type of permissions; not accepted with mode=clone or mode=inherit.  # noqa: E501

        :return: The mapping_type of this JobJobPrepairParams.  # noqa: E501
        :rtype: str
        """
        return self._mapping_type

    @mapping_type.setter
    def mapping_type(self, mapping_type):
        """Sets the mapping_type of this JobJobPrepairParams.

        Type of permissions; not accepted with mode=clone or mode=inherit.  # noqa: E501

        :param mapping_type: The mapping_type of this JobJobPrepairParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["global", "sid", "unix", "native"]  # noqa: E501
        if mapping_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mapping_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mapping_type, allowed_values)
            )

        self._mapping_type = mapping_type

    @property
    def mode(self):
        """Gets the mode of this JobJobPrepairParams.  # noqa: E501

        Type of PermissionRepair operation.  # noqa: E501

        :return: The mode of this JobJobPrepairParams.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this JobJobPrepairParams.

        Type of PermissionRepair operation.  # noqa: E501

        :param mode: The mode of this JobJobPrepairParams.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["clone", "inherit", "convert"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def template(self):
        """Gets the template of this JobJobPrepairParams.  # noqa: E501


        :return: The template of this JobJobPrepairParams.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this JobJobPrepairParams.


        :param template: The template of this JobJobPrepairParams.  # noqa: E501
        :type: str
        """
        if template is not None and len(template) > 4096:
            raise ValueError("Invalid value for `template`, length must be less than or equal to `4096`")  # noqa: E501
        if template is not None and len(template) < 4:
            raise ValueError("Invalid value for `template`, length must be greater than or equal to `4`")  # noqa: E501
        if template is not None and not re.search('^\/ifs|^\/ifs\/.*', template):  # noqa: E501
            raise ValueError("Invalid value for `template`, must be a follow pattern or equal to `/^\/ifs|^\/ifs\/.*/`")  # noqa: E501

        self._template = template

    @property
    def zone(self):
        """Gets the zone of this JobJobPrepairParams.  # noqa: E501

        Authentication zone; not accepted with mode=clone or mode=inherit.  # noqa: E501

        :return: The zone of this JobJobPrepairParams.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this JobJobPrepairParams.

        Authentication zone; not accepted with mode=clone or mode=inherit.  # noqa: E501

        :param zone: The zone of this JobJobPrepairParams.  # noqa: E501
        :type: str
        """
        if zone is not None and len(zone) > 2147483647:
            raise ValueError("Invalid value for `zone`, length must be less than or equal to `2147483647`")  # noqa: E501
        if zone is not None and len(zone) < 1:
            raise ValueError("Invalid value for `zone`, length must be greater than or equal to `1`")  # noqa: E501

        self._zone = zone

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
        if not isinstance(other, JobJobPrepairParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other