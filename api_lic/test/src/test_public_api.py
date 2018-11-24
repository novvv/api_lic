# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cli_lic
from cli_lic.rest import ApiException
from cli_lic.apis.public_api import PublicApi


class TestPublicApi(unittest.TestCase):
    """ PublicApi unit test stubs """

    def setUp(self):
        self.api = cli_lic.apis.public_api.PublicApi()

    def tearDown(self):
        pass

    def test_file_download_download_token_get(self):
        """
        Test case for file_download_download_token_get

        
        """
        pass

    def test_file_download_link_belongs_to_uuid_uuid_get(self):
        """
        Test case for file_download_link_belongs_to_uuid_uuid_get

        
        """
        pass

    def test_file_file_uuid_get(self):
        """
        Test case for file_file_uuid_get

        
        """
        pass

    def test_file_list_get(self):
        """
        Test case for file_list_get

        
        """
        pass

    def test_file_list_tmp_get(self):
        """
        Test case for file_list_tmp_get

        
        """
        pass

    def test_file_post(self):
        """
        Test case for file_post

        
        """
        pass

    def test_image_file_name_get(self):
        """
        Test case for image_file_name_get

        
        """
        pass

    def test_image_post(self):
        """
        Test case for image_post

        
        """
        pass

    def test_package_lrn_list_get(self):
        """
        Test case for package_lrn_list_get

        
        """
        pass

    def test_package_switch_list_get(self):
        """
        Test case for package_switch_list_get

        
        """
        pass

    def test_package_switch_minute_table_get(self):
        """
        Test case for package_switch_minute_table_get

        
        """
        pass

    def test_package_switch_port_table_get(self):
        """
        Test case for package_switch_port_table_get

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
