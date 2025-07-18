# TornItemDetails

If the item 'type' is 'Armor' then TornItemArmorDetails is returned.<br>If the item 'type' is 'Weapon' then TornItemWeaponDetails is returned.<br>Otherwise, null is returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stealth_level** | **float** |  | 
**base_stats** | [**TornItemBaseStats**](TornItemBaseStats.md) |  | 
**category** | [**TornItemWeaponCategoryEnum**](TornItemWeaponCategoryEnum.md) |  | 
**ammo** | [**TornItemWeaponDetailsAmmo**](TornItemWeaponDetailsAmmo.md) |  | 
**mods** | **List[int]** |  | 
**coverage** | [**List[TornItemArmorCoverage]**](TornItemArmorCoverage.md) |  | 

## Example

```python
from openapi_client.models.torn_item_details import TornItemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemDetails from a JSON string
torn_item_details_instance = TornItemDetails.from_json(json)
# print the JSON string representation of the object
print(TornItemDetails.to_json())

# convert the object into a dict
torn_item_details_dict = torn_item_details_instance.to_dict()
# create an instance of TornItemDetails from a dict
torn_item_details_from_dict = TornItemDetails.from_dict(torn_item_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


