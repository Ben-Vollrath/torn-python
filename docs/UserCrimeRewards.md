# UserCrimeRewards


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money** | **int** |  | 
**ammo** | [**UserCrimeRewardAmmo**](UserCrimeRewardAmmo.md) |  | 
**items** | [**List[UserCrimeRewardItem]**](UserCrimeRewardItem.md) |  | 

## Example

```python
from openapi_client.models.user_crime_rewards import UserCrimeRewards

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeRewards from a JSON string
user_crime_rewards_instance = UserCrimeRewards.from_json(json)
# print the JSON string representation of the object
print(UserCrimeRewards.to_json())

# convert the object into a dict
user_crime_rewards_dict = user_crime_rewards_instance.to_dict()
# create an instance of UserCrimeRewards from a dict
user_crime_rewards_from_dict = UserCrimeRewards.from_dict(user_crime_rewards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


