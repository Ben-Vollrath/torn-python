# MarketPropertyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listings** | [**List[MarketPropertyDetailsListingsInner]**](MarketPropertyDetailsListingsInner.md) |  | 
**var_property** | [**BasicProperty**](BasicProperty.md) |  | 

## Example

```python
from openapi_client.models.market_property_details import MarketPropertyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MarketPropertyDetails from a JSON string
market_property_details_instance = MarketPropertyDetails.from_json(json)
# print the JSON string representation of the object
print(MarketPropertyDetails.to_json())

# convert the object into a dict
market_property_details_dict = market_property_details_instance.to_dict()
# create an instance of MarketPropertyDetails from a dict
market_property_details_from_dict = MarketPropertyDetails.from_dict(market_property_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


