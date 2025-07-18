# FactionTerritoryWarReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**territory** | [**FactionTerritoryEnum**](FactionTerritoryEnum.md) |  | 
**started_at** | **int** |  | 
**ended_at** | **int** |  | 
**winner** | **int** |  | 
**result** | **str** |  | 
**factions** | [**List[FactionTerritoryWarReportFaction]**](FactionTerritoryWarReportFaction.md) |  | 

## Example

```python
from openapi_client.models.faction_territory_war_report import FactionTerritoryWarReport

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarReport from a JSON string
faction_territory_war_report_instance = FactionTerritoryWarReport.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarReport.to_json())

# convert the object into a dict
faction_territory_war_report_dict = faction_territory_war_report_instance.to_dict()
# create an instance of FactionTerritoryWarReport from a dict
faction_territory_war_report_from_dict = FactionTerritoryWarReport.from_dict(faction_territory_war_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


