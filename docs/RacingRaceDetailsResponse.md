# RacingRaceDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**race** | [**RacingRaceDetails**](RacingRaceDetails.md) |  | 

## Example

```python
from openapi_client.models.racing_race_details_response import RacingRaceDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RacingRaceDetailsResponse from a JSON string
racing_race_details_response_instance = RacingRaceDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(RacingRaceDetailsResponse.to_json())

# convert the object into a dict
racing_race_details_response_dict = racing_race_details_response_instance.to_dict()
# create an instance of RacingRaceDetailsResponse from a dict
racing_race_details_response_from_dict = RacingRaceDetailsResponse.from_dict(racing_race_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


