# RaceCarUpgrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**class_required** | [**RaceClassEnum**](RaceClassEnum.md) |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**category** | [**RaceCarUpgradeCategory**](RaceCarUpgradeCategory.md) |  | 
**subcategory** | [**RaceCarUpgradeSubCategory**](RaceCarUpgradeSubCategory.md) |  | 
**effects** | [**RaceCarUpgradeEffects**](RaceCarUpgradeEffects.md) |  | 
**cost** | [**RaceCarUpgradeCost**](RaceCarUpgradeCost.md) |  | 

## Example

```python
from openapi_client.models.race_car_upgrade import RaceCarUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of RaceCarUpgrade from a JSON string
race_car_upgrade_instance = RaceCarUpgrade.from_json(json)
# print the JSON string representation of the object
print(RaceCarUpgrade.to_json())

# convert the object into a dict
race_car_upgrade_dict = race_car_upgrade_instance.to_dict()
# create an instance of RaceCarUpgrade from a dict
race_car_upgrade_from_dict = RaceCarUpgrade.from_dict(race_car_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


