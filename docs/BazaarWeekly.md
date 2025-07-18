# BazaarWeekly


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

## Example

```python
from openapi_client.models.bazaar_weekly import BazaarWeekly

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarWeekly from a JSON string
bazaar_weekly_instance = BazaarWeekly.from_json(json)
# print the JSON string representation of the object
print(BazaarWeekly.to_json())

# convert the object into a dict
bazaar_weekly_dict = bazaar_weekly_instance.to_dict()
# create an instance of BazaarWeekly from a dict
bazaar_weekly_from_dict = BazaarWeekly.from_dict(bazaar_weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


