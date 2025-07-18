# UserRacesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**races** | [**List[RacingRaceDetails]**](RacingRaceDetails.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.user_races_response import UserRacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserRacesResponse from a JSON string
user_races_response_instance = UserRacesResponse.from_json(json)
# print the JSON string representation of the object
print(UserRacesResponse.to_json())

# convert the object into a dict
user_races_response_dict = user_races_response_instance.to_dict()
# create an instance of UserRacesResponse from a dict
user_races_response_from_dict = UserRacesResponse.from_dict(user_races_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


