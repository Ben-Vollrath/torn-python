# TornEducation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**courses** | [**List[TornEducationCourses]**](TornEducationCourses.md) |  | 

## Example

```python
from openapi_client.models.torn_education import TornEducation

# TODO update the JSON string below
json = "{}"
# create an instance of TornEducation from a JSON string
torn_education_instance = TornEducation.from_json(json)
# print the JSON string representation of the object
print(TornEducation.to_json())

# convert the object into a dict
torn_education_dict = torn_education_instance.to_dict()
# create an instance of TornEducation from a dict
torn_education_from_dict = TornEducation.from_dict(torn_education_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


