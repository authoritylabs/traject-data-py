"""
    Traject Data • SERP Data API

    Traject Data • trajectdata.com • SERP Data API • SERP Data API for Scale | Locale SEO | Agencies | Brands  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: support@trajectdata.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import traject_data
from traject_data.api.serp_api import SerpApi  # noqa: E501


class TestSerpApi(unittest.TestCase):
    """SerpApi unit test stubs"""

    def setUp(self):
        self.api = SerpApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_engine_locale(self):
        """Test case for get_engine_locale

        Locale details for a given engine  # noqa: E501
        """
        pass

    def test_get_locales(self):
        """Test case for get_locales

        Fetch supported locales for a given engine  # noqa: E501
        """
        pass

    def test_get_serp(self):
        """Test case for get_serp

        Fetches SERP json  # noqa: E501
        """
        pass

    def test_get_serp_html(self):
        """Test case for get_serp_html

        Fetches SERP html  # noqa: E501
        """
        pass

    def test_post_keyword(self):
        """Test case for post_keyword

        Create keyword search  # noqa: E501
        """
        pass

    def test_post_keyword_priority(self):
        """Test case for post_keyword_priority

        Priority create keyword search  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()