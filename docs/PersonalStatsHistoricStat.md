# PersonalStatsHistoricStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Requested stat name | 
**value** | **int** |  | 
**timestamp** | **int** | Timestamp when the stat was last updated | 

## Example

```python
from openapi_client.models.personal_stats_historic_stat import PersonalStatsHistoricStat

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsHistoricStat from a JSON string
personal_stats_historic_stat_instance = PersonalStatsHistoricStat.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsHistoricStat.to_json())

# convert the object into a dict
personal_stats_historic_stat_dict = personal_stats_historic_stat_instance.to_dict()
# create an instance of PersonalStatsHistoricStat from a dict
personal_stats_historic_stat_from_dict = PersonalStatsHistoricStat.from_dict(personal_stats_historic_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


