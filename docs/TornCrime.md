# TornCrime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**category_id** | **int** |  | 
**category_name** | **str** |  | [optional] 
**enhancer_id** | **int** |  | 
**enhancer_name** | **str** |  | 
**unique_outcomes_count** | **int** |  | 
**unique_outcomes_ids** | **List[int]** |  | 
**notes** | **List[str]** |  | 

## Example

```python
from openapi_client.models.torn_crime import TornCrime

# TODO update the JSON string below
json = "{}"
# create an instance of TornCrime from a JSON string
torn_crime_instance = TornCrime.from_json(json)
# print the JSON string representation of the object
print(TornCrime.to_json())

# convert the object into a dict
torn_crime_dict = torn_crime_instance.to_dict()
# create an instance of TornCrime from a dict
torn_crime_from_dict = TornCrime.from_dict(torn_crime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


