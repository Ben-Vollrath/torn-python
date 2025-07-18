# FactionTerritoryWarReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**territorywarreport** | [**List[FactionTerritoryWarReport]**](FactionTerritoryWarReport.md) |  | 

## Example

```python
from openapi_client.models.faction_territory_war_report_response import FactionTerritoryWarReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarReportResponse from a JSON string
faction_territory_war_report_response_instance = FactionTerritoryWarReportResponse.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarReportResponse.to_json())

# convert the object into a dict
faction_territory_war_report_response_dict = faction_territory_war_report_response_instance.to_dict()
# create an instance of FactionTerritoryWarReportResponse from a dict
faction_territory_war_report_response_from_dict = FactionTerritoryWarReportResponse.from_dict(faction_territory_war_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


