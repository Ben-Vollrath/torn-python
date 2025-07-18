# ItemMarketItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**average_price** | **int** |  | 

## Example

```python
from openapi_client.models.item_market_item import ItemMarketItem

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMarketItem from a JSON string
item_market_item_instance = ItemMarketItem.from_json(json)
# print the JSON string representation of the object
print(ItemMarketItem.to_json())

# convert the object into a dict
item_market_item_dict = item_market_item_instance.to_dict()
# create an instance of ItemMarketItem from a dict
item_market_item_from_dict = ItemMarketItem.from_dict(item_market_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


