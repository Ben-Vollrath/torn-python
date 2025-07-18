# MarketItemMarketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itemmarket** | [**ItemMarket**](ItemMarket.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.market_item_market_response import MarketItemMarketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketItemMarketResponse from a JSON string
market_item_market_response_instance = MarketItemMarketResponse.from_json(json)
# print the JSON string representation of the object
print(MarketItemMarketResponse.to_json())

# convert the object into a dict
market_item_market_response_dict = market_item_market_response_instance.to_dict()
# create an instance of MarketItemMarketResponse from a dict
market_item_market_response_from_dict = MarketItemMarketResponse.from_dict(market_item_market_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


