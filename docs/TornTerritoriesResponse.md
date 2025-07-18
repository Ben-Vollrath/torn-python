# TornTerritoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**territory** | [**List[TornTerritory]**](TornTerritory.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.torn_territories_response import TornTerritoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornTerritoriesResponse from a JSON string
torn_territories_response_instance = TornTerritoriesResponse.from_json(json)
# print the JSON string representation of the object
print(TornTerritoriesResponse.to_json())

# convert the object into a dict
torn_territories_response_dict = torn_territories_response_instance.to_dict()
# create an instance of TornTerritoriesResponse from a dict
torn_territories_response_from_dict = TornTerritoriesResponse.from_dict(torn_territories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


