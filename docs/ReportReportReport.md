# ReportReportReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money** | **int** |  | 
**strength** | **int** |  | 
**speed** | **int** |  | 
**dexterity** | **int** |  | 
**defense** | **int** |  | 
**total** | **int** |  | 
**top** | [**List[ReportWarrantDetails]**](ReportWarrantDetails.md) |  | 
**notable** | [**List[ReportWarrantDetails]**](ReportWarrantDetails.md) |  | 
**factions** | [**List[ReportHistoryFaction]**](ReportHistoryFaction.md) |  | 
**companies** | [**List[ReportHistoryCompany]**](ReportHistoryCompany.md) |  | 
**friends** | [**List[ReportFriendOrFoeUser]**](ReportFriendOrFoeUser.md) |  | 
**enemies** | [**List[ReportFriendOrFoeUser]**](ReportFriendOrFoeUser.md) |  | 
**balance** | **int** |  | 
**employees** | **int** |  | 
**wages** | [**ReportCompanyFinancialsWages**](ReportCompanyFinancialsWages.md) |  | 
**level** | **int** |  | 
**items** | [**List[ReportStockAnalysisItemsInner]**](ReportStockAnalysisItemsInner.md) |  | 
**bounties** | [**List[ReportAnonymousBountiesBountiesInner]**](ReportAnonymousBountiesBountiesInner.md) |  | 
**amount** | **int** |  | 
**until** | **int** |  | 

## Example

```python
from openapi_client.models.report_report_report import ReportReportReport

# TODO update the JSON string below
json = "{}"
# create an instance of ReportReportReport from a JSON string
report_report_report_instance = ReportReportReport.from_json(json)
# print the JSON string representation of the object
print(ReportReportReport.to_json())

# convert the object into a dict
report_report_report_dict = report_report_report_instance.to_dict()
# create an instance of ReportReportReport from a dict
report_report_report_from_dict = ReportReportReport.from_dict(report_report_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


