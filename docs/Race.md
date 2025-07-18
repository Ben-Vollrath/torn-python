# Race


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**track_id** | **int** |  | 
**creator_id** | **int** |  | 
**status** | [**RaceStatusEnum**](RaceStatusEnum.md) |  | 
**laps** | **int** |  | 
**participants** | [**RaceParticipants**](RaceParticipants.md) |  | 
**schedule** | [**RaceSchedule**](RaceSchedule.md) |  | 
**requirements** | [**RaceRequirements**](RaceRequirements.md) |  | 
**is_official** | **bool** |  | 

## Example

```python
from openapi_client.models.race import Race

# TODO update the JSON string below
json = "{}"
# create an instance of Race from a JSON string
race_instance = Race.from_json(json)
# print the JSON string representation of the object
print(Race.to_json())

# convert the object into a dict
race_dict = race_instance.to_dict()
# create an instance of Race from a dict
race_from_dict = Race.from_dict(race_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


