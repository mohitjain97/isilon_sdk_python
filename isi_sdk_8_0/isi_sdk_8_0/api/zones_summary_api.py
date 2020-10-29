# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_8_0.api_client import ApiClient


class ZonesSummaryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_zones_summary(self, **kwargs):  # noqa: E501
        """get_zones_summary  # noqa: E501

        Retrieve access zone summary information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zones_summary(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str groupnet: Name of groupnet in which to list zones.
        :return: ZonesSummaryExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_zones_summary_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_zones_summary_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_zones_summary_with_http_info(self, **kwargs):  # noqa: E501
        """get_zones_summary  # noqa: E501

        Retrieve access zone summary information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zones_summary_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str groupnet: Name of groupnet in which to list zones.
        :return: ZonesSummaryExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['groupnet']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zones_summary" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'groupnet' in params:
            query_params.append(('groupnet', params['groupnet']))  # noqa: E501

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
            '/platform/1/zones-summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZonesSummaryExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_zones_summary_zone(self, zones_summary_zone, **kwargs):  # noqa: E501
        """get_zones_summary_zone  # noqa: E501

        Retrieve non-privileged access zone information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zones_summary_zone(zones_summary_zone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int zones_summary_zone: Retrieve non-privileged access zone information. (required)
        :return: ZonesSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_zones_summary_zone_with_http_info(zones_summary_zone, **kwargs)  # noqa: E501
        else:
            (data) = self.get_zones_summary_zone_with_http_info(zones_summary_zone, **kwargs)  # noqa: E501
            return data

    def get_zones_summary_zone_with_http_info(self, zones_summary_zone, **kwargs):  # noqa: E501
        """get_zones_summary_zone  # noqa: E501

        Retrieve non-privileged access zone information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zones_summary_zone_with_http_info(zones_summary_zone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int zones_summary_zone: Retrieve non-privileged access zone information. (required)
        :return: ZonesSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zones_summary_zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zones_summary_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zones_summary_zone' is set
        if ('zones_summary_zone' not in params or
                params['zones_summary_zone'] is None):
            raise ValueError("Missing the required parameter `zones_summary_zone` when calling `get_zones_summary_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zones_summary_zone' in params:
            path_params['ZonesSummaryZone'] = params['zones_summary_zone']  # noqa: E501

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
            '/platform/1/zones-summary/{ZonesSummaryZone}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZonesSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)