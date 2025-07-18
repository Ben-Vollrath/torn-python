# PersonalStatsTradingTradingItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bought** | [**PersonalStatsTradingTradingItemsBought**](PersonalStatsTradingTradingItemsBought.md) |  | 
**auctions** | [**PersonalStatsTradingTradingItemsAuctions**](PersonalStatsTradingTradingItemsAuctions.md) |  | 
**sent** | **int** |  | 

## Example

```python
from openapi_client.models.personal_stats_trading_trading_items import PersonalStatsTradingTradingItems

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsTradingTradingItems from a JSON string
personal_stats_trading_trading_items_instance = PersonalStatsTradingTradingItems.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsTradingTradingItems.to_json())

# convert the object into a dict
personal_stats_trading_trading_items_dict = personal_stats_trading_trading_items_instance.to_dict()
# create an instance of PersonalStatsTradingTradingItems from a dict
personal_stats_trading_trading_items_from_dict = PersonalStatsTradingTradingItems.from_dict(personal_stats_trading_trading_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


