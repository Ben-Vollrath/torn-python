# FactionApplicationUserStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strength** | **int** |  | 
**speed** | **int** |  | 
**dexterity** | **int** |  | 
**defense** | **int** |  | 

## Example

```python
from openapi_client.models.faction_application_user_stats import FactionApplicationUserStats

# TODO update the JSON string below
json = "{}"
# create an instance of FactionApplicationUserStats from a JSON string
faction_application_user_stats_instance = FactionApplicationUserStats.from_json(json)
# print the JSON string representation of the object
print(FactionApplicationUserStats.to_json())

# convert the object into a dict
faction_application_user_stats_dict = faction_application_user_stats_instance.to_dict()
# create an instance of FactionApplicationUserStats from a dict
faction_application_user_stats_from_dict = FactionApplicationUserStats.from_dict(faction_application_user_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


