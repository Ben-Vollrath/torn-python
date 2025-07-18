# TornFactionHofResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factionhof** | [**List[TornFactionHof]**](TornFactionHof.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.torn_faction_hof_response import TornFactionHofResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornFactionHofResponse from a JSON string
torn_faction_hof_response_instance = TornFactionHofResponse.from_json(json)
# print the JSON string representation of the object
print(TornFactionHofResponse.to_json())

# convert the object into a dict
torn_faction_hof_response_dict = torn_faction_hof_response_instance.to_dict()
# create an instance of TornFactionHofResponse from a dict
torn_faction_hof_response_from_dict = TornFactionHofResponse.from_dict(torn_faction_hof_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


