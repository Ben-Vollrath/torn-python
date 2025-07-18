# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.personal_stats_travel import PersonalStatsTravel

class TestPersonalStatsTravel(unittest.TestCase):
    """PersonalStatsTravel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonalStatsTravel:
        """Test PersonalStatsTravel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonalStatsTravel`
        """
        model = PersonalStatsTravel()
        if include_optional:
            return PersonalStatsTravel(
                travel = openapi_client.models.personal_stats_travel_travel.PersonalStatsTravel_travel(
                    total = 56, 
                    time_spent = 56, 
                    items_bought = 56, 
                    hunting = openapi_client.models.personal_stats_travel_travel_hunting.PersonalStatsTravel_travel_hunting(
                        skill = 56, ), 
                    attacks_won = 56, 
                    defends_lost = 56, 
                    argentina = 56, 
                    canada = 56, 
                    cayman_islands = 56, 
                    china = 56, 
                    hawaii = 56, 
                    japan = 56, 
                    mexico = 56, 
                    united_arab_emirates = 56, 
                    united_kingdom = 56, 
                    south_africa = 56, 
                    switzerland = 56, )
            )
        else:
            return PersonalStatsTravel(
                travel = openapi_client.models.personal_stats_travel_travel.PersonalStatsTravel_travel(
                    total = 56, 
                    time_spent = 56, 
                    items_bought = 56, 
                    hunting = openapi_client.models.personal_stats_travel_travel_hunting.PersonalStatsTravel_travel_hunting(
                        skill = 56, ), 
                    attacks_won = 56, 
                    defends_lost = 56, 
                    argentina = 56, 
                    canada = 56, 
                    cayman_islands = 56, 
                    china = 56, 
                    hawaii = 56, 
                    japan = 56, 
                    mexico = 56, 
                    united_arab_emirates = 56, 
                    united_kingdom = 56, 
                    south_africa = 56, 
                    switzerland = 56, ),
        )
        """

    def testPersonalStatsTravel(self):
        """Test PersonalStatsTravel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
