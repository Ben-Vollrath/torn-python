# MarketRentalDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listings** | [**List[MarketRentalDetailsListingsInner]**](MarketRentalDetailsListingsInner.md) |  | 
**var_property** | [**BasicProperty**](BasicProperty.md) |  | 

## Example

```python
from openapi_client.models.market_rental_details import MarketRentalDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MarketRentalDetails from a JSON string
market_rental_details_instance = MarketRentalDetails.from_json(json)
# print the JSON string representation of the object
print(MarketRentalDetails.to_json())

# convert the object into a dict
market_rental_details_dict = market_rental_details_instance.to_dict()
# create an instance of MarketRentalDetails from a dict
market_rental_details_from_dict = MarketRentalDetails.from_dict(market_rental_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


