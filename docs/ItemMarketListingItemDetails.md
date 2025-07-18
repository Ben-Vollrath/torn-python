# ItemMarketListingItemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **int** |  | 
**stats** | [**ItemMarketListingItemStats**](ItemMarketListingItemStats.md) |  | 
**bonuses** | [**List[ItemMarketListingItemBonus]**](ItemMarketListingItemBonus.md) |  | 
**rarity** | **str** |  | 

## Example

```python
from openapi_client.models.item_market_listing_item_details import ItemMarketListingItemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMarketListingItemDetails from a JSON string
item_market_listing_item_details_instance = ItemMarketListingItemDetails.from_json(json)
# print the JSON string representation of the object
print(ItemMarketListingItemDetails.to_json())

# convert the object into a dict
item_market_listing_item_details_dict = item_market_listing_item_details_instance.to_dict()
# create an instance of ItemMarketListingItemDetails from a dict
item_market_listing_item_details_from_dict = ItemMarketListingItemDetails.from_dict(item_market_listing_item_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


