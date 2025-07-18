# UserLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selections** | [**List[UserSelectionName]**](UserSelectionName.md) |  | 

## Example

```python
from openapi_client.models.user_lookup_response import UserLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserLookupResponse from a JSON string
user_lookup_response_instance = UserLookupResponse.from_json(json)
# print the JSON string representation of the object
print(UserLookupResponse.to_json())

# convert the object into a dict
user_lookup_response_dict = user_lookup_response_instance.to_dict()
# create an instance of UserLookupResponse from a dict
user_lookup_response_from_dict = UserLookupResponse.from_dict(user_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


