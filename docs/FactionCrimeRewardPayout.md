# FactionCrimeRewardPayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FactionOrganizedCrimePayoutType**](FactionOrganizedCrimePayoutType.md) |  | 
**percentage** | **int** | Total percentage split between all participants. | 
**paid_by** | **int** |  | 
**paid_at** | **int** |  | 

## Example

```python
from openapi_client.models.faction_crime_reward_payout import FactionCrimeRewardPayout

# TODO update the JSON string below
json = "{}"
# create an instance of FactionCrimeRewardPayout from a JSON string
faction_crime_reward_payout_instance = FactionCrimeRewardPayout.from_json(json)
# print the JSON string representation of the object
print(FactionCrimeRewardPayout.to_json())

# convert the object into a dict
faction_crime_reward_payout_dict = faction_crime_reward_payout_instance.to_dict()
# create an instance of FactionCrimeRewardPayout from a dict
faction_crime_reward_payout_from_dict = FactionCrimeRewardPayout.from_dict(faction_crime_reward_payout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


