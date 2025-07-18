# FactionAttacksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacks** | [**List[Attack]**](Attack.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.faction_attacks_response import FactionAttacksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionAttacksResponse from a JSON string
faction_attacks_response_instance = FactionAttacksResponse.from_json(json)
# print the JSON string representation of the object
print(FactionAttacksResponse.to_json())

# convert the object into a dict
faction_attacks_response_dict = faction_attacks_response_instance.to_dict()
# create an instance of FactionAttacksResponse from a dict
faction_attacks_response_from_dict = FactionAttacksResponse.from_dict(faction_attacks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


