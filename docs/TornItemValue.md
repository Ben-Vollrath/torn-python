# TornItemValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | [**TornItemValueVendor**](TornItemValueVendor.md) |  | 
**buy_price** | **int** |  | 
**sell_price** | **int** |  | 
**market_price** | **int** |  | 

## Example

```python
from openapi_client.models.torn_item_value import TornItemValue

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemValue from a JSON string
torn_item_value_instance = TornItemValue.from_json(json)
# print the JSON string representation of the object
print(TornItemValue.to_json())

# convert the object into a dict
torn_item_value_dict = torn_item_value_instance.to_dict()
# create an instance of TornItemValue from a dict
torn_item_value_from_dict = TornItemValue.from_dict(torn_item_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


