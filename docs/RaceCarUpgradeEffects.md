# RaceCarUpgradeEffects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_speed** | **int** |  | 
**acceleration** | **int** |  | 
**braking** | **int** |  | 
**handling** | **int** |  | 
**safety** | **int** |  | 
**dirt** | **int** |  | 
**tarmac** | **int** |  | 

## Example

```python
from openapi_client.models.race_car_upgrade_effects import RaceCarUpgradeEffects

# TODO update the JSON string below
json = "{}"
# create an instance of RaceCarUpgradeEffects from a JSON string
race_car_upgrade_effects_instance = RaceCarUpgradeEffects.from_json(json)
# print the JSON string representation of the object
print(RaceCarUpgradeEffects.to_json())

# convert the object into a dict
race_car_upgrade_effects_dict = race_car_upgrade_effects_instance.to_dict()
# create an instance of RaceCarUpgradeEffects from a dict
race_car_upgrade_effects_from_dict = RaceCarUpgradeEffects.from_dict(race_car_upgrade_effects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


