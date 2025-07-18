# PersonalStatsCrimesV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offenses** | [**PersonalStatsCrimesV2Offenses**](PersonalStatsCrimesV2Offenses.md) |  | 
**skills** | [**PersonalStatsCrimesV2Skills**](PersonalStatsCrimesV2Skills.md) |  | 
**version** | **str** |  | 

## Example

```python
from openapi_client.models.personal_stats_crimes_v2 import PersonalStatsCrimesV2

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsCrimesV2 from a JSON string
personal_stats_crimes_v2_instance = PersonalStatsCrimesV2.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsCrimesV2.to_json())

# convert the object into a dict
personal_stats_crimes_v2_dict = personal_stats_crimes_v2_instance.to_dict()
# create an instance of PersonalStatsCrimesV2 from a dict
personal_stats_crimes_v2_from_dict = PersonalStatsCrimesV2.from_dict(personal_stats_crimes_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


