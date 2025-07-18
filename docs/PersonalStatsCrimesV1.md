# PersonalStatsCrimesV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**sell_illegal_goods** | **int** |  | 
**theft** | **int** |  | 
**auto_theft** | **int** |  | 
**drug_deals** | **int** |  | 
**computer** | **int** |  | 
**fraud** | **int** |  | 
**murder** | **int** |  | 
**other** | **int** |  | 
**organized_crimes** | **int** |  | 
**version** | **str** |  | 

## Example

```python
from openapi_client.models.personal_stats_crimes_v1 import PersonalStatsCrimesV1

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsCrimesV1 from a JSON string
personal_stats_crimes_v1_instance = PersonalStatsCrimesV1.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsCrimesV1.to_json())

# convert the object into a dict
personal_stats_crimes_v1_dict = personal_stats_crimes_v1_instance.to_dict()
# create an instance of PersonalStatsCrimesV1 from a dict
personal_stats_crimes_v1_from_dict = PersonalStatsCrimesV1.from_dict(personal_stats_crimes_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


