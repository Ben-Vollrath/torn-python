# Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**races** | [**List[Race]**](Race.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 
**records** | [**List[RaceRecord]**](RaceRecord.md) |  | 
**race** | [**RacingRaceDetails**](RacingRaceDetails.md) |  | 
**cars** | [**List[RaceCar]**](RaceCar.md) |  | 
**tracks** | [**List[RaceTrack]**](RaceTrack.md) |  | 
**carupgrades** | [**List[RaceCarUpgrade]**](RaceCarUpgrade.md) |  | 
**selections** | [**List[RacingSelectionName]**](RacingSelectionName.md) |  | 
**timestamp** | **int** |  | 

## Example

```python
from openapi_client.models.model39b8ce36e3fffc9e2aa1d0aed9ebccda200_response import Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response from a JSON string
model39b8ce36e3fffc9e2aa1d0aed9ebccda200_response_instance = Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response.from_json(json)
# print the JSON string representation of the object
print(Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response.to_json())

# convert the object into a dict
model39b8ce36e3fffc9e2aa1d0aed9ebccda200_response_dict = model39b8ce36e3fffc9e2aa1d0aed9ebccda200_response_instance.to_dict()
# create an instance of Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response from a dict
model39b8ce36e3fffc9e2aa1d0aed9ebccda200_response_from_dict = Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response.from_dict(model39b8ce36e3fffc9e2aa1d0aed9ebccda200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


