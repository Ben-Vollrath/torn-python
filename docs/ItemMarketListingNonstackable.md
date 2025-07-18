# ItemMarketListingNonstackable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **int** |  | 
**amount** | **int** |  | 
**item_details** | [**ItemMarketListingItemDetails**](ItemMarketListingItemDetails.md) |  | 

## Example

```python
from openapi_client.models.item_market_listing_nonstackable import ItemMarketListingNonstackable

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMarketListingNonstackable from a JSON string
item_market_listing_nonstackable_instance = ItemMarketListingNonstackable.from_json(json)
# print the JSON string representation of the object
print(ItemMarketListingNonstackable.to_json())

# convert the object into a dict
item_market_listing_nonstackable_dict = item_market_listing_nonstackable_instance.to_dict()
# create an instance of ItemMarketListingNonstackable from a dict
item_market_listing_nonstackable_from_dict = ItemMarketListingNonstackable.from_dict(item_market_listing_nonstackable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


