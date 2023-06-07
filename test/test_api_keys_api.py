# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import conekta
from conekta import ApiClient
from conekta.api.api_keys_api import ApiKeysApi  # noqa: E501
from conekta.rest import ApiException
from test.test_utils import get_base_path


class TestApiKeysApi(unittest.TestCase):
    """ApiKeysApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.api_keys_api.ApiKeysApi(ApiClient(
            configuration=conekta.Configuration(host=get_base_path())
        ))  # noqa: E501

    def tearDown(self):
        pass

    def test_create_api_key(self):
        """Test case for create_api_key

        Create Api Key  # noqa: E501
        """
        accept_language = 'es'
        api_key_request = conekta.ApiKeyRequest(
            active=True,
            description='description',
            role='private'
        )
        response = self.api.create_api_key(api_key_request, accept_language)
        self.assertIsNotNone(response)

    def test_delete_api_key(self):
        """Test case for delete_api_key

        Delete Api Key  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.delete_api_key('64625cc9f3e02c00163f5e4d', accept_language)
        self.assertIsNotNone(response)

    def test_get_api_key(self):
        """Test case for get_api_key

        Get Api Key  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_api_key('64625cc9f3e02c00163f5e4d', accept_language)
        self.assertIsNotNone(response)

    def test_get_api_keys(self):
        """Test case for get_api_keys

        Get list of Api Keys  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.get_api_keys(accept_language, limit=20)
        self.assertIsNotNone(response)

    def test_update_api_key(self):
        """Test case for update_api_key

        Update Api Key  # noqa: E501
        """
        accept_language = 'es'
        api_key_update_request = conekta.ApiKeyUpdateRequest(
            active=False,
            description='description'
        )
        response = self.api.update_api_key('64625cc9f3e02c00163f5e4d', accept_language, api_key_update_request)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
