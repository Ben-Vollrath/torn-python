# BazaarResponseBazaar

If there's a specific item ID passed or a category chosen, the response will be of type 'BazaarSpecialized', otherwise it will be 'BazaarWeekly'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**busiest** | [**List[BazaarWeeklyCustomers]**](BazaarWeeklyCustomers.md) |  | 
**most_popular** | [**List[BazaarTotalFavorites]**](BazaarTotalFavorites.md) |  | 
**trending** | [**List[BazaarRecentFavorites]**](BazaarRecentFavorites.md) |  | 
**top_grossing** | [**List[BazaarWeeklyIncome]**](BazaarWeeklyIncome.md) |  | 
**bulk** | [**List[BazaarBulkSales]**](BazaarBulkSales.md) |  | 
**advanced_item** | [**List[BazaarAdvancedItemSales]**](BazaarAdvancedItemSales.md) |  | 
**bargain** | [**List[BazaarBargainSales]**](BazaarBargainSales.md) |  | 
**dollar_sale** | [**List[BazaarDollarSales]**](BazaarDollarSales.md) |  | 
**specialized** | [**List[BazaarWeeklyCustomers]**](BazaarWeeklyCustomers.md) |  | 

## Example

```python
from openapi_client.models.bazaar_response_bazaar import BazaarResponseBazaar

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarResponseBazaar from a JSON string
bazaar_response_bazaar_instance = BazaarResponseBazaar.from_json(json)
# print the JSON string representation of the object
print(BazaarResponseBazaar.to_json())

# convert the object into a dict
bazaar_response_bazaar_dict = bazaar_response_bazaar_instance.to_dict()
# create an instance of BazaarResponseBazaar from a dict
bazaar_response_bazaar_from_dict = BazaarResponseBazaar.from_dict(bazaar_response_bazaar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


