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


class CloudAccount(object):
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
        'account_id': 'str',
        'account_username': 'str',
        'birth_cluster_id': 'str',
        'enabled': 'bool',
        'key': 'str',
        'name': 'str',
        'proxy': 'str',
        'skip_account_check': 'bool',
        'skip_ssl_validation': 'bool',
        'storage_region': 'str',
        'telemetry_bucket': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_username': 'account_username',
        'birth_cluster_id': 'birth_cluster_id',
        'enabled': 'enabled',
        'key': 'key',
        'name': 'name',
        'proxy': 'proxy',
        'skip_account_check': 'skip_account_check',
        'skip_ssl_validation': 'skip_ssl_validation',
        'storage_region': 'storage_region',
        'telemetry_bucket': 'telemetry_bucket',
        'uri': 'uri'
    }

    def __init__(self, account_id=None, account_username=None, birth_cluster_id=None, enabled=None, key=None, name=None, proxy=None, skip_account_check=None, skip_ssl_validation=None, storage_region=None, telemetry_bucket=None, uri=None):  # noqa: E501
        """CloudAccount - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._account_username = None
        self._birth_cluster_id = None
        self._enabled = None
        self._key = None
        self._name = None
        self._proxy = None
        self._skip_account_check = None
        self._skip_ssl_validation = None
        self._storage_region = None
        self._telemetry_bucket = None
        self._uri = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_username is not None:
            self.account_username = account_username
        if birth_cluster_id is not None:
            self.birth_cluster_id = birth_cluster_id
        if enabled is not None:
            self.enabled = enabled
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if proxy is not None:
            self.proxy = proxy
        if skip_account_check is not None:
            self.skip_account_check = skip_account_check
        if skip_ssl_validation is not None:
            self.skip_ssl_validation = skip_ssl_validation
        if storage_region is not None:
            self.storage_region = storage_region
        if telemetry_bucket is not None:
            self.telemetry_bucket = telemetry_bucket
        if uri is not None:
            self.uri = uri

    @property
    def account_id(self):
        """Gets the account_id of this CloudAccount.  # noqa: E501

        (S3 only) The user id of the S3 account  # noqa: E501

        :return: The account_id of this CloudAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CloudAccount.

        (S3 only) The user id of the S3 account  # noqa: E501

        :param account_id: The account_id of this CloudAccount.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_username(self):
        """Gets the account_username of this CloudAccount.  # noqa: E501

        The username required to authenticate against the cloud service  # noqa: E501

        :return: The account_username of this CloudAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_username

    @account_username.setter
    def account_username(self, account_username):
        """Sets the account_username of this CloudAccount.

        The username required to authenticate against the cloud service  # noqa: E501

        :param account_username: The account_username of this CloudAccount.  # noqa: E501
        :type: str
        """

        self._account_username = account_username

    @property
    def birth_cluster_id(self):
        """Gets the birth_cluster_id of this CloudAccount.  # noqa: E501

        The guid of the cluster where this account was created  # noqa: E501

        :return: The birth_cluster_id of this CloudAccount.  # noqa: E501
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """Sets the birth_cluster_id of this CloudAccount.

        The guid of the cluster where this account was created  # noqa: E501

        :param birth_cluster_id: The birth_cluster_id of this CloudAccount.  # noqa: E501
        :type: str
        """

        self._birth_cluster_id = birth_cluster_id

    @property
    def enabled(self):
        """Gets the enabled of this CloudAccount.  # noqa: E501

        Whether this account is explicitly enabled or disabled by a user  # noqa: E501

        :return: The enabled of this CloudAccount.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CloudAccount.

        Whether this account is explicitly enabled or disabled by a user  # noqa: E501

        :param enabled: The enabled of this CloudAccount.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def key(self):
        """Gets the key of this CloudAccount.  # noqa: E501

        A valid authentication key for connecting to the cloud  # noqa: E501

        :return: The key of this CloudAccount.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CloudAccount.

        A valid authentication key for connecting to the cloud  # noqa: E501

        :param key: The key of this CloudAccount.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this CloudAccount.  # noqa: E501

        A unique name for this account  # noqa: E501

        :return: The name of this CloudAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudAccount.

        A unique name for this account  # noqa: E501

        :param name: The name of this CloudAccount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def proxy(self):
        """Gets the proxy of this CloudAccount.  # noqa: E501

        The id or name of a proxy to be used by this account  # noqa: E501

        :return: The proxy of this CloudAccount.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CloudAccount.

        The id or name of a proxy to be used by this account  # noqa: E501

        :param proxy: The proxy of this CloudAccount.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def skip_account_check(self):
        """Gets the skip_account_check of this CloudAccount.  # noqa: E501

        (Not recommended) Indicates whether to skip validation that the cloud account is still accessible  # noqa: E501

        :return: The skip_account_check of this CloudAccount.  # noqa: E501
        :rtype: bool
        """
        return self._skip_account_check

    @skip_account_check.setter
    def skip_account_check(self, skip_account_check):
        """Sets the skip_account_check of this CloudAccount.

        (Not recommended) Indicates whether to skip validation that the cloud account is still accessible  # noqa: E501

        :param skip_account_check: The skip_account_check of this CloudAccount.  # noqa: E501
        :type: bool
        """

        self._skip_account_check = skip_account_check

    @property
    def skip_ssl_validation(self):
        """Gets the skip_ssl_validation of this CloudAccount.  # noqa: E501

        Indicates whether to skip SSL certificate validation when connecting to the cloud  # noqa: E501

        :return: The skip_ssl_validation of this CloudAccount.  # noqa: E501
        :rtype: bool
        """
        return self._skip_ssl_validation

    @skip_ssl_validation.setter
    def skip_ssl_validation(self, skip_ssl_validation):
        """Sets the skip_ssl_validation of this CloudAccount.

        Indicates whether to skip SSL certificate validation when connecting to the cloud  # noqa: E501

        :param skip_ssl_validation: The skip_ssl_validation of this CloudAccount.  # noqa: E501
        :type: bool
        """

        self._skip_ssl_validation = skip_ssl_validation

    @property
    def storage_region(self):
        """Gets the storage_region of this CloudAccount.  # noqa: E501

        (S3 only) An appropriate region for the S3 account.  For example, faster access times may be gained by referencing a nearby region  # noqa: E501

        :return: The storage_region of this CloudAccount.  # noqa: E501
        :rtype: str
        """
        return self._storage_region

    @storage_region.setter
    def storage_region(self, storage_region):
        """Sets the storage_region of this CloudAccount.

        (S3 only) An appropriate region for the S3 account.  For example, faster access times may be gained by referencing a nearby region  # noqa: E501

        :param storage_region: The storage_region of this CloudAccount.  # noqa: E501
        :type: str
        """

        self._storage_region = storage_region

    @property
    def telemetry_bucket(self):
        """Gets the telemetry_bucket of this CloudAccount.  # noqa: E501

        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider  # noqa: E501

        :return: The telemetry_bucket of this CloudAccount.  # noqa: E501
        :rtype: str
        """
        return self._telemetry_bucket

    @telemetry_bucket.setter
    def telemetry_bucket(self, telemetry_bucket):
        """Sets the telemetry_bucket of this CloudAccount.

        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider  # noqa: E501

        :param telemetry_bucket: The telemetry_bucket of this CloudAccount.  # noqa: E501
        :type: str
        """

        self._telemetry_bucket = telemetry_bucket

    @property
    def uri(self):
        """Gets the uri of this CloudAccount.  # noqa: E501

        A valid URI pointing to the location of the cloud storage  # noqa: E501

        :return: The uri of this CloudAccount.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CloudAccount.

        A valid URI pointing to the location of the cloud storage  # noqa: E501

        :param uri: The uri of this CloudAccount.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if not isinstance(other, CloudAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
