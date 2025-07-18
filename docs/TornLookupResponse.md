# TornLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selections** | [**List[TornSelectionName]**](TornSelectionName.md) |  | 

## Example

```python
from openapi_client.models.torn_lookup_response import TornLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornLookupResponse from a JSON string
torn_lookup_response_instance = TornLookupResponse.from_json(json)
# print the JSON string representation of the object
print(TornLookupResponse.to_json())

# convert the object into a dict
torn_lookup_response_dict = torn_lookup_response_instance.to_dict()
# create an instance of TornLookupResponse from a dict
torn_lookup_response_from_dict = TornLookupResponse.from_dict(torn_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


