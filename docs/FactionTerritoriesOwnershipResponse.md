# FactionTerritoriesOwnershipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**territory_ownership** | [**List[FactionTerritoryOwnership]**](FactionTerritoryOwnership.md) |  | 

## Example

```python
from openapi_client.models.faction_territories_ownership_response import FactionTerritoriesOwnershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoriesOwnershipResponse from a JSON string
faction_territories_ownership_response_instance = FactionTerritoriesOwnershipResponse.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoriesOwnershipResponse.to_json())

# convert the object into a dict
faction_territories_ownership_response_dict = faction_territories_ownership_response_instance.to_dict()
# create an instance of FactionTerritoriesOwnershipResponse from a dict
faction_territories_ownership_response_from_dict = FactionTerritoriesOwnershipResponse.from_dict(faction_territories_ownership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


