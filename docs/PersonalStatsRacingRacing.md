# PersonalStatsRacingRacing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill** | **int** |  | 
**points** | **int** |  | 
**races** | [**PersonalStatsRacingRacingRaces**](PersonalStatsRacingRacingRaces.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_racing_racing import PersonalStatsRacingRacing

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsRacingRacing from a JSON string
personal_stats_racing_racing_instance = PersonalStatsRacingRacing.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsRacingRacing.to_json())

# convert the object into a dict
personal_stats_racing_racing_dict = personal_stats_racing_racing_instance.to_dict()
# create an instance of PersonalStatsRacingRacing from a dict
personal_stats_racing_racing_from_dict = PersonalStatsRacingRacing.from_dict(personal_stats_racing_racing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


