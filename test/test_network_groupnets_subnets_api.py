# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 5
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_1_0
from isi_sdk_8_1_0.api.network_groupnets_subnets_api import NetworkGroupnetsSubnetsApi  # noqa: E501
from isi_sdk_8_1_0.rest import ApiException


class TestNetworkGroupnetsSubnetsApi(unittest.TestCase):
    """NetworkGroupnetsSubnetsApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_1_0.api.network_groupnets_subnets_api.NetworkGroupnetsSubnetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_pools_pool_rebalance_ip(self):
        """Test case for create_pools_pool_rebalance_ip

        """
        pass

    def test_create_pools_pool_rule(self):
        """Test case for create_pools_pool_rule

        """
        pass

    def test_create_pools_pool_sc_resume_node(self):
        """Test case for create_pools_pool_sc_resume_node

        """
        pass

    def test_create_pools_pool_sc_suspend_node(self):
        """Test case for create_pools_pool_sc_suspend_node

        """
        pass

    def test_delete_pools_pool_rule(self):
        """Test case for delete_pools_pool_rule

        """
        pass

    def test_get_pools_pool_interfaces(self):
        """Test case for get_pools_pool_interfaces

        """
        pass

    def test_get_pools_pool_rule(self):
        """Test case for get_pools_pool_rule

        """
        pass

    def test_list_pools_pool_rules(self):
        """Test case for list_pools_pool_rules

        """
        pass

    def test_update_pools_pool_rule(self):
        """Test case for update_pools_pool_rule

        """
        pass


if __name__ == '__main__':
    unittest.main()
