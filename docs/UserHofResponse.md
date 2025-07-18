# UserHofResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hof** | [**UserHofStats**](UserHofStats.md) |  | 

## Example

```python
from openapi_client.models.user_hof_response import UserHofResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserHofResponse from a JSON string
user_hof_response_instance = UserHofResponse.from_json(json)
# print the JSON string representation of the object
print(UserHofResponse.to_json())

# convert the object into a dict
user_hof_response_dict = user_hof_response_instance.to_dict()
# create an instance of UserHofResponse from a dict
user_hof_response_from_dict = UserHofResponse.from_dict(user_hof_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


