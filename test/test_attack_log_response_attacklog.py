# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.attack_log_response_attacklog import AttackLogResponseAttacklog

class TestAttackLogResponseAttacklog(unittest.TestCase):
    """AttackLogResponseAttacklog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttackLogResponseAttacklog:
        """Test AttackLogResponseAttacklog
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttackLogResponseAttacklog`
        """
        model = AttackLogResponseAttacklog()
        if include_optional:
            return AttackLogResponseAttacklog(
                log = [
                    openapi_client.models.attack_log.AttackLog(
                        text = '', 
                        timestamp = 56, 
                        action = 'attackerhosp', 
                        icon = '', 
                        attacker = openapi_client.models.attack_log_attacker.AttackLog_attacker(
                            id = 56, 
                            name = '', 
                            item = openapi_client.models.attack_log_attacker_item.AttackLog_attacker_item(
                                id = 56, 
                                name = '', ), ), 
                        defender = openapi_client.models.attack_log_defender.AttackLog_defender(
                            id = 56, 
                            name = '', ), 
                        attacker_item = openapi_client.models.attack_log_attacker_item_1.AttackLog_attacker_item_1(
                            id = 56, 
                            name = '', ), )
                    ],
                summary = [
                    openapi_client.models.attack_log_summary.AttackLogSummary(
                        id = 56, 
                        name = '', 
                        hits = 56, 
                        misses = 56, 
                        damage = 56, )
                    ]
            )
        else:
            return AttackLogResponseAttacklog(
                log = [
                    openapi_client.models.attack_log.AttackLog(
                        text = '', 
                        timestamp = 56, 
                        action = 'attackerhosp', 
                        icon = '', 
                        attacker = openapi_client.models.attack_log_attacker.AttackLog_attacker(
                            id = 56, 
                            name = '', 
                            item = openapi_client.models.attack_log_attacker_item.AttackLog_attacker_item(
                                id = 56, 
                                name = '', ), ), 
                        defender = openapi_client.models.attack_log_defender.AttackLog_defender(
                            id = 56, 
                            name = '', ), 
                        attacker_item = openapi_client.models.attack_log_attacker_item_1.AttackLog_attacker_item_1(
                            id = 56, 
                            name = '', ), )
                    ],
                summary = [
                    openapi_client.models.attack_log_summary.AttackLogSummary(
                        id = 56, 
                        name = '', 
                        hits = 56, 
                        misses = 56, 
                        damage = 56, )
                    ],
        )
        """

    def testAttackLogResponseAttacklog(self):
        """Test AttackLogResponseAttacklog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
