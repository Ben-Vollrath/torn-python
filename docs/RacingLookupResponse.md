# RacingLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selections** | [**List[RacingSelectionName]**](RacingSelectionName.md) |  | 

## Example

```python
from openapi_client.models.racing_lookup_response import RacingLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RacingLookupResponse from a JSON string
racing_lookup_response_instance = RacingLookupResponse.from_json(json)
# print the JSON string representation of the object
print(RacingLookupResponse.to_json())

# convert the object into a dict
racing_lookup_response_dict = racing_lookup_response_instance.to_dict()
# create an instance of RacingLookupResponse from a dict
racing_lookup_response_from_dict = RacingLookupResponse.from_dict(racing_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


