# TornEducationCourses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**duration** | **int** |  | 
**rewards** | [**TornEducationRewards**](TornEducationRewards.md) |  | 
**prerequisites** | [**TornEducationPrerequisites**](TornEducationPrerequisites.md) |  | 

## Example

```python
from openapi_client.models.torn_education_courses import TornEducationCourses

# TODO update the JSON string below
json = "{}"
# create an instance of TornEducationCourses from a JSON string
torn_education_courses_instance = TornEducationCourses.from_json(json)
# print the JSON string representation of the object
print(TornEducationCourses.to_json())

# convert the object into a dict
torn_education_courses_dict = torn_education_courses_instance.to_dict()
# create an instance of TornEducationCourses from a dict
torn_education_courses_from_dict = TornEducationCourses.from_dict(torn_education_courses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


