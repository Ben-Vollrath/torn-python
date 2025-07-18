# PersonalStatsTradingTrading


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**PersonalStatsTradingTradingItems**](PersonalStatsTradingTradingItems.md) |  | 
**trades** | **int** |  | 
**points** | [**PersonalStatsTradingTradingPoints**](PersonalStatsTradingTradingPoints.md) |  | 
**bazaar** | [**PersonalStatsTradingTradingBazaar**](PersonalStatsTradingTradingBazaar.md) |  | 
**item_market** | [**PersonalStatsTradingTradingItemMarket**](PersonalStatsTradingTradingItemMarket.md) |  | [optional] 

## Example

```python
from openapi_client.models.personal_stats_trading_trading import PersonalStatsTradingTrading

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsTradingTrading from a JSON string
personal_stats_trading_trading_instance = PersonalStatsTradingTrading.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsTradingTrading.to_json())

# convert the object into a dict
personal_stats_trading_trading_dict = personal_stats_trading_trading_instance.to_dict()
# create an instance of PersonalStatsTradingTrading from a dict
personal_stats_trading_trading_from_dict = PersonalStatsTradingTrading.from_dict(personal_stats_trading_trading_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


