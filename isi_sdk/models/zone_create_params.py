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

from isi_sdk_8_1_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isi_sdk_8_1_0.models.zone import Zone  # noqa: F401,E501


class ZoneCreateParams(object):
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
        'alternate_system_provider': 'str',
        'auth_providers': 'list[str]',
        'cache_entry_expiry': 'int',
        'create_path': 'bool',
        'force_overlap': 'bool',
        'home_directory_umask': 'int',
        'ifs_restricted': 'list[AuthAccessAccessItemFileGroup]',
        'map_untrusted': 'str',
        'name': 'str',
        'negative_cache_entry_expiry': 'int',
        'netbios_name': 'str',
        'path': 'str',
        'skeleton_directory': 'str',
        'system_provider': 'str',
        'user_mapping_rules': 'list[str]',
        'groupnet': 'str'
    }

    attribute_map = {
        'alternate_system_provider': 'alternate_system_provider',
        'auth_providers': 'auth_providers',
        'cache_entry_expiry': 'cache_entry_expiry',
        'create_path': 'create_path',
        'force_overlap': 'force_overlap',
        'home_directory_umask': 'home_directory_umask',
        'ifs_restricted': 'ifs_restricted',
        'map_untrusted': 'map_untrusted',
        'name': 'name',
        'negative_cache_entry_expiry': 'negative_cache_entry_expiry',
        'netbios_name': 'netbios_name',
        'path': 'path',
        'skeleton_directory': 'skeleton_directory',
        'system_provider': 'system_provider',
        'user_mapping_rules': 'user_mapping_rules',
        'groupnet': 'groupnet'
    }

    def __init__(self, alternate_system_provider=None, auth_providers=None, cache_entry_expiry=None, create_path=None, force_overlap=None, home_directory_umask=None, ifs_restricted=None, map_untrusted=None, name=None, negative_cache_entry_expiry=None, netbios_name=None, path=None, skeleton_directory=None, system_provider=None, user_mapping_rules=None, groupnet=None):  # noqa: E501
        """ZoneCreateParams - a model defined in Swagger"""  # noqa: E501

        self._alternate_system_provider = None
        self._auth_providers = None
        self._cache_entry_expiry = None
        self._create_path = None
        self._force_overlap = None
        self._home_directory_umask = None
        self._ifs_restricted = None
        self._map_untrusted = None
        self._name = None
        self._negative_cache_entry_expiry = None
        self._netbios_name = None
        self._path = None
        self._skeleton_directory = None
        self._system_provider = None
        self._user_mapping_rules = None
        self._groupnet = None
        self.discriminator = None

        if alternate_system_provider is not None:
            self.alternate_system_provider = alternate_system_provider
        if auth_providers is not None:
            self.auth_providers = auth_providers
        if cache_entry_expiry is not None:
            self.cache_entry_expiry = cache_entry_expiry
        if create_path is not None:
            self.create_path = create_path
        if force_overlap is not None:
            self.force_overlap = force_overlap
        if home_directory_umask is not None:
            self.home_directory_umask = home_directory_umask
        if ifs_restricted is not None:
            self.ifs_restricted = ifs_restricted
        if map_untrusted is not None:
            self.map_untrusted = map_untrusted
        self.name = name
        if negative_cache_entry_expiry is not None:
            self.negative_cache_entry_expiry = negative_cache_entry_expiry
        if netbios_name is not None:
            self.netbios_name = netbios_name
        if path is not None:
            self.path = path
        if skeleton_directory is not None:
            self.skeleton_directory = skeleton_directory
        if system_provider is not None:
            self.system_provider = system_provider
        if user_mapping_rules is not None:
            self.user_mapping_rules = user_mapping_rules
        if groupnet is not None:
            self.groupnet = groupnet

    @property
    def alternate_system_provider(self):
        """Gets the alternate_system_provider of this ZoneCreateParams.  # noqa: E501

        Specifies an alternate system provider.  # noqa: E501

        :return: The alternate_system_provider of this ZoneCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._alternate_system_provider

    @alternate_system_provider.setter
    def alternate_system_provider(self, alternate_system_provider):
        """Sets the alternate_system_provider of this ZoneCreateParams.

        Specifies an alternate system provider.  # noqa: E501

        :param alternate_system_provider: The alternate_system_provider of this ZoneCreateParams.  # noqa: E501
        :type: str
        """

        self._alternate_system_provider = alternate_system_provider

    @property
    def auth_providers(self):
        """Gets the auth_providers of this ZoneCreateParams.  # noqa: E501

        Specifies the list of authentication providers available on this access zone.  # noqa: E501

        :return: The auth_providers of this ZoneCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._auth_providers

    @auth_providers.setter
    def auth_providers(self, auth_providers):
        """Sets the auth_providers of this ZoneCreateParams.

        Specifies the list of authentication providers available on this access zone.  # noqa: E501

        :param auth_providers: The auth_providers of this ZoneCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._auth_providers = auth_providers

    @property
    def cache_entry_expiry(self):
        """Gets the cache_entry_expiry of this ZoneCreateParams.  # noqa: E501

        Specifies amount of time in seconds to cache a user/group.  # noqa: E501

        :return: The cache_entry_expiry of this ZoneCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._cache_entry_expiry

    @cache_entry_expiry.setter
    def cache_entry_expiry(self, cache_entry_expiry):
        """Sets the cache_entry_expiry of this ZoneCreateParams.

        Specifies amount of time in seconds to cache a user/group.  # noqa: E501

        :param cache_entry_expiry: The cache_entry_expiry of this ZoneCreateParams.  # noqa: E501
        :type: int
        """

        self._cache_entry_expiry = cache_entry_expiry

    @property
    def create_path(self):
        """Gets the create_path of this ZoneCreateParams.  # noqa: E501

        Determines if a path is created when a path does not exist.  # noqa: E501

        :return: The create_path of this ZoneCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._create_path

    @create_path.setter
    def create_path(self, create_path):
        """Sets the create_path of this ZoneCreateParams.

        Determines if a path is created when a path does not exist.  # noqa: E501

        :param create_path: The create_path of this ZoneCreateParams.  # noqa: E501
        :type: bool
        """

        self._create_path = create_path

    @property
    def force_overlap(self):
        """Gets the force_overlap of this ZoneCreateParams.  # noqa: E501

        Allow for overlapping base path.  # noqa: E501

        :return: The force_overlap of this ZoneCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._force_overlap

    @force_overlap.setter
    def force_overlap(self, force_overlap):
        """Sets the force_overlap of this ZoneCreateParams.

        Allow for overlapping base path.  # noqa: E501

        :param force_overlap: The force_overlap of this ZoneCreateParams.  # noqa: E501
        :type: bool
        """

        self._force_overlap = force_overlap

    @property
    def home_directory_umask(self):
        """Gets the home_directory_umask of this ZoneCreateParams.  # noqa: E501

        Specifies the permissions set on automatically created user home directories.  # noqa: E501

        :return: The home_directory_umask of this ZoneCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._home_directory_umask

    @home_directory_umask.setter
    def home_directory_umask(self, home_directory_umask):
        """Sets the home_directory_umask of this ZoneCreateParams.

        Specifies the permissions set on automatically created user home directories.  # noqa: E501

        :param home_directory_umask: The home_directory_umask of this ZoneCreateParams.  # noqa: E501
        :type: int
        """

        self._home_directory_umask = home_directory_umask

    @property
    def ifs_restricted(self):
        """Gets the ifs_restricted of this ZoneCreateParams.  # noqa: E501

        Specifies a list of users and groups that have read and write access to /ifs.  # noqa: E501

        :return: The ifs_restricted of this ZoneCreateParams.  # noqa: E501
        :rtype: list[AuthAccessAccessItemFileGroup]
        """
        return self._ifs_restricted

    @ifs_restricted.setter
    def ifs_restricted(self, ifs_restricted):
        """Sets the ifs_restricted of this ZoneCreateParams.

        Specifies a list of users and groups that have read and write access to /ifs.  # noqa: E501

        :param ifs_restricted: The ifs_restricted of this ZoneCreateParams.  # noqa: E501
        :type: list[AuthAccessAccessItemFileGroup]
        """

        self._ifs_restricted = ifs_restricted

    @property
    def map_untrusted(self):
        """Gets the map_untrusted of this ZoneCreateParams.  # noqa: E501

        Maps untrusted domains to this NetBIOS domain during authentication.  # noqa: E501

        :return: The map_untrusted of this ZoneCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._map_untrusted

    @map_untrusted.setter
    def map_untrusted(self, map_untrusted):
        """Sets the map_untrusted of this ZoneCreateParams.

        Maps untrusted domains to this NetBIOS domain during authentication.  # noqa: E501

        :param map_untrusted: The map_untrusted of this ZoneCreateParams.  # noqa: E501
        :type: str
        """

        self._map_untrusted = map_untrusted

    @property
    def name(self):
        """Gets the name of this ZoneCreateParams.  # noqa: E501

        Specifies the access zone name.  # noqa: E501

        :return: The name of this ZoneCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ZoneCreateParams.

        Specifies the access zone name.  # noqa: E501

        :param name: The name of this ZoneCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def negative_cache_entry_expiry(self):
        """Gets the negative_cache_entry_expiry of this ZoneCreateParams.  # noqa: E501

        Specifies number of seconds the negative cache entry is valid.  # noqa: E501

        :return: The negative_cache_entry_expiry of this ZoneCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._negative_cache_entry_expiry

    @negative_cache_entry_expiry.setter
    def negative_cache_entry_expiry(self, negative_cache_entry_expiry):
        """Sets the negative_cache_entry_expiry of this ZoneCreateParams.

        Specifies number of seconds the negative cache entry is valid.  # noqa: E501

        :param negative_cache_entry_expiry: The negative_cache_entry_expiry of this ZoneCreateParams.  # noqa: E501
        :type: int
        """

        self._negative_cache_entry_expiry = negative_cache_entry_expiry

    @property
    def netbios_name(self):
        """Gets the netbios_name of this ZoneCreateParams.  # noqa: E501

        Specifies the NetBIOS name.  # noqa: E501

        :return: The netbios_name of this ZoneCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._netbios_name

    @netbios_name.setter
    def netbios_name(self, netbios_name):
        """Sets the netbios_name of this ZoneCreateParams.

        Specifies the NetBIOS name.  # noqa: E501

        :param netbios_name: The netbios_name of this ZoneCreateParams.  # noqa: E501
        :type: str
        """

        self._netbios_name = netbios_name

    @property
    def path(self):
        """Gets the path of this ZoneCreateParams.  # noqa: E501

        Specifies the access zone base directory path.  # noqa: E501

        :return: The path of this ZoneCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ZoneCreateParams.

        Specifies the access zone base directory path.  # noqa: E501

        :param path: The path of this ZoneCreateParams.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def skeleton_directory(self):
        """Gets the skeleton_directory of this ZoneCreateParams.  # noqa: E501

        Specifies the skeleton directory that is used for user home directories.  # noqa: E501

        :return: The skeleton_directory of this ZoneCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._skeleton_directory

    @skeleton_directory.setter
    def skeleton_directory(self, skeleton_directory):
        """Sets the skeleton_directory of this ZoneCreateParams.

        Specifies the skeleton directory that is used for user home directories.  # noqa: E501

        :param skeleton_directory: The skeleton_directory of this ZoneCreateParams.  # noqa: E501
        :type: str
        """

        self._skeleton_directory = skeleton_directory

    @property
    def system_provider(self):
        """Gets the system_provider of this ZoneCreateParams.  # noqa: E501

        Specifies the system provider for the access zone.  # noqa: E501

        :return: The system_provider of this ZoneCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._system_provider

    @system_provider.setter
    def system_provider(self, system_provider):
        """Sets the system_provider of this ZoneCreateParams.

        Specifies the system provider for the access zone.  # noqa: E501

        :param system_provider: The system_provider of this ZoneCreateParams.  # noqa: E501
        :type: str
        """

        self._system_provider = system_provider

    @property
    def user_mapping_rules(self):
        """Gets the user_mapping_rules of this ZoneCreateParams.  # noqa: E501

        Specifies the current ID mapping rules.  # noqa: E501

        :return: The user_mapping_rules of this ZoneCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_mapping_rules

    @user_mapping_rules.setter
    def user_mapping_rules(self, user_mapping_rules):
        """Sets the user_mapping_rules of this ZoneCreateParams.

        Specifies the current ID mapping rules.  # noqa: E501

        :param user_mapping_rules: The user_mapping_rules of this ZoneCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._user_mapping_rules = user_mapping_rules

    @property
    def groupnet(self):
        """Gets the groupnet of this ZoneCreateParams.  # noqa: E501

        Groupnet identitier  # noqa: E501

        :return: The groupnet of this ZoneCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """Sets the groupnet of this ZoneCreateParams.

        Groupnet identitier  # noqa: E501

        :param groupnet: The groupnet of this ZoneCreateParams.  # noqa: E501
        :type: str
        """

        self._groupnet = groupnet

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
        if not isinstance(other, ZoneCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
