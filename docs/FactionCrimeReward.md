# FactionCrimeReward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money** | **int** |  | 
**items** | [**List[FactionCrimeRewardItem]**](FactionCrimeRewardItem.md) |  | 
**respect** | **int** |  | 
**scope** | **int** |  | 
**payout** | [**FactionCrimeRewardPayout**](FactionCrimeRewardPayout.md) |  | 

## Example

```python
from openapi_client.models.faction_crime_reward import FactionCrimeReward

# TODO update the JSON string below
json = "{}"
# create an instance of FactionCrimeReward from a JSON string
faction_crime_reward_instance = FactionCrimeReward.from_json(json)
# print the JSON string representation of the object
print(FactionCrimeReward.to_json())

# convert the object into a dict
faction_crime_reward_dict = faction_crime_reward_instance.to_dict()
# create an instance of FactionCrimeReward from a dict
faction_crime_reward_from_dict = FactionCrimeReward.from_dict(faction_crime_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


