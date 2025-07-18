# MarketLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selections** | [**List[MarketSelectionName]**](MarketSelectionName.md) |  | 

## Example

```python
from openapi_client.models.market_lookup_response import MarketLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketLookupResponse from a JSON string
market_lookup_response_instance = MarketLookupResponse.from_json(json)
# print the JSON string representation of the object
print(MarketLookupResponse.to_json())

# convert the object into a dict
market_lookup_response_dict = market_lookup_response_instance.to_dict()
# create an instance of MarketLookupResponse from a dict
market_lookup_response_from_dict = MarketLookupResponse.from_dict(market_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


