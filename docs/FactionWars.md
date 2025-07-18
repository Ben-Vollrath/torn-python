# FactionWars


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranked** | [**FactionRankedWar**](FactionRankedWar.md) |  | 
**raids** | [**List[FactionRaidWar]**](FactionRaidWar.md) |  | 
**territory** | [**List[FactionTerritoryWar]**](FactionTerritoryWar.md) |  | 

## Example

```python
from openapi_client.models.faction_wars import FactionWars

# TODO update the JSON string below
json = "{}"
# create an instance of FactionWars from a JSON string
faction_wars_instance = FactionWars.from_json(json)
# print the JSON string representation of the object
print(FactionWars.to_json())

# convert the object into a dict
faction_wars_dict = faction_wars_instance.to_dict()
# create an instance of FactionWars from a dict
faction_wars_from_dict = FactionWars.from_dict(faction_wars_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


