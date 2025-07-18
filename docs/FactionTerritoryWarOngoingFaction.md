# FactionTerritoryWarOngoingFaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **int** |  | 
**is_aggressor** | **bool** |  | 
**chain** | **int** |  | 
**player_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.faction_territory_war_ongoing_faction import FactionTerritoryWarOngoingFaction

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarOngoingFaction from a JSON string
faction_territory_war_ongoing_faction_instance = FactionTerritoryWarOngoingFaction.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarOngoingFaction.to_json())

# convert the object into a dict
faction_territory_war_ongoing_faction_dict = faction_territory_war_ongoing_faction_instance.to_dict()
# create an instance of FactionTerritoryWarOngoingFaction from a dict
faction_territory_war_ongoing_faction_from_dict = FactionTerritoryWarOngoingFaction.from_dict(faction_territory_war_ongoing_faction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


