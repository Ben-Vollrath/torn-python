# ItemMarketListingItemBonus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from openapi_client.models.item_market_listing_item_bonus import ItemMarketListingItemBonus

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMarketListingItemBonus from a JSON string
item_market_listing_item_bonus_instance = ItemMarketListingItemBonus.from_json(json)
# print the JSON string representation of the object
print(ItemMarketListingItemBonus.to_json())

# convert the object into a dict
item_market_listing_item_bonus_dict = item_market_listing_item_bonus_instance.to_dict()
# create an instance of ItemMarketListingItemBonus from a dict
item_market_listing_item_bonus_from_dict = ItemMarketListingItemBonus.from_dict(item_market_listing_item_bonus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


