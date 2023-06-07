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
from conekta.api.taxes_api import TaxesApi  # noqa: E501
from conekta.rest import ApiException
from test.test_utils import get_base_path


class TestTaxesApi(unittest.TestCase):
    """TaxesApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.taxes_api.TaxesApi(ApiClient(
            configuration=conekta.Configuration(host=get_base_path())
        ))  # noqa: E501

    def tearDown(self):
        pass

    def test_orders_create_taxes(self):
        """Test case for orders_create_taxes

        Create Tax  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.OrderTaxRequest(
            amount=100,
            description='desc'
        )
        response = self.api.orders_create_taxes('ord_2tUigJ8DgBhbp6w5D', rq, accept_language)
        self.assertIsNotNone(response)

    def test_orders_delete_taxes(self):
        """Test case for orders_delete_taxes

        Delete Tax  # noqa: E501
        """
        accept_language = 'es'
        response = self.api.orders_delete_taxes('ord_2tUigJ8DgBhbp6w5D', 'tax_lin_2tVzVp6AAptCRHhgt', accept_language)
        self.assertIsNotNone(response)

    def test_orders_update_taxes(self):
        """Test case for orders_update_taxes

        Update Tax  # noqa: E501
        """
        accept_language = 'es'
        rq = conekta.UpdateOrderTaxRequest(
            amount=100,
            description='desc'
        )
        response = self.api.orders_update_taxes('ord_2tUigJ8DgBhbp6w5D', 'tax_lin_2tVzVp6AAptCRHhgt', rq,
                                                accept_language)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
