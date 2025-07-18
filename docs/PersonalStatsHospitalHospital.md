# PersonalStatsHospitalHospital


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**times_hospitalized** | **int** |  | 
**medical_items_used** | **int** |  | 
**blood_withdrawn** | **int** |  | 
**reviving** | [**PersonalStatsHospitalHospitalReviving**](PersonalStatsHospitalHospitalReviving.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_hospital_hospital import PersonalStatsHospitalHospital

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsHospitalHospital from a JSON string
personal_stats_hospital_hospital_instance = PersonalStatsHospitalHospital.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsHospitalHospital.to_json())

# convert the object into a dict
personal_stats_hospital_hospital_dict = personal_stats_hospital_hospital_instance.to_dict()
# create an instance of PersonalStatsHospitalHospital from a dict
personal_stats_hospital_hospital_from_dict = PersonalStatsHospitalHospital.from_dict(personal_stats_hospital_hospital_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


