# PersonalStatsCrimesV2Offenses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vandalism** | **int** |  | 
**fraud** | **int** |  | 
**theft** | **int** |  | 
**counterfeiting** | **int** |  | 
**illicit_services** | **int** |  | 
**cybercrime** | **int** |  | 
**extortion** | **int** |  | 
**illegal_production** | **int** |  | 
**organized_crimes** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.personal_stats_crimes_v2_offenses import PersonalStatsCrimesV2Offenses

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsCrimesV2Offenses from a JSON string
personal_stats_crimes_v2_offenses_instance = PersonalStatsCrimesV2Offenses.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsCrimesV2Offenses.to_json())

# convert the object into a dict
personal_stats_crimes_v2_offenses_dict = personal_stats_crimes_v2_offenses_instance.to_dict()
# create an instance of PersonalStatsCrimesV2Offenses from a dict
personal_stats_crimes_v2_offenses_from_dict = PersonalStatsCrimesV2Offenses.from_dict(personal_stats_crimes_v2_offenses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


