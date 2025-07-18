# MarketRentalsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**MarketRentalDetails**](MarketRentalDetails.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.market_rentals_response import MarketRentalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketRentalsResponse from a JSON string
market_rentals_response_instance = MarketRentalsResponse.from_json(json)
# print the JSON string representation of the object
print(MarketRentalsResponse.to_json())

# convert the object into a dict
market_rentals_response_dict = market_rentals_response_instance.to_dict()
# create an instance of MarketRentalsResponse from a dict
market_rentals_response_from_dict = MarketRentalsResponse.from_dict(market_rentals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


