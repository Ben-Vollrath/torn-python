# FactionTerritoryWarFinished


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**territory** | [**FactionTerritoryEnum**](FactionTerritoryEnum.md) |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**target** | **int** |  | 
**result** | [**FactionTerritoryWarResultEnum**](FactionTerritoryWarResultEnum.md) |  | 
**factions** | [**List[FactionTerritoryWarFinishedFaction]**](FactionTerritoryWarFinishedFaction.md) |  | 

## Example

```python
from openapi_client.models.faction_territory_war_finished import FactionTerritoryWarFinished

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarFinished from a JSON string
faction_territory_war_finished_instance = FactionTerritoryWarFinished.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarFinished.to_json())

# convert the object into a dict
faction_territory_war_finished_dict = faction_territory_war_finished_instance.to_dict()
# create an instance of FactionTerritoryWarFinished from a dict
faction_territory_war_finished_from_dict = FactionTerritoryWarFinished.from_dict(faction_territory_war_finished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


