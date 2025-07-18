# TornEducationRewards


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**working_stats** | [**TornEducationRewardsWorkingStats**](TornEducationRewardsWorkingStats.md) |  | 
**effect** | **str** |  | 
**honor** | **str** |  | 

## Example

```python
from openapi_client.models.torn_education_rewards import TornEducationRewards

# TODO update the JSON string below
json = "{}"
# create an instance of TornEducationRewards from a JSON string
torn_education_rewards_instance = TornEducationRewards.from_json(json)
# print the JSON string representation of the object
print(TornEducationRewards.to_json())

# convert the object into a dict
torn_education_rewards_dict = torn_education_rewards_instance.to_dict()
# create an instance of TornEducationRewards from a dict
torn_education_rewards_from_dict = TornEducationRewards.from_dict(torn_education_rewards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


