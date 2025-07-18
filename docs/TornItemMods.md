# TornItemMods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**dual_fit** | **bool** | Whether the upgrade fits on dual weapons. | 
**weapons** | [**List[TornItemWeaponTypeEnum]**](TornItemWeaponTypeEnum.md) | The weapon types this upgrade can be attached to. | 

## Example

```python
from openapi_client.models.torn_item_mods import TornItemMods

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemMods from a JSON string
torn_item_mods_instance = TornItemMods.from_json(json)
# print the JSON string representation of the object
print(TornItemMods.to_json())

# convert the object into a dict
torn_item_mods_dict = torn_item_mods_instance.to_dict()
# create an instance of TornItemMods from a dict
torn_item_mods_from_dict = TornItemMods.from_dict(torn_item_mods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


