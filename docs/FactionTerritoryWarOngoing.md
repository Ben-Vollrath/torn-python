# FactionTerritoryWarOngoing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**territory** | [**FactionTerritoryEnum**](FactionTerritoryEnum.md) |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**target** | **int** |  | 
**factions** | [**List[FactionTerritoryWarOngoingFaction]**](FactionTerritoryWarOngoingFaction.md) |  | 

## Example

```python
from openapi_client.models.faction_territory_war_ongoing import FactionTerritoryWarOngoing

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarOngoing from a JSON string
faction_territory_war_ongoing_instance = FactionTerritoryWarOngoing.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarOngoing.to_json())

# convert the object into a dict
faction_territory_war_ongoing_dict = faction_territory_war_ongoing_instance.to_dict()
# create an instance of FactionTerritoryWarOngoing from a dict
faction_territory_war_ongoing_from_dict = FactionTerritoryWarOngoing.from_dict(faction_territory_war_ongoing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


