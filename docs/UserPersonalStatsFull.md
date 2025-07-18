# UserPersonalStatsFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personalstats** | [**UserPersonalStatsFullPersonalstats**](UserPersonalStatsFullPersonalstats.md) |  | 

## Example

```python
from openapi_client.models.user_personal_stats_full import UserPersonalStatsFull

# TODO update the JSON string below
json = "{}"
# create an instance of UserPersonalStatsFull from a JSON string
user_personal_stats_full_instance = UserPersonalStatsFull.from_json(json)
# print the JSON string representation of the object
print(UserPersonalStatsFull.to_json())

# convert the object into a dict
user_personal_stats_full_dict = user_personal_stats_full_instance.to_dict()
# create an instance of UserPersonalStatsFull from a dict
user_personal_stats_full_from_dict = UserPersonalStatsFull.from_dict(user_personal_stats_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


