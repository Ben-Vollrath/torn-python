# FactionTerritoryWarReportFaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **int** |  | 
**joins** | **int** |  | 
**clears** | **int** |  | 
**is_aggressor** | **bool** |  | 
**members** | [**List[FactionTerritoryWarReportMembers]**](FactionTerritoryWarReportMembers.md) |  | 

## Example

```python
from openapi_client.models.faction_territory_war_report_faction import FactionTerritoryWarReportFaction

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarReportFaction from a JSON string
faction_territory_war_report_faction_instance = FactionTerritoryWarReportFaction.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarReportFaction.to_json())

# convert the object into a dict
faction_territory_war_report_faction_dict = faction_territory_war_report_faction_instance.to_dict()
# create an instance of FactionTerritoryWarReportFaction from a dict
faction_territory_war_report_faction_from_dict = FactionTerritoryWarReportFaction.from_dict(faction_territory_war_report_faction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


