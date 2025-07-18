# FactionTerritoryWarfare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**territory** | [**FactionTerritoryEnum**](FactionTerritoryEnum.md) |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**target** | **int** |  | 
**aggressor** | [**FactionTerritoryWarFaction**](FactionTerritoryWarFaction.md) |  | 
**defender** | [**FactionTerritoryWarFaction**](FactionTerritoryWarFaction.md) |  | 
**result** | **str** |  | 

## Example

```python
from openapi_client.models.faction_territory_warfare import FactionTerritoryWarfare

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarfare from a JSON string
faction_territory_warfare_instance = FactionTerritoryWarfare.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarfare.to_json())

# convert the object into a dict
faction_territory_warfare_dict = faction_territory_warfare_instance.to_dict()
# create an instance of FactionTerritoryWarfare from a dict
faction_territory_warfare_from_dict = FactionTerritoryWarfare.from_dict(faction_territory_warfare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


