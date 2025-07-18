# TornItemWeaponDetailsAmmo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**magazine_rounds** | **int** |  | 
**rate_of_fire** | [**TornItemWeaponDetailsAmmoRateOfFire**](TornItemWeaponDetailsAmmoRateOfFire.md) |  | 

## Example

```python
from openapi_client.models.torn_item_weapon_details_ammo import TornItemWeaponDetailsAmmo

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemWeaponDetailsAmmo from a JSON string
torn_item_weapon_details_ammo_instance = TornItemWeaponDetailsAmmo.from_json(json)
# print the JSON string representation of the object
print(TornItemWeaponDetailsAmmo.to_json())

# convert the object into a dict
torn_item_weapon_details_ammo_dict = torn_item_weapon_details_ammo_instance.to_dict()
# create an instance of TornItemWeaponDetailsAmmo from a dict
torn_item_weapon_details_ammo_from_dict = TornItemWeaponDetailsAmmo.from_dict(torn_item_weapon_details_ammo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


