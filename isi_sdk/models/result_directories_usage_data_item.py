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


class ResultDirectoriesUsageDataItem(object):
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
        'ads_cnt': 'int',
        'dir_cnt': 'int',
        'file_cnt': 'int',
        'has_subdirs': 'bool',
        'lin': 'int',
        'log_size_sum': 'int',
        'log_size_sum_overflow': 'int',
        'name': 'str',
        'other_cnt': 'int',
        'parent': 'int',
        'phys_size_sum': 'int'
    }

    attribute_map = {
        'ads_cnt': 'ads_cnt',
        'dir_cnt': 'dir_cnt',
        'file_cnt': 'file_cnt',
        'has_subdirs': 'has_subdirs',
        'lin': 'lin',
        'log_size_sum': 'log_size_sum',
        'log_size_sum_overflow': 'log_size_sum_overflow',
        'name': 'name',
        'other_cnt': 'other_cnt',
        'parent': 'parent',
        'phys_size_sum': 'phys_size_sum'
    }

    def __init__(self, ads_cnt=None, dir_cnt=None, file_cnt=None, has_subdirs=None, lin=None, log_size_sum=None, log_size_sum_overflow=None, name=None, other_cnt=None, parent=None, phys_size_sum=None):  # noqa: E501
        """ResultDirectoriesUsageDataItem - a model defined in Swagger"""  # noqa: E501

        self._ads_cnt = None
        self._dir_cnt = None
        self._file_cnt = None
        self._has_subdirs = None
        self._lin = None
        self._log_size_sum = None
        self._log_size_sum_overflow = None
        self._name = None
        self._other_cnt = None
        self._parent = None
        self._phys_size_sum = None
        self.discriminator = None

        self.ads_cnt = ads_cnt
        self.dir_cnt = dir_cnt
        self.file_cnt = file_cnt
        self.has_subdirs = has_subdirs
        self.lin = lin
        self.log_size_sum = log_size_sum
        self.log_size_sum_overflow = log_size_sum_overflow
        self.name = name
        self.other_cnt = other_cnt
        self.parent = parent
        self.phys_size_sum = phys_size_sum

    @property
    def ads_cnt(self):
        """Gets the ads_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Number of alternate data streams.  # noqa: E501

        :return: The ads_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: int
        """
        return self._ads_cnt

    @ads_cnt.setter
    def ads_cnt(self, ads_cnt):
        """Sets the ads_cnt of this ResultDirectoriesUsageDataItem.

        Number of alternate data streams.  # noqa: E501

        :param ads_cnt: The ads_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: int
        """
        if ads_cnt is None:
            raise ValueError("Invalid value for `ads_cnt`, must not be `None`")  # noqa: E501

        self._ads_cnt = ads_cnt

    @property
    def dir_cnt(self):
        """Gets the dir_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Number of directories.  # noqa: E501

        :return: The dir_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: int
        """
        return self._dir_cnt

    @dir_cnt.setter
    def dir_cnt(self, dir_cnt):
        """Sets the dir_cnt of this ResultDirectoriesUsageDataItem.

        Number of directories.  # noqa: E501

        :param dir_cnt: The dir_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: int
        """
        if dir_cnt is None:
            raise ValueError("Invalid value for `dir_cnt`, must not be `None`")  # noqa: E501

        self._dir_cnt = dir_cnt

    @property
    def file_cnt(self):
        """Gets the file_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Number of files.  # noqa: E501

        :return: The file_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: int
        """
        return self._file_cnt

    @file_cnt.setter
    def file_cnt(self, file_cnt):
        """Sets the file_cnt of this ResultDirectoriesUsageDataItem.

        Number of files.  # noqa: E501

        :param file_cnt: The file_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: int
        """
        if file_cnt is None:
            raise ValueError("Invalid value for `file_cnt`, must not be `None`")  # noqa: E501

        self._file_cnt = file_cnt

    @property
    def has_subdirs(self):
        """Gets the has_subdirs of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Defines if directory has subdirectories.  # noqa: E501

        :return: The has_subdirs of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_subdirs

    @has_subdirs.setter
    def has_subdirs(self, has_subdirs):
        """Sets the has_subdirs of this ResultDirectoriesUsageDataItem.

        Defines if directory has subdirectories.  # noqa: E501

        :param has_subdirs: The has_subdirs of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: bool
        """
        if has_subdirs is None:
            raise ValueError("Invalid value for `has_subdirs`, must not be `None`")  # noqa: E501

        self._has_subdirs = has_subdirs

    @property
    def lin(self):
        """Gets the lin of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Logical inode number.  # noqa: E501

        :return: The lin of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: int
        """
        return self._lin

    @lin.setter
    def lin(self, lin):
        """Sets the lin of this ResultDirectoriesUsageDataItem.

        Logical inode number.  # noqa: E501

        :param lin: The lin of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: int
        """
        if lin is None:
            raise ValueError("Invalid value for `lin`, must not be `None`")  # noqa: E501

        self._lin = lin

    @property
    def log_size_sum(self):
        """Gets the log_size_sum of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Logical size directory in bytes.  # noqa: E501

        :return: The log_size_sum of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: int
        """
        return self._log_size_sum

    @log_size_sum.setter
    def log_size_sum(self, log_size_sum):
        """Sets the log_size_sum of this ResultDirectoriesUsageDataItem.

        Logical size directory in bytes.  # noqa: E501

        :param log_size_sum: The log_size_sum of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: int
        """
        if log_size_sum is None:
            raise ValueError("Invalid value for `log_size_sum`, must not be `None`")  # noqa: E501

        self._log_size_sum = log_size_sum

    @property
    def log_size_sum_overflow(self):
        """Gets the log_size_sum_overflow of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Logical size sum of overflow in bytes.  # noqa: E501

        :return: The log_size_sum_overflow of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: int
        """
        return self._log_size_sum_overflow

    @log_size_sum_overflow.setter
    def log_size_sum_overflow(self, log_size_sum_overflow):
        """Sets the log_size_sum_overflow of this ResultDirectoriesUsageDataItem.

        Logical size sum of overflow in bytes.  # noqa: E501

        :param log_size_sum_overflow: The log_size_sum_overflow of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: int
        """
        if log_size_sum_overflow is None:
            raise ValueError("Invalid value for `log_size_sum_overflow`, must not be `None`")  # noqa: E501

        self._log_size_sum_overflow = log_size_sum_overflow

    @property
    def name(self):
        """Gets the name of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Name of directory.  # noqa: E501

        :return: The name of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResultDirectoriesUsageDataItem.

        Name of directory.  # noqa: E501

        :param name: The name of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def other_cnt(self):
        """Gets the other_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Other count.  # noqa: E501

        :return: The other_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: int
        """
        return self._other_cnt

    @other_cnt.setter
    def other_cnt(self, other_cnt):
        """Sets the other_cnt of this ResultDirectoriesUsageDataItem.

        Other count.  # noqa: E501

        :param other_cnt: The other_cnt of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: int
        """
        if other_cnt is None:
            raise ValueError("Invalid value for `other_cnt`, must not be `None`")  # noqa: E501

        self._other_cnt = other_cnt

    @property
    def parent(self):
        """Gets the parent of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Parent directory inode.  # noqa: E501

        :return: The parent of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ResultDirectoriesUsageDataItem.

        Parent directory inode.  # noqa: E501

        :param parent: The parent of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: int
        """
        if parent is None:
            raise ValueError("Invalid value for `parent`, must not be `None`")  # noqa: E501

        self._parent = parent

    @property
    def phys_size_sum(self):
        """Gets the phys_size_sum of this ResultDirectoriesUsageDataItem.  # noqa: E501

        Physical size directory in bytes.  # noqa: E501

        :return: The phys_size_sum of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :rtype: int
        """
        return self._phys_size_sum

    @phys_size_sum.setter
    def phys_size_sum(self, phys_size_sum):
        """Sets the phys_size_sum of this ResultDirectoriesUsageDataItem.

        Physical size directory in bytes.  # noqa: E501

        :param phys_size_sum: The phys_size_sum of this ResultDirectoriesUsageDataItem.  # noqa: E501
        :type: int
        """
        if phys_size_sum is None:
            raise ValueError("Invalid value for `phys_size_sum`, must not be `None`")  # noqa: E501

        self._phys_size_sum = phys_size_sum

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
        if not isinstance(other, ResultDirectoriesUsageDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
