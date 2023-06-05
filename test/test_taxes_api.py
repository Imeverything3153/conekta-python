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
from conekta.api.taxes_api import TaxesApi  # noqa: E501
from conekta.rest import ApiException


class TestTaxesApi(unittest.TestCase):
    """TaxesApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.taxes_api.TaxesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_orders_create_taxes(self):
        """Test case for orders_create_taxes

        Create Tax  # noqa: E501
        """
        pass

    def test_orders_delete_taxes(self):
        """Test case for orders_delete_taxes

        Delete Tax  # noqa: E501
        """
        pass

    def test_orders_update_taxes(self):
        """Test case for orders_update_taxes

        Update Tax  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
