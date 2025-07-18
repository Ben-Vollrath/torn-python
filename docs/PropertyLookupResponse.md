# PropertyLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selections** | [**List[PropertySelectionName]**](PropertySelectionName.md) |  | 

## Example

```python
from openapi_client.models.property_lookup_response import PropertyLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyLookupResponse from a JSON string
property_lookup_response_instance = PropertyLookupResponse.from_json(json)
# print the JSON string representation of the object
print(PropertyLookupResponse.to_json())

# convert the object into a dict
property_lookup_response_dict = property_lookup_response_instance.to_dict()
# create an instance of PropertyLookupResponse from a dict
property_lookup_response_from_dict = PropertyLookupResponse.from_dict(property_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


