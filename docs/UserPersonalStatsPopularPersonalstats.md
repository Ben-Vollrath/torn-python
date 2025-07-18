# UserPersonalStatsPopularPersonalstats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacking** | [**PersonalStatsAttackingPopularAttacking**](PersonalStatsAttackingPopularAttacking.md) |  | 
**jobs** | [**PersonalStatsJobsPublicJobs**](PersonalStatsJobsPublicJobs.md) |  | 
**hospital** | [**PersonalStatsHospitalPopularHospital**](PersonalStatsHospitalPopularHospital.md) |  | 
**crimes** | [**PersonalStatsCrimesPopularCrimes**](PersonalStatsCrimesPopularCrimes.md) |  | 
**items** | [**PersonalStatsItemsPopularItems**](PersonalStatsItemsPopularItems.md) |  | 
**travel** | [**PersonalStatsTravelPopularTravel**](PersonalStatsTravelPopularTravel.md) |  | 
**drugs** | [**PersonalStatsDrugsDrugs**](PersonalStatsDrugsDrugs.md) |  | 
**networth** | [**PersonalStatsNetworthPublicNetworth**](PersonalStatsNetworthPublicNetworth.md) |  | 
**other** | [**PersonalStatsOtherPopularOther**](PersonalStatsOtherPopularOther.md) |  | 

## Example

```python
from openapi_client.models.user_personal_stats_popular_personalstats import UserPersonalStatsPopularPersonalstats

# TODO update the JSON string below
json = "{}"
# create an instance of UserPersonalStatsPopularPersonalstats from a JSON string
user_personal_stats_popular_personalstats_instance = UserPersonalStatsPopularPersonalstats.from_json(json)
# print the JSON string representation of the object
print(UserPersonalStatsPopularPersonalstats.to_json())

# convert the object into a dict
user_personal_stats_popular_personalstats_dict = user_personal_stats_popular_personalstats_instance.to_dict()
# create an instance of UserPersonalStatsPopularPersonalstats from a dict
user_personal_stats_popular_personalstats_from_dict = UserPersonalStatsPopularPersonalstats.from_dict(user_personal_stats_popular_personalstats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


