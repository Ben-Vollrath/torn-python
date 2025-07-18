# ItemMarketListingItemStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**damage** | **float** |  | 
**accuracy** | **float** |  | 
**armor** | **float** |  | 
**quality** | **float** |  | 

## Example

```python
from openapi_client.models.item_market_listing_item_stats import ItemMarketListingItemStats

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMarketListingItemStats from a JSON string
item_market_listing_item_stats_instance = ItemMarketListingItemStats.from_json(json)
# print the JSON string representation of the object
print(ItemMarketListingItemStats.to_json())

# convert the object into a dict
item_market_listing_item_stats_dict = item_market_listing_item_stats_instance.to_dict()
# create an instance of ItemMarketListingItemStats from a dict
item_market_listing_item_stats_from_dict = ItemMarketListingItemStats.from_dict(item_market_listing_item_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


