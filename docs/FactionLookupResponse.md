# FactionLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selections** | [**List[FactionSelectionName]**](FactionSelectionName.md) |  | 

## Example

```python
from openapi_client.models.faction_lookup_response import FactionLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionLookupResponse from a JSON string
faction_lookup_response_instance = FactionLookupResponse.from_json(json)
# print the JSON string representation of the object
print(FactionLookupResponse.to_json())

# convert the object into a dict
faction_lookup_response_dict = faction_lookup_response_instance.to_dict()
# create an instance of FactionLookupResponse from a dict
faction_lookup_response_from_dict = FactionLookupResponse.from_dict(faction_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


