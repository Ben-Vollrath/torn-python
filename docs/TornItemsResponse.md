# TornItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TornItem]**](TornItem.md) |  | 

## Example

```python
from openapi_client.models.torn_items_response import TornItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemsResponse from a JSON string
torn_items_response_instance = TornItemsResponse.from_json(json)
# print the JSON string representation of the object
print(TornItemsResponse.to_json())

# convert the object into a dict
torn_items_response_dict = torn_items_response_instance.to_dict()
# create an instance of TornItemsResponse from a dict
torn_items_response_from_dict = TornItemsResponse.from_dict(torn_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


