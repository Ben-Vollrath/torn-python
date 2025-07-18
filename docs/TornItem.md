# TornItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**effect** | **str** |  | 
**requirement** | **str** |  | 
**image** | **str** |  | 
**type** | [**TornItemTypeEnum**](TornItemTypeEnum.md) |  | 
**sub_type** | [**TornItemWeaponTypeEnum**](TornItemWeaponTypeEnum.md) |  | 
**is_masked** | **bool** |  | 
**is_tradable** | **bool** |  | 
**is_found_in_city** | **bool** |  | 
**value** | [**TornItemValue**](TornItemValue.md) |  | 
**circulation** | **int** |  | 
**details** | [**TornItemDetails**](TornItemDetails.md) |  | 

## Example

```python
from openapi_client.models.torn_item import TornItem

# TODO update the JSON string below
json = "{}"
# create an instance of TornItem from a JSON string
torn_item_instance = TornItem.from_json(json)
# print the JSON string representation of the object
print(TornItem.to_json())

# convert the object into a dict
torn_item_dict = torn_item_instance.to_dict()
# create an instance of TornItem from a dict
torn_item_from_dict = TornItem.from_dict(torn_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


