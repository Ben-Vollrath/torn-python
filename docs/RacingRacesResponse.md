# RacingRacesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**races** | [**List[Race]**](Race.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.racing_races_response import RacingRacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RacingRacesResponse from a JSON string
racing_races_response_instance = RacingRacesResponse.from_json(json)
# print the JSON string representation of the object
print(RacingRacesResponse.to_json())

# convert the object into a dict
racing_races_response_dict = racing_races_response_instance.to_dict()
# create an instance of RacingRacesResponse from a dict
racing_races_response_from_dict = RacingRacesResponse.from_dict(racing_races_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


