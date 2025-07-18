# TornItemAmmo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**price** | **int** |  | 
**types** | [**List[TornItemAmmoTypeEnum]**](TornItemAmmoTypeEnum.md) | Types of ammo | 

## Example

```python
from openapi_client.models.torn_item_ammo import TornItemAmmo

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemAmmo from a JSON string
torn_item_ammo_instance = TornItemAmmo.from_json(json)
# print the JSON string representation of the object
print(TornItemAmmo.to_json())

# convert the object into a dict
torn_item_ammo_dict = torn_item_ammo_instance.to_dict()
# create an instance of TornItemAmmo from a dict
torn_item_ammo_from_dict = TornItemAmmo.from_dict(torn_item_ammo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


