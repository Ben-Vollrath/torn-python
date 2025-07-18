# UserPersonalStatsCategory

Schema name corresponds to the requested category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personalstats** | [**UserPersonalStatsCategoryPersonalstats**](UserPersonalStatsCategoryPersonalstats.md) |  | 

## Example

```python
from openapi_client.models.user_personal_stats_category import UserPersonalStatsCategory

# TODO update the JSON string below
json = "{}"
# create an instance of UserPersonalStatsCategory from a JSON string
user_personal_stats_category_instance = UserPersonalStatsCategory.from_json(json)
# print the JSON string representation of the object
print(UserPersonalStatsCategory.to_json())

# convert the object into a dict
user_personal_stats_category_dict = user_personal_stats_category_instance.to_dict()
# create an instance of UserPersonalStatsCategory from a dict
user_personal_stats_category_from_dict = UserPersonalStatsCategory.from_dict(user_personal_stats_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


