# FactionRankedWarReportResponseRankedwarreport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**start** | **int** | Timestamp the war started at. | 
**end** | **int** | Timestamp the war ended at. | 
**winner** | **int** |  | 
**forfeit** | **bool** |  | 
**factions** | [**List[FactionRankedWarReportResponseRankedwarreportFactionsInner]**](FactionRankedWarReportResponseRankedwarreportFactionsInner.md) |  | 

## Example

```python
from openapi_client.models.faction_ranked_war_report_response_rankedwarreport import FactionRankedWarReportResponseRankedwarreport

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRankedWarReportResponseRankedwarreport from a JSON string
faction_ranked_war_report_response_rankedwarreport_instance = FactionRankedWarReportResponseRankedwarreport.from_json(json)
# print the JSON string representation of the object
print(FactionRankedWarReportResponseRankedwarreport.to_json())

# convert the object into a dict
faction_ranked_war_report_response_rankedwarreport_dict = faction_ranked_war_report_response_rankedwarreport_instance.to_dict()
# create an instance of FactionRankedWarReportResponseRankedwarreport from a dict
faction_ranked_war_report_response_rankedwarreport_from_dict = FactionRankedWarReportResponseRankedwarreport.from_dict(faction_ranked_war_report_response_rankedwarreport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


