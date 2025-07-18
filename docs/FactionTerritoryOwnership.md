# FactionTerritoryOwnership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**owned_by** | **int** |  | 
**acquired_at** | **int** |  | 

## Example

```python
from openapi_client.models.faction_territory_ownership import FactionTerritoryOwnership

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryOwnership from a JSON string
faction_territory_ownership_instance = FactionTerritoryOwnership.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryOwnership.to_json())

# convert the object into a dict
faction_territory_ownership_dict = faction_territory_ownership_instance.to_dict()
# create an instance of FactionTerritoryOwnership from a dict
faction_territory_ownership_from_dict = FactionTerritoryOwnership.from_dict(faction_territory_ownership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


