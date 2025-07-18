# FactionTerritoryWarFaction

The fields 'chain' and 'players_on_wall' exist only for wars with the result 'in_progress'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **int** |  | 
**chain** | **int** |  | [optional] 
**players_on_wall** | [**List[FactionTerritoryWarFactionWallPlayers]**](FactionTerritoryWarFactionWallPlayers.md) |  | [optional] 

## Example

```python
from openapi_client.models.faction_territory_war_faction import FactionTerritoryWarFaction

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarFaction from a JSON string
faction_territory_war_faction_instance = FactionTerritoryWarFaction.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarFaction.to_json())

# convert the object into a dict
faction_territory_war_faction_dict = faction_territory_war_faction_instance.to_dict()
# create an instance of FactionTerritoryWarFaction from a dict
faction_territory_war_faction_from_dict = FactionTerritoryWarFaction.from_dict(faction_territory_war_faction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


