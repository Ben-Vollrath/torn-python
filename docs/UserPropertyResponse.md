# UserPropertyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**UserPropertyDetails**](UserPropertyDetails.md) |  | 

## Example

```python
from openapi_client.models.user_property_response import UserPropertyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserPropertyResponse from a JSON string
user_property_response_instance = UserPropertyResponse.from_json(json)
# print the JSON string representation of the object
print(UserPropertyResponse.to_json())

# convert the object into a dict
user_property_response_dict = user_property_response_instance.to_dict()
# create an instance of UserPropertyResponse from a dict
user_property_response_from_dict = UserPropertyResponse.from_dict(user_property_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


