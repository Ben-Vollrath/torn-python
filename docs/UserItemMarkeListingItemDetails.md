# UserItemMarkeListingItemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**rarity** | **str** |  | 
**uid** | **int** |  | 
**stats** | [**ItemMarketListingItemStats**](ItemMarketListingItemStats.md) |  | 
**bonuses** | [**List[ItemMarketListingItemBonus]**](ItemMarketListingItemBonus.md) |  | 

## Example

```python
from openapi_client.models.user_item_marke_listing_item_details import UserItemMarkeListingItemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserItemMarkeListingItemDetails from a JSON string
user_item_marke_listing_item_details_instance = UserItemMarkeListingItemDetails.from_json(json)
# print the JSON string representation of the object
print(UserItemMarkeListingItemDetails.to_json())

# convert the object into a dict
user_item_marke_listing_item_details_dict = user_item_marke_listing_item_details_instance.to_dict()
# create an instance of UserItemMarkeListingItemDetails from a dict
user_item_marke_listing_item_details_from_dict = UserItemMarkeListingItemDetails.from_dict(user_item_marke_listing_item_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


