# UserPersonalStatsHistoric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personalstats** | [**List[PersonalStatsHistoricStat]**](PersonalStatsHistoricStat.md) |  | 

## Example

```python
from openapi_client.models.user_personal_stats_historic import UserPersonalStatsHistoric

# TODO update the JSON string below
json = "{}"
# create an instance of UserPersonalStatsHistoric from a JSON string
user_personal_stats_historic_instance = UserPersonalStatsHistoric.from_json(json)
# print the JSON string representation of the object
print(UserPersonalStatsHistoric.to_json())

# convert the object into a dict
user_personal_stats_historic_dict = user_personal_stats_historic_instance.to_dict()
# create an instance of UserPersonalStatsHistoric from a dict
user_personal_stats_historic_from_dict = UserPersonalStatsHistoric.from_dict(user_personal_stats_historic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


