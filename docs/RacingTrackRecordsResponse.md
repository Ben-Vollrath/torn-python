# RacingTrackRecordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[RaceRecord]**](RaceRecord.md) |  | 

## Example

```python
from openapi_client.models.racing_track_records_response import RacingTrackRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RacingTrackRecordsResponse from a JSON string
racing_track_records_response_instance = RacingTrackRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(RacingTrackRecordsResponse.to_json())

# convert the object into a dict
racing_track_records_response_dict = racing_track_records_response_instance.to_dict()
# create an instance of RacingTrackRecordsResponse from a dict
racing_track_records_response_from_dict = RacingTrackRecordsResponse.from_dict(racing_track_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


