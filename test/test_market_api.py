# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.market_api import MarketApi


class TestMarketApi(unittest.TestCase):
    """MarketApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MarketApi()

    def tearDown(self) -> None:
        pass

    def test_ad0c908328835d9672d157fe84eac884(self) -> None:
        """Test case for ad0c908328835d9672d157fe84eac884

        Get current server time
        """
        pass

    def test_call_17e406574ff1eb686891c0fb0e15343a(self) -> None:
        """Test case for call_17e406574ff1eb686891c0fb0e15343a

        Get properties market listings
        """
        pass

    def test_call_22a00095ad734485b6dacdc12c1f62ff(self) -> None:
        """Test case for call_22a00095ad734485b6dacdc12c1f62ff

        Get all available market selections
        """
        pass

    def test_call_38cd1a2c47e266a703a13e0dd401f4a9(self) -> None:
        """Test case for call_38cd1a2c47e266a703a13e0dd401f4a9

        Get properties rental listings
        """
        pass

    def test_call_422876deda064e2f3a2cc3c4bf6d73a9(self) -> None:
        """Test case for call_422876deda064e2f3a2cc3c4bf6d73a9

        Get bazaar directory
        """
        pass

    def test_call_8254489388603bf1b21740e6f71bef06(self) -> None:
        """Test case for call_8254489388603bf1b21740e6f71bef06

        Get item specialized bazaar directory
        """
        pass

    def test_call_8e78be3fa3d353f59f8654fcc1c2199c(self) -> None:
        """Test case for call_8e78be3fa3d353f59f8654fcc1c2199c

        Get any Market selection
        """
        pass

    def test_f535a33bf405e7bd60918e536f827e5c(self) -> None:
        """Test case for f535a33bf405e7bd60918e536f827e5c

        Get item market listings
        """
        pass


if __name__ == '__main__':
    unittest.main()
