# TornTerritory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**FactionTerritoryEnum**](FactionTerritoryEnum.md) |  | 
**sector** | **int** |  | 
**size** | **int** |  | 
**density** | **int** |  | 
**slots** | **int** |  | 
**respect** | **int** |  | 
**coordinates** | [**TornTerritoryCoordinates**](TornTerritoryCoordinates.md) |  | 
**neighbors** | [**List[FactionTerritoryEnum]**](FactionTerritoryEnum.md) |  | 

## Example

```python
from openapi_client.models.torn_territory import TornTerritory

# TODO update the JSON string below
json = "{}"
# create an instance of TornTerritory from a JSON string
torn_territory_instance = TornTerritory.from_json(json)
# print the JSON string representation of the object
print(TornTerritory.to_json())

# convert the object into a dict
torn_territory_dict = torn_territory_instance.to_dict()
# create an instance of TornTerritory from a dict
torn_territory_from_dict = TornTerritory.from_dict(torn_territory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


