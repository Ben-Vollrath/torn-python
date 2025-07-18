# RaceTrack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from openapi_client.models.race_track import RaceTrack

# TODO update the JSON string below
json = "{}"
# create an instance of RaceTrack from a JSON string
race_track_instance = RaceTrack.from_json(json)
# print the JSON string representation of the object
print(RaceTrack.to_json())

# convert the object into a dict
race_track_dict = race_track_instance.to_dict()
# create an instance of RaceTrack from a dict
race_track_from_dict = RaceTrack.from_dict(race_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


