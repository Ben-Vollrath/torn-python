# FactionTerritoryWar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**war_id** | **int** |  | 
**territory** | **str** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**target** | **int** | The score target of the war. | 
**winner** | **int** |  | [optional] 
**factions** | [**List[FactionTerritoryWarParticipant]**](FactionTerritoryWarParticipant.md) | The factions involved in the territory war. | 

## Example

```python
from openapi_client.models.faction_territory_war import FactionTerritoryWar

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWar from a JSON string
faction_territory_war_instance = FactionTerritoryWar.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWar.to_json())

# convert the object into a dict
faction_territory_war_dict = faction_territory_war_instance.to_dict()
# create an instance of FactionTerritoryWar from a dict
faction_territory_war_from_dict = FactionTerritoryWar.from_dict(faction_territory_war_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


