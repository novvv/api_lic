# coding: utf-8

"""
    LICENSE API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cli_lic
from cli_lic.rest import ApiException
from cli_lic.apis.user_api import UserApi

from api_lic.test.settings import *

class TestUserApi(unittest.TestCase):
    """ UserApi unit test stubs """

    def setUp(self):
        self.api = cli_lic.apis.user_api.UserApi()
        self.license_lrn = []
        self.license_switch = []
        self.payment = []

    def tearDown(self):
        def clear(name):
            for uuid in getattr(self,name):
                try:
                    m=getattr(self.api,'{}_{}_uuid_delete'.format(name,name))
                    args={'{}_uuid'.format(name):uuid}
                    m(**args)
                except Exception as e:
                    print('tear down warning deleting {} {}:{}'.format(name,uuid,e))
                    pass
        auth()
        for name in ('license_lrn','license_switch','payment'):
            clear(name)

    def test_home_get(self):
        """
        Test case for home_get

        
        """
        auth_user()
        ret=self.api.home_get()
        assert (ret.success)
        print(ret)
        pass

    def test_home_patch(self):
        """
        Test case for home_patch


        """
        pass

    def test_license_lrn_license_lrn_uuid_delete(self):
        """
        Test case for license_lrn_license_lrn_uuid_delete


        """
        if not self.license_lrn:
            self.test_license_lrn_post()
        ret=self.api.license_lrn_license_lrn_uuid_delete(license_lrn_uuid=self.license_lrn[0])
        assert(ret.success)
        del self.license_lrn[0]
        pass

    def test_license_lrn_license_lrn_uuid_get(self):
        """
        Test case for license_lrn_license_lrn_uuid_get


        """
        if not self.license_lrn:
            self.test_license_lrn_post()
        ret=self.api.license_lrn_license_lrn_uuid_get(license_lrn_uuid=self.license_lrn[0])
        assert(ret.success)
        print(ret)
        pass

    def test_license_lrn_license_lrn_uuid_patch(self):
        """
        Test case for license_lrn_license_lrn_uuid_patch


        """
        if not self.license_lrn:
            self.test_license_lrn_post()
        data = dict(package_lrn_uuid=rand_package_lrn()[0], end_time=str(datetime.now(UTC) + timedelta(days=10)))
        ret=self.api.license_lrn_license_lrn_uuid_patch(license_lrn_uuid=self.license_lrn[0])
        assert(ret.success)
        print(ret)
        pass

    def test_license_lrn_list_get(self):
        """
        Test case for license_lrn_list_get


        """
        auth_user()
        ret = self.api.license_lrn_list_get()
        assert (ret.success)
        print(ret)
        pass

    def test_license_lrn_post(self):
        """
        Test case for license_lrn_post


        """
        auth_user()
        package_lrn_uuid = rand_package_lrn()[0]
        data=dict(package_lrn_uuid = package_lrn_uuid,ip=ip(),
                  start_time=str(datetime.utcnow()),
                  end_time=str(datetime.utcnow()+timedelta(days=random.randint(30,120)))
                  )
        old = self.api.license_lrn_list_get(package_lrn_uuid=package_lrn_uuid)
        if old.payload.items:#clean duplicates
            self.api.license_lrn_license_lrn_uuid_delete(
                license_lrn_uuid=old.payload.items[0].license_lrn_uuid)
        ret = self.api.license_lrn_post(body=data) # main test
        assert (ret.success)
        self.license_lrn.append(ret.object_uuid)
        print(ret)
        pass

    def test_license_switch_license_switch_uuid_delete(self):
        """
        Test case for license_switch_license_switch_uuid_delete


        """
        if not self.license_switch:
            self.test_license_switch_post()
        ret=self.api.license_switch_license_switch_uuid_delete(license_switch_uuid=self.license_switch[0])
        assert(ret.success)
        del self.license_switch[0]
        pass

    def test_license_switch_license_switch_uuid_get(self):
        """
        Test case for license_switch_license_switch_uuid_get


        """
        if not self.license_switch:
            self.test_license_switch_post()
        ret=self.api.license_switch_license_switch_uuid_get(license_switch_uuid=self.license_switch[0])
        assert(ret.success)
        print(ret)
        pass

    def test_license_switch_license_switch_uuid_patch(self):
        """
        Test case for license_switch_license_switch_uuid_patch


        """
        if not self.license_switch:
            self.test_license_switch_post()
        data = dict(package_switch_uuid=rand_package_switch()[0], end_time=str(datetime.now(UTC) + timedelta(days=10)))
        ret=self.api.license_switch_license_switch_uuid_patch(license_switch_uuid=self.license_switch[0],body=data)
        assert(ret.success)
        print(ret)
        pass

    def test_license_switch_list_get(self):
        """
        Test case for license_switch_list_get


        """
        auth_user()
        ret=self.api.license_switch_list_get()
        assert (ret.success)
        print(ret)
        pass

    def test_license_switch_post(self):
        """
        Test case for license_switch_post


        """
        auth_user()
        package_switch_uuid = rand_package_switch()[0]
        data = dict(package_switch_uuid =package_switch_uuid, ip=ip())
        old = self.api.license_switch_list_get(package_switch_uuid=package_switch_uuid)
        if old.payload.items:
            self.api.license_switch_license_switch_uuid_delete(license_switch_uuid=old.payload.items[0].license_switch_uuid)
        ret = self.api.license_switch_post(body=data)
        assert (ret.success)
        self.license_switch.append(ret.object_uuid)
        print(ret)
        pass

    def test_notification_list_get(self):
        """
        Test case for notification_list_get


        """
        auth_user()
        ret = self.api.notification_list_get()
        assert (ret.success)
        pass

    def test_payment_list_get(self):
        """
        Test case for payment_list_get


        """
        auth_user()
        ret = self.api.payment_list_get()
        assert (ret.success)
        print(ret)
        pass

    def test_payment_payment_uuid_delete(self):
        """
        Test case for payment_payment_uuid_delete


        """
        pass

    def test_payment_payment_uuid_get(self):
        """
        Test case for payment_payment_uuid_get


        """
        pass

    def test_payment_payment_uuid_patch(self):
        """
        Test case for payment_payment_uuid_patch


        """
        pass

    def test_payment_paypal_post(self):
        """
        Test case for payment_paypal_post


        """
        pass

    def test_payment_post(self):
        """
        Test case for payment_post


        """
        auth_user()

        try:
            license_lrn_uuid = rand_license_lrn()[0]
        except:
            self.test_license_lrn_post()
            license_lrn_uuid = rand_license_lrn()[0]
        try:
            license_switch_uuid = rand_license_switch()[0]
        except:
            self.test_license_switch_post()
            license_switch_uuid = rand_license_switch()[0]

        data = dict(license_lrn_uuid =license_lrn_uuid ,
                    license_switch_uuid=license_switch_uuid,
                    amount_lrn=random.randint(1,1000)/10.0,
                    amount_swwitch=random.randint(1, 1000/10.0),
                    type=random.choice(['paypal','strip']))
        print(json.dumps(data))
        ret=self.api.payment_post(body=data)
        assert(ret.success)

        try:
            license_switch_uuid = rand_license_switch()[0]
        except:
            self.test_license_switch_post()
            license_switch_uuid = rand_license_switch()[0]
        data = dict(license_switch_uuid = license_switch_uuid , amount=random.randint(1, 1000),
                        type=random.choice(['paypal', 'strip']))
        ret = self.api.payment_post(body=data)
        assert (ret.success)
        pass

    def test_payment_stripe_post(self):
        """
        Test case for payment_stripe_post


        """
        pass


if __name__ == '__main__':
    unittest.main()
