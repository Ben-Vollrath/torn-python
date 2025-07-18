# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.model8e78be3fa3d353f59f8654fcc1c2199c200_response import Model8e78be3fa3d353f59f8654fcc1c2199c200Response

class TestModel8e78be3fa3d353f59f8654fcc1c2199c200Response(unittest.TestCase):
    """Model8e78be3fa3d353f59f8654fcc1c2199c200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Model8e78be3fa3d353f59f8654fcc1c2199c200Response:
        """Test Model8e78be3fa3d353f59f8654fcc1c2199c200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Model8e78be3fa3d353f59f8654fcc1c2199c200Response`
        """
        model = Model8e78be3fa3d353f59f8654fcc1c2199c200Response()
        if include_optional:
            return Model8e78be3fa3d353f59f8654fcc1c2199c200Response(
                bazaar = openapi_client.models.bazaar_specialized.BazaarSpecialized(
                    specialized = [
                        null
                        ], ),
                itemmarket = openapi_client.models.item_market.ItemMarket(
                    item = openapi_client.models.item_market_item.ItemMarketItem(
                        id = 56, 
                        name = '', 
                        type = '', 
                        average_price = 56, ), 
                    listings = [
                        null
                        ], 
                    cache_timestamp = 56, ),
                metadata = openapi_client.models.request_metadata_with_links.RequestMetadataWithLinks(
                    links = openapi_client.models.request_links.RequestLinks(
                        next = '', 
                        prev = '', ), ),
                properties = openapi_client.models.market_property_details.MarketPropertyDetails(
                    listings = [
                        openapi_client.models.market_property_details_listings_inner.MarketPropertyDetails_listings_inner(
                            happy = 56, 
                            cost = 56, 
                            market_price = 56, 
                            upkeep = 56, 
                            modifications = [
                                'Hot Tub'
                                ], )
                        ], 
                    property = openapi_client.models.basic_property.BasicProperty(
                        id = 56, 
                        name = '', ), ),
                selections = [
                    null
                    ],
                timestamp = 56
            )
        else:
            return Model8e78be3fa3d353f59f8654fcc1c2199c200Response(
                bazaar = openapi_client.models.bazaar_specialized.BazaarSpecialized(
                    specialized = [
                        null
                        ], ),
                itemmarket = openapi_client.models.item_market.ItemMarket(
                    item = openapi_client.models.item_market_item.ItemMarketItem(
                        id = 56, 
                        name = '', 
                        type = '', 
                        average_price = 56, ), 
                    listings = [
                        null
                        ], 
                    cache_timestamp = 56, ),
                metadata = openapi_client.models.request_metadata_with_links.RequestMetadataWithLinks(
                    links = openapi_client.models.request_links.RequestLinks(
                        next = '', 
                        prev = '', ), ),
                properties = openapi_client.models.market_property_details.MarketPropertyDetails(
                    listings = [
                        openapi_client.models.market_property_details_listings_inner.MarketPropertyDetails_listings_inner(
                            happy = 56, 
                            cost = 56, 
                            market_price = 56, 
                            upkeep = 56, 
                            modifications = [
                                'Hot Tub'
                                ], )
                        ], 
                    property = openapi_client.models.basic_property.BasicProperty(
                        id = 56, 
                        name = '', ), ),
                selections = [
                    null
                    ],
                timestamp = 56,
        )
        """

    def testModel8e78be3fa3d353f59f8654fcc1c2199c200Response(self):
        """Test Model8e78be3fa3d353f59f8654fcc1c2199c200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
