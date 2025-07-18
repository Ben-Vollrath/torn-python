# PersonalStatsCrimesV2Skills


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_for_cash** | **int** |  | 
**bootlegging** | **int** |  | 
**graffiti** | **int** |  | 
**shoplifting** | **int** |  | 
**pickpocketing** | **int** |  | 
**card_skimming** | **int** |  | 
**burglary** | **int** |  | 
**hustling** | **int** |  | 
**disposal** | **int** |  | 
**cracking** | **int** |  | 
**forgery** | **int** |  | 
**scamming** | **int** |  | 

## Example

```python
from openapi_client.models.personal_stats_crimes_v2_skills import PersonalStatsCrimesV2Skills

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsCrimesV2Skills from a JSON string
personal_stats_crimes_v2_skills_instance = PersonalStatsCrimesV2Skills.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsCrimesV2Skills.to_json())

# convert the object into a dict
personal_stats_crimes_v2_skills_dict = personal_stats_crimes_v2_skills_instance.to_dict()
# create an instance of PersonalStatsCrimesV2Skills from a dict
personal_stats_crimes_v2_skills_from_dict = PersonalStatsCrimesV2Skills.from_dict(personal_stats_crimes_v2_skills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


