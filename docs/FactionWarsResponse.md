# FactionWarsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pacts** | [**List[FactionPact]**](FactionPact.md) |  | 
**wars** | [**FactionWars**](FactionWars.md) |  | 

## Example

```python
from openapi_client.models.faction_wars_response import FactionWarsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionWarsResponse from a JSON string
faction_wars_response_instance = FactionWarsResponse.from_json(json)
# print the JSON string representation of the object
print(FactionWarsResponse.to_json())

# convert the object into a dict
faction_wars_response_dict = faction_wars_response_instance.to_dict()
# create an instance of FactionWarsResponse from a dict
faction_wars_response_from_dict = FactionWarsResponse.from_dict(faction_wars_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


