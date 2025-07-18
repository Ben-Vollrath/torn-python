# RacingCarUpgradesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carupgrades** | [**List[RaceCarUpgrade]**](RaceCarUpgrade.md) |  | 

## Example

```python
from openapi_client.models.racing_car_upgrades_response import RacingCarUpgradesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RacingCarUpgradesResponse from a JSON string
racing_car_upgrades_response_instance = RacingCarUpgradesResponse.from_json(json)
# print the JSON string representation of the object
print(RacingCarUpgradesResponse.to_json())

# convert the object into a dict
racing_car_upgrades_response_dict = racing_car_upgrades_response_instance.to_dict()
# create an instance of RacingCarUpgradesResponse from a dict
racing_car_upgrades_response_from_dict = RacingCarUpgradesResponse.from_dict(racing_car_upgrades_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


