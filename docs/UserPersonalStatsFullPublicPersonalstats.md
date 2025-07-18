# UserPersonalStatsFullPublicPersonalstats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacking** | [**PersonalStatsAttackingPublicAttacking**](PersonalStatsAttackingPublicAttacking.md) |  | 
**jobs** | [**PersonalStatsJobsPublicJobs**](PersonalStatsJobsPublicJobs.md) |  | 
**trading** | [**PersonalStatsTradingTrading**](PersonalStatsTradingTrading.md) |  | 
**jail** | [**PersonalStatsJailJail**](PersonalStatsJailJail.md) |  | 
**hospital** | [**PersonalStatsHospitalHospital**](PersonalStatsHospitalHospital.md) |  | 
**finishing_hits** | [**PersonalStatsFinishingHitsFinishingHits**](PersonalStatsFinishingHitsFinishingHits.md) |  | 
**communication** | [**PersonalStatsCommunicationCommunication**](PersonalStatsCommunicationCommunication.md) |  | 
**crimes** | [**PersonalStatsCrimesCrimes**](PersonalStatsCrimesCrimes.md) |  | 
**bounties** | [**PersonalStatsBountiesBounties**](PersonalStatsBountiesBounties.md) |  | 
**items** | [**PersonalStatsItemsItems**](PersonalStatsItemsItems.md) |  | 
**travel** | [**PersonalStatsTravelTravel**](PersonalStatsTravelTravel.md) |  | 
**drugs** | [**PersonalStatsDrugsDrugs**](PersonalStatsDrugsDrugs.md) |  | 
**missions** | [**PersonalStatsMissionsMissions**](PersonalStatsMissionsMissions.md) |  | 
**racing** | [**PersonalStatsRacingRacing**](PersonalStatsRacingRacing.md) |  | 
**networth** | [**PersonalStatsNetworthPublicNetworth**](PersonalStatsNetworthPublicNetworth.md) |  | 
**other** | [**PersonalStatsOtherOther**](PersonalStatsOtherOther.md) |  | 

## Example

```python
from openapi_client.models.user_personal_stats_full_public_personalstats import UserPersonalStatsFullPublicPersonalstats

# TODO update the JSON string below
json = "{}"
# create an instance of UserPersonalStatsFullPublicPersonalstats from a JSON string
user_personal_stats_full_public_personalstats_instance = UserPersonalStatsFullPublicPersonalstats.from_json(json)
# print the JSON string representation of the object
print(UserPersonalStatsFullPublicPersonalstats.to_json())

# convert the object into a dict
user_personal_stats_full_public_personalstats_dict = user_personal_stats_full_public_personalstats_instance.to_dict()
# create an instance of UserPersonalStatsFullPublicPersonalstats from a dict
user_personal_stats_full_public_personalstats_from_dict = UserPersonalStatsFullPublicPersonalstats.from_dict(user_personal_stats_full_public_personalstats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


