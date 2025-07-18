# UserHofStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacks** | [**HofValue**](HofValue.md) |  | 
**busts** | [**HofValue**](HofValue.md) |  | 
**defends** | [**HofValue**](HofValue.md) |  | 
**networth** | [**HofValue**](HofValue.md) |  | 
**offences** | [**HofValue**](HofValue.md) |  | 
**revives** | [**HofValue**](HofValue.md) |  | 
**level** | [**HofValue**](HofValue.md) |  | 
**rank** | [**HofValue**](HofValue.md) |  | 
**awards** | [**HofValue**](HofValue.md) |  | 
**racing_skill** | [**HofValueFloat**](HofValueFloat.md) |  | 
**racing_points** | [**HofValue**](HofValue.md) |  | 
**racing_wins** | [**HofValue**](HofValue.md) |  | 
**travel_time** | [**HofValue**](HofValue.md) |  | 
**working_stats** | [**HofValue**](HofValue.md) |  | 
**battle_stats** | [**HofValue**](HofValue.md) | This field is null when requesting data for other players. | 

## Example

```python
from openapi_client.models.user_hof_stats import UserHofStats

# TODO update the JSON string below
json = "{}"
# create an instance of UserHofStats from a JSON string
user_hof_stats_instance = UserHofStats.from_json(json)
# print the JSON string representation of the object
print(UserHofStats.to_json())

# convert the object into a dict
user_hof_stats_dict = user_hof_stats_instance.to_dict()
# create an instance of UserHofStats from a dict
user_hof_stats_from_dict = UserHofStats.from_dict(user_hof_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


