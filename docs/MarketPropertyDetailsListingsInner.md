# MarketPropertyDetailsListingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**happy** | **int** |  | 
**cost** | **int** |  | 
**market_price** | **int** |  | 
**upkeep** | **int** |  | 
**modifications** | [**List[PropertyModificationEnum]**](PropertyModificationEnum.md) |  | 

## Example

```python
from openapi_client.models.market_property_details_listings_inner import MarketPropertyDetailsListingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarketPropertyDetailsListingsInner from a JSON string
market_property_details_listings_inner_instance = MarketPropertyDetailsListingsInner.from_json(json)
# print the JSON string representation of the object
print(MarketPropertyDetailsListingsInner.to_json())

# convert the object into a dict
market_property_details_listings_inner_dict = market_property_details_listings_inner_instance.to_dict()
# create an instance of MarketPropertyDetailsListingsInner from a dict
market_property_details_listings_inner_from_dict = MarketPropertyDetailsListingsInner.from_dict(market_property_details_listings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


