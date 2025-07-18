# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.report_stock_analysis import ReportStockAnalysis

class TestReportStockAnalysis(unittest.TestCase):
    """ReportStockAnalysis unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportStockAnalysis:
        """Test ReportStockAnalysis
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportStockAnalysis`
        """
        model = ReportStockAnalysis()
        if include_optional:
            return ReportStockAnalysis(
                items = [
                    openapi_client.models.report_stock_analysis_items_inner.ReportStockAnalysis_items_inner(
                        country = 'Mexico', 
                        item = openapi_client.models.report_stock_analysis_items_inner_item.ReportStockAnalysis_items_inner_item(
                            id = 56, 
                            name = '', 
                            price = 56, 
                            value = 56, 
                            due = 56, ), 
                        trip_duration = 56, 
                        hourly_profit = 56, )
                    ]
            )
        else:
            return ReportStockAnalysis(
                items = [
                    openapi_client.models.report_stock_analysis_items_inner.ReportStockAnalysis_items_inner(
                        country = 'Mexico', 
                        item = openapi_client.models.report_stock_analysis_items_inner_item.ReportStockAnalysis_items_inner_item(
                            id = 56, 
                            name = '', 
                            price = 56, 
                            value = 56, 
                            due = 56, ), 
                        trip_duration = 56, 
                        hourly_profit = 56, )
                    ],
        )
        """

    def testReportStockAnalysis(self):
        """Test ReportStockAnalysis"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
