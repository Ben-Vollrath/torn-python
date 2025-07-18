# TornFactionTreeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faction_tree** | [**List[TornFactionTree]**](TornFactionTree.md) |  | 

## Example

```python
from openapi_client.models.torn_faction_tree_response import TornFactionTreeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornFactionTreeResponse from a JSON string
torn_faction_tree_response_instance = TornFactionTreeResponse.from_json(json)
# print the JSON string representation of the object
print(TornFactionTreeResponse.to_json())

# convert the object into a dict
torn_faction_tree_response_dict = torn_faction_tree_response_instance.to_dict()
# create an instance of TornFactionTreeResponse from a dict
torn_faction_tree_response_from_dict = TornFactionTreeResponse.from_dict(torn_faction_tree_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


