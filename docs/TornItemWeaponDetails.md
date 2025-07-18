# TornItemWeaponDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stealth_level** | **float** |  | 
**base_stats** | [**TornItemBaseStats**](TornItemBaseStats.md) |  | 
**category** | [**TornItemWeaponCategoryEnum**](TornItemWeaponCategoryEnum.md) |  | 
**ammo** | [**TornItemWeaponDetailsAmmo**](TornItemWeaponDetailsAmmo.md) |  | 
**mods** | **List[int]** |  | 

## Example

```python
from openapi_client.models.torn_item_weapon_details import TornItemWeaponDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemWeaponDetails from a JSON string
torn_item_weapon_details_instance = TornItemWeaponDetails.from_json(json)
# print the JSON string representation of the object
print(TornItemWeaponDetails.to_json())

# convert the object into a dict
torn_item_weapon_details_dict = torn_item_weapon_details_instance.to_dict()
# create an instance of TornItemWeaponDetails from a dict
torn_item_weapon_details_from_dict = TornItemWeaponDetails.from_dict(torn_item_weapon_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


