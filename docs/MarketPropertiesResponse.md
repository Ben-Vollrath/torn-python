# MarketPropertiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**MarketPropertyDetails**](MarketPropertyDetails.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.market_properties_response import MarketPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketPropertiesResponse from a JSON string
market_properties_response_instance = MarketPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print(MarketPropertiesResponse.to_json())

# convert the object into a dict
market_properties_response_dict = market_properties_response_instance.to_dict()
# create an instance of MarketPropertiesResponse from a dict
market_properties_response_from_dict = MarketPropertiesResponse.from_dict(market_properties_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


