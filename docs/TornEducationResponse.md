# TornEducationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**education** | [**List[TornEducation]**](TornEducation.md) |  | 

## Example

```python
from openapi_client.models.torn_education_response import TornEducationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornEducationResponse from a JSON string
torn_education_response_instance = TornEducationResponse.from_json(json)
# print the JSON string representation of the object
print(TornEducationResponse.to_json())

# convert the object into a dict
torn_education_response_dict = torn_education_response_instance.to_dict()
# create an instance of TornEducationResponse from a dict
torn_education_response_from_dict = TornEducationResponse.from_dict(torn_education_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


