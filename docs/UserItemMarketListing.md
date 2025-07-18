# UserItemMarketListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**price** | **int** |  | 
**average_price** | **int** |  | 
**amount** | **int** |  | 
**is_anonymous** | **bool** |  | 
**available** | **int** | Amount remaining in the inventory. | 
**item** | [**UserItemMarkeListingItemDetails**](UserItemMarkeListingItemDetails.md) |  | 

## Example

```python
from openapi_client.models.user_item_market_listing import UserItemMarketListing

# TODO update the JSON string below
json = "{}"
# create an instance of UserItemMarketListing from a JSON string
user_item_market_listing_instance = UserItemMarketListing.from_json(json)
# print the JSON string representation of the object
print(UserItemMarketListing.to_json())

# convert the object into a dict
user_item_market_listing_dict = user_item_market_listing_instance.to_dict()
# create an instance of UserItemMarketListing from a dict
user_item_market_listing_from_dict = UserItemMarketListing.from_dict(user_item_market_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


