# PersonalStatsCrimesCrimes


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
**offenses** | [**PersonalStatsCrimesV2Offenses**](PersonalStatsCrimesV2Offenses.md) |  | 
**skills** | [**PersonalStatsCrimesV2Skills**](PersonalStatsCrimesV2Skills.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_crimes_crimes import PersonalStatsCrimesCrimes

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsCrimesCrimes from a JSON string
personal_stats_crimes_crimes_instance = PersonalStatsCrimesCrimes.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsCrimesCrimes.to_json())

# convert the object into a dict
personal_stats_crimes_crimes_dict = personal_stats_crimes_crimes_instance.to_dict()
# create an instance of PersonalStatsCrimesCrimes from a dict
personal_stats_crimes_crimes_from_dict = PersonalStatsCrimesCrimes.from_dict(personal_stats_crimes_crimes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


