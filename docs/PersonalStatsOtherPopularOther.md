# PersonalStatsOtherPopularOther


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**PersonalStatsOtherOtherActivity**](PersonalStatsOtherOtherActivity.md) |  | 
**awards** | **int** |  | 
**merits_bought** | **int** |  | 
**refills** | [**PersonalStatsOtherPopularOtherRefills**](PersonalStatsOtherPopularOtherRefills.md) |  | 
**donator_days** | **int** |  | 
**ranked_war_wins** | **int** |  | 

## Example

```python
from openapi_client.models.personal_stats_other_popular_other import PersonalStatsOtherPopularOther

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsOtherPopularOther from a JSON string
personal_stats_other_popular_other_instance = PersonalStatsOtherPopularOther.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsOtherPopularOther.to_json())

# convert the object into a dict
personal_stats_other_popular_other_dict = personal_stats_other_popular_other_instance.to_dict()
# create an instance of PersonalStatsOtherPopularOther from a dict
personal_stats_other_popular_other_from_dict = PersonalStatsOtherPopularOther.from_dict(personal_stats_other_popular_other_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


