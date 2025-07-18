# UserEducationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**education** | [**UserEducation**](UserEducation.md) |  | 

## Example

```python
from openapi_client.models.user_education_response import UserEducationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserEducationResponse from a JSON string
user_education_response_instance = UserEducationResponse.from_json(json)
# print the JSON string representation of the object
print(UserEducationResponse.to_json())

# convert the object into a dict
user_education_response_dict = user_education_response_instance.to_dict()
# create an instance of UserEducationResponse from a dict
user_education_response_from_dict = UserEducationResponse.from_dict(user_education_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


