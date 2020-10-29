# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_9_0_0.api_client import ApiClient


class SnapshotChangelistsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_changelist_entries(self, changelist, **kwargs):  # noqa: E501
        """get_changelist_entries  # noqa: E501

        Get entries from a changelist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_changelist_entries(changelist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str changelist: (required)
        :param bool diff_regions: Include snapshot diff regions in entry output.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: ChangelistEntriesExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_changelist_entries_with_http_info(changelist, **kwargs)  # noqa: E501
        else:
            (data) = self.get_changelist_entries_with_http_info(changelist, **kwargs)  # noqa: E501
            return data

    def get_changelist_entries_with_http_info(self, changelist, **kwargs):  # noqa: E501
        """get_changelist_entries  # noqa: E501

        Get entries from a changelist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_changelist_entries_with_http_info(changelist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str changelist: (required)
        :param bool diff_regions: Include snapshot diff regions in entry output.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: ChangelistEntriesExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['changelist', 'diff_regions', 'limit', 'resume']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_changelist_entries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'changelist' is set
        if ('changelist' not in params or
                params['changelist'] is None):
            raise ValueError("Missing the required parameter `changelist` when calling `get_changelist_entries`")  # noqa: E501

        if 'limit' in params and params['limit'] > 2048:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_changelist_entries`, must be a value less than or equal to `2048`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_changelist_entries`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_changelist_entries`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_changelist_entries`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'changelist' in params:
            path_params['Changelist'] = params['changelist']  # noqa: E501

        query_params = []
        if 'diff_regions' in params:
            query_params.append(('diff_regions', params['diff_regions']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/10/snapshot/changelists/{Changelist}/entries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChangelistEntriesExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_changelist_entry(self, changelist_entry_id, changelist, **kwargs):  # noqa: E501
        """get_changelist_entry  # noqa: E501

        Get a single entry from the changelist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_changelist_entry(changelist_entry_id, changelist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str changelist_entry_id: Get a single entry from the changelist. (required)
        :param str changelist: (required)
        :return: ChangelistEntries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_changelist_entry_with_http_info(changelist_entry_id, changelist, **kwargs)  # noqa: E501
        else:
            (data) = self.get_changelist_entry_with_http_info(changelist_entry_id, changelist, **kwargs)  # noqa: E501
            return data

    def get_changelist_entry_with_http_info(self, changelist_entry_id, changelist, **kwargs):  # noqa: E501
        """get_changelist_entry  # noqa: E501

        Get a single entry from the changelist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_changelist_entry_with_http_info(changelist_entry_id, changelist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str changelist_entry_id: Get a single entry from the changelist. (required)
        :param str changelist: (required)
        :return: ChangelistEntries
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['changelist_entry_id', 'changelist']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_changelist_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'changelist_entry_id' is set
        if ('changelist_entry_id' not in params or
                params['changelist_entry_id'] is None):
            raise ValueError("Missing the required parameter `changelist_entry_id` when calling `get_changelist_entry`")  # noqa: E501
        # verify the required parameter 'changelist' is set
        if ('changelist' not in params or
                params['changelist'] is None):
            raise ValueError("Missing the required parameter `changelist` when calling `get_changelist_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'changelist_entry_id' in params:
            path_params['ChangelistEntryId'] = params['changelist_entry_id']  # noqa: E501
        if 'changelist' in params:
            path_params['Changelist'] = params['changelist']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/10/snapshot/changelists/{Changelist}/entries/{ChangelistEntryId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChangelistEntries',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_changelist_lin(self, changelist_lin_id, changelist, **kwargs):  # noqa: E501
        """get_changelist_lin  # noqa: E501

        Get a single entry from the changelist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_changelist_lin(changelist_lin_id, changelist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int changelist_lin_id: Get a single entry from the changelist. (required)
        :param str changelist: (required)
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: ChangelistLins
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_changelist_lin_with_http_info(changelist_lin_id, changelist, **kwargs)  # noqa: E501
        else:
            (data) = self.get_changelist_lin_with_http_info(changelist_lin_id, changelist, **kwargs)  # noqa: E501
            return data

    def get_changelist_lin_with_http_info(self, changelist_lin_id, changelist, **kwargs):  # noqa: E501
        """get_changelist_lin  # noqa: E501

        Get a single entry from the changelist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_changelist_lin_with_http_info(changelist_lin_id, changelist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int changelist_lin_id: Get a single entry from the changelist. (required)
        :param str changelist: (required)
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: ChangelistLins
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['changelist_lin_id', 'changelist', 'limit', 'resume']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_changelist_lin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'changelist_lin_id' is set
        if ('changelist_lin_id' not in params or
                params['changelist_lin_id'] is None):
            raise ValueError("Missing the required parameter `changelist_lin_id` when calling `get_changelist_lin`")  # noqa: E501
        # verify the required parameter 'changelist' is set
        if ('changelist' not in params or
                params['changelist'] is None):
            raise ValueError("Missing the required parameter `changelist` when calling `get_changelist_lin`")  # noqa: E501

        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_changelist_lin`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_changelist_lin`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_changelist_lin`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_changelist_lin`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'changelist_lin_id' in params:
            path_params['ChangelistLinId'] = params['changelist_lin_id']  # noqa: E501
        if 'changelist' in params:
            path_params['Changelist'] = params['changelist']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/snapshot/changelists/{Changelist}/lins/{ChangelistLinId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChangelistLins',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_changelist_lins(self, changelist, **kwargs):  # noqa: E501
        """get_changelist_lins  # noqa: E501

        Get entries from a changelist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_changelist_lins(changelist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str changelist: (required)
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: ChangelistLinsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_changelist_lins_with_http_info(changelist, **kwargs)  # noqa: E501
        else:
            (data) = self.get_changelist_lins_with_http_info(changelist, **kwargs)  # noqa: E501
            return data

    def get_changelist_lins_with_http_info(self, changelist, **kwargs):  # noqa: E501
        """get_changelist_lins  # noqa: E501

        Get entries from a changelist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_changelist_lins_with_http_info(changelist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str changelist: (required)
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: ChangelistLinsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['changelist', 'limit', 'resume']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_changelist_lins" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'changelist' is set
        if ('changelist' not in params or
                params['changelist'] is None):
            raise ValueError("Missing the required parameter `changelist` when calling `get_changelist_lins`")  # noqa: E501

        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_changelist_lins`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_changelist_lins`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_changelist_lins`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_changelist_lins`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'changelist' in params:
            path_params['Changelist'] = params['changelist']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/snapshot/changelists/{Changelist}/lins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChangelistLinsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)