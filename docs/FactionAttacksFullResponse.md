# FactionAttacksFullResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacks** | [**List[AttackSimplified]**](AttackSimplified.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.faction_attacks_full_response import FactionAttacksFullResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionAttacksFullResponse from a JSON string
faction_attacks_full_response_instance = FactionAttacksFullResponse.from_json(json)
# print the JSON string representation of the object
print(FactionAttacksFullResponse.to_json())

# convert the object into a dict
faction_attacks_full_response_dict = faction_attacks_full_response_instance.to_dict()
# create an instance of FactionAttacksFullResponse from a dict
faction_attacks_full_response_from_dict = FactionAttacksFullResponse.from_dict(faction_attacks_full_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


