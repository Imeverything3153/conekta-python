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
from conekta.api.events_api import EventsApi  # noqa: E501
from conekta.rest import ApiException


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = conekta.api.events_api.EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_event(self):
        """Test case for get_event

        Get Event  # noqa: E501
        """
        pass

    def test_get_events(self):
        """Test case for get_events

        Get list of Events  # noqa: E501
        """
        pass

    def test_resend_event(self):
        """Test case for resend_event

        Resend Event  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()