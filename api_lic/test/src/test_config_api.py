# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cli_lic
from cli_lic.rest import ApiException
from cli_lic.apis.config_api import ConfigApi


class TestConfigApi(unittest.TestCase):
    """ ConfigApi unit test stubs """

    def setUp(self):
        self.api = cli_lic.apis.config_api.ConfigApi()

    def tearDown(self):
        pass

    def test_config_payment_get(self):
        """
        Test case for config_payment_get

        
        """
        pass

    def test_config_payment_patch(self):
        """
        Test case for config_payment_patch

        
        """
        pass

    def test_email_template_list_get(self):
        """
        Test case for email_template_list_get

        
        """
        pass

    def test_email_template_name_get(self):
        """
        Test case for email_template_name_get

        
        """
        pass

    def test_email_template_name_patch(self):
        """
        Test case for email_template_name_patch

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
