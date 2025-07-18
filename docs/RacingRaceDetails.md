# RacingRaceDetails


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
**results** | [**List[RacerDetails]**](RacerDetails.md) |  | 

## Example

```python
from openapi_client.models.racing_race_details import RacingRaceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RacingRaceDetails from a JSON string
racing_race_details_instance = RacingRaceDetails.from_json(json)
# print the JSON string representation of the object
print(RacingRaceDetails.to_json())

# convert the object into a dict
racing_race_details_dict = racing_race_details_instance.to_dict()
# create an instance of RacingRaceDetails from a dict
racing_race_details_from_dict = RacingRaceDetails.from_dict(racing_race_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


