# UserPropertiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**List[UserPropertiesResponsePropertiesInner]**](UserPropertiesResponsePropertiesInner.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.user_properties_response import UserPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserPropertiesResponse from a JSON string
user_properties_response_instance = UserPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print(UserPropertiesResponse.to_json())

# convert the object into a dict
user_properties_response_dict = user_properties_response_instance.to_dict()
# create an instance of UserPropertiesResponse from a dict
user_properties_response_from_dict = UserPropertiesResponse.from_dict(user_properties_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


