# RacingTracksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracks** | [**List[RaceTrack]**](RaceTrack.md) |  | 

## Example

```python
from openapi_client.models.racing_tracks_response import RacingTracksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RacingTracksResponse from a JSON string
racing_tracks_response_instance = RacingTracksResponse.from_json(json)
# print the JSON string representation of the object
print(RacingTracksResponse.to_json())

# convert the object into a dict
racing_tracks_response_dict = racing_tracks_response_instance.to_dict()
# create an instance of RacingTracksResponse from a dict
racing_tracks_response_from_dict = RacingTracksResponse.from_dict(racing_tracks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


