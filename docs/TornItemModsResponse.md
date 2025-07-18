# TornItemModsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itemmods** | [**List[TornItemMods]**](TornItemMods.md) |  | 

## Example

```python
from openapi_client.models.torn_item_mods_response import TornItemModsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemModsResponse from a JSON string
torn_item_mods_response_instance = TornItemModsResponse.from_json(json)
# print the JSON string representation of the object
print(TornItemModsResponse.to_json())

# convert the object into a dict
torn_item_mods_response_dict = torn_item_mods_response_instance.to_dict()
# create an instance of TornItemModsResponse from a dict
torn_item_mods_response_from_dict = TornItemModsResponse.from_dict(torn_item_mods_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


