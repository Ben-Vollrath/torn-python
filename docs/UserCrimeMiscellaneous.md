# UserCrimeMiscellaneous

 Miscellaneous stats for specific crime. Results differ based on the cat id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online_store** | [**UserCrimeDetailsBootleggingOnlineStore**](UserCrimeDetailsBootleggingOnlineStore.md) |  | 
**dvd_sales** | [**UserCrimeDetailsBootleggingDvdSales**](UserCrimeDetailsBootleggingDvdSales.md) |  | 
**dvds_copied** | **int** |  | [optional] 
**cans_used** | **int** |  | 
**most_graffiti_in_one_area** | **int** |  | 
**most_graffiti_simultaneously** | **int** |  | 
**graffiti_removed** | **int** |  | 
**cost_to_city** | **int** |  | 
**average_notoriety** | **int** |  | 
**card_details** | [**UserCrimeDetailsCardSkimmingCardDetails**](UserCrimeDetailsCardSkimmingCardDetails.md) |  | 
**skimmers** | [**UserCrimeDetailsCardSkimmingSkimmers**](UserCrimeDetailsCardSkimmingSkimmers.md) |  | 
**total_audience_gathered** | **int** |  | 
**biggest_money_won** | **int** |  | 
**shill_money_collected** | **int** |  | 
**pickpocket_money_collected** | **int** |  | 
**brute_force_cycles** | **int** |  | 
**encryption_layers_broken** | **int** |  | 
**highest_mips** | **int** |  | 
**chars_guessed** | **int** |  | 
**chars_guessed_total** | **int** |  | 
**most_responses** | **int** |  | [default to 0]
**zones** | [**UserCrimeDetailsScammingZones**](UserCrimeDetailsScammingZones.md) |  | 
**concerns** | [**UserCrimeDetailsScammingConcerns**](UserCrimeDetailsScammingConcerns.md) |  | 
**payouts** | [**UserCrimeDetailsScammingPayouts**](UserCrimeDetailsScammingPayouts.md) |  | 
**emails** | [**UserCrimeDetailsScammingEmails**](UserCrimeDetailsScammingEmails.md) |  | 

## Example

```python
from openapi_client.models.user_crime_miscellaneous import UserCrimeMiscellaneous

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeMiscellaneous from a JSON string
user_crime_miscellaneous_instance = UserCrimeMiscellaneous.from_json(json)
# print the JSON string representation of the object
print(UserCrimeMiscellaneous.to_json())

# convert the object into a dict
user_crime_miscellaneous_dict = user_crime_miscellaneous_instance.to_dict()
# create an instance of UserCrimeMiscellaneous from a dict
user_crime_miscellaneous_from_dict = UserCrimeMiscellaneous.from_dict(user_crime_miscellaneous_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


