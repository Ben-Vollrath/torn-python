# UserEducation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **List[int]** |  | 
**current** | [**UserCurrentEducation**](UserCurrentEducation.md) |  | 

## Example

```python
from openapi_client.models.user_education import UserEducation

# TODO update the JSON string below
json = "{}"
# create an instance of UserEducation from a JSON string
user_education_instance = UserEducation.from_json(json)
# print the JSON string representation of the object
print(UserEducation.to_json())

# convert the object into a dict
user_education_dict = user_education_instance.to_dict()
# create an instance of UserEducation from a dict
user_education_from_dict = UserEducation.from_dict(user_education_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


