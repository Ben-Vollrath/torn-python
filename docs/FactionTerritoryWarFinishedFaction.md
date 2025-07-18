# FactionTerritoryWarFinishedFaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **int** |  | 
**is_aggressor** | **bool** |  | 

## Example

```python
from openapi_client.models.faction_territory_war_finished_faction import FactionTerritoryWarFinishedFaction

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarFinishedFaction from a JSON string
faction_territory_war_finished_faction_instance = FactionTerritoryWarFinishedFaction.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarFinishedFaction.to_json())

# convert the object into a dict
faction_territory_war_finished_faction_dict = faction_territory_war_finished_faction_instance.to_dict()
# create an instance of FactionTerritoryWarFinishedFaction from a dict
faction_territory_war_finished_faction_from_dict = FactionTerritoryWarFinishedFaction.from_dict(faction_territory_war_finished_faction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


