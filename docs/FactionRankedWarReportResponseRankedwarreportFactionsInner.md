# FactionRankedWarReportResponseRankedwarreportFactionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **int** |  | 
**attacks** | **int** |  | 
**rank** | [**FactionRankedWarReportResponseRankedwarreportFactionsInnerRank**](FactionRankedWarReportResponseRankedwarreportFactionsInnerRank.md) |  | 
**rewards** | [**FactionRankedWarReportResponseRankedwarreportFactionsInnerRewards**](FactionRankedWarReportResponseRankedwarreportFactionsInnerRewards.md) |  | 
**members** | [**List[FactionRankedWarReportResponseRankedwarreportFactionsInnerMembersInner]**](FactionRankedWarReportResponseRankedwarreportFactionsInnerMembersInner.md) |  | 

## Example

```python
from openapi_client.models.faction_ranked_war_report_response_rankedwarreport_factions_inner import FactionRankedWarReportResponseRankedwarreportFactionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRankedWarReportResponseRankedwarreportFactionsInner from a JSON string
faction_ranked_war_report_response_rankedwarreport_factions_inner_instance = FactionRankedWarReportResponseRankedwarreportFactionsInner.from_json(json)
# print the JSON string representation of the object
print(FactionRankedWarReportResponseRankedwarreportFactionsInner.to_json())

# convert the object into a dict
faction_ranked_war_report_response_rankedwarreport_factions_inner_dict = faction_ranked_war_report_response_rankedwarreport_factions_inner_instance.to_dict()
# create an instance of FactionRankedWarReportResponseRankedwarreportFactionsInner from a dict
faction_ranked_war_report_response_rankedwarreport_factions_inner_from_dict = FactionRankedWarReportResponseRankedwarreportFactionsInner.from_dict(faction_ranked_war_report_response_rankedwarreport_factions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


