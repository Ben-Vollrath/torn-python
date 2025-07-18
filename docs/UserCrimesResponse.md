# UserCrimesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crimes** | [**UserCrime**](UserCrime.md) |  | 

## Example

```python
from openapi_client.models.user_crimes_response import UserCrimesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimesResponse from a JSON string
user_crimes_response_instance = UserCrimesResponse.from_json(json)
# print the JSON string representation of the object
print(UserCrimesResponse.to_json())

# convert the object into a dict
user_crimes_response_dict = user_crimes_response_instance.to_dict()
# create an instance of UserCrimesResponse from a dict
user_crimes_response_from_dict = UserCrimesResponse.from_dict(user_crimes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


