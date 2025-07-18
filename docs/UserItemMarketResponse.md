# UserItemMarketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itemmarket** | [**List[UserItemMarketListing]**](UserItemMarketListing.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.user_item_market_response import UserItemMarketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserItemMarketResponse from a JSON string
user_item_market_response_instance = UserItemMarketResponse.from_json(json)
# print the JSON string representation of the object
print(UserItemMarketResponse.to_json())

# convert the object into a dict
user_item_market_response_dict = user_item_market_response_instance.to_dict()
# create an instance of UserItemMarketResponse from a dict
user_item_market_response_from_dict = UserItemMarketResponse.from_dict(user_item_market_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


