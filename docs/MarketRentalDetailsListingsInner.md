# MarketRentalDetailsListingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**happy** | **int** |  | 
**cost** | **int** |  | 
**cost_per_day** | **int** |  | 
**rental_period** | **int** |  | 
**market_price** | **int** |  | 
**upkeep** | **int** |  | 
**modifications** | [**List[PropertyModificationEnum]**](PropertyModificationEnum.md) |  | 

## Example

```python
from openapi_client.models.market_rental_details_listings_inner import MarketRentalDetailsListingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarketRentalDetailsListingsInner from a JSON string
market_rental_details_listings_inner_instance = MarketRentalDetailsListingsInner.from_json(json)
# print the JSON string representation of the object
print(MarketRentalDetailsListingsInner.to_json())

# convert the object into a dict
market_rental_details_listings_inner_dict = market_rental_details_listings_inner_instance.to_dict()
# create an instance of MarketRentalDetailsListingsInner from a dict
market_rental_details_listings_inner_from_dict = MarketRentalDetailsListingsInner.from_dict(market_rental_details_listings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


