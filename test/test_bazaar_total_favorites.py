# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.bazaar_total_favorites import BazaarTotalFavorites

class TestBazaarTotalFavorites(unittest.TestCase):
    """BazaarTotalFavorites unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BazaarTotalFavorites:
        """Test BazaarTotalFavorites
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BazaarTotalFavorites`
        """
        model = BazaarTotalFavorites()
        if include_optional:
            return BazaarTotalFavorites(
                id = 56,
                name = '',
                is_open = True,
                total_favorites = 56
            )
        else:
            return BazaarTotalFavorites(
                id = 56,
                name = '',
                is_open = True,
                total_favorites = 56,
        )
        """

    def testBazaarTotalFavorites(self):
        """Test BazaarTotalFavorites"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
