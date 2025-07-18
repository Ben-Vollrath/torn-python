# RaceSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**join_from** | **int** |  | 
**join_until** | **int** |  | 
**start** | **int** |  | 
**end** | **int** |  | 

## Example

```python
from openapi_client.models.race_schedule import RaceSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of RaceSchedule from a JSON string
race_schedule_instance = RaceSchedule.from_json(json)
# print the JSON string representation of the object
print(RaceSchedule.to_json())

# convert the object into a dict
race_schedule_dict = race_schedule_instance.to_dict()
# create an instance of RaceSchedule from a dict
race_schedule_from_dict = RaceSchedule.from_dict(race_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


