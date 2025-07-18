# FactionTerritory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**FactionTerritoryEnum**](FactionTerritoryEnum.md) |  | 
**acquired_at** | **int** |  | 
**sector** | **int** |  | 
**size** | **int** |  | 
**density** | **int** |  | 
**slots** | **int** |  | 
**respect** | **int** |  | 
**coordinates** | [**TornTerritoryCoordinates**](TornTerritoryCoordinates.md) |  | 
**racket** | [**TornRacket**](TornRacket.md) |  | 

## Example

```python
from openapi_client.models.faction_territory import FactionTerritory

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritory from a JSON string
faction_territory_instance = FactionTerritory.from_json(json)
# print the JSON string representation of the object
print(FactionTerritory.to_json())

# convert the object into a dict
faction_territory_dict = faction_territory_instance.to_dict()
# create an instance of FactionTerritory from a dict
faction_territory_from_dict = FactionTerritory.from_dict(faction_territory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


