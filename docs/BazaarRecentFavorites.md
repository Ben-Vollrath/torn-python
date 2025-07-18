# BazaarRecentFavorites


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_open** | **bool** |  | 
**recent_favorites** | **int** |  | 

## Example

```python
from openapi_client.models.bazaar_recent_favorites import BazaarRecentFavorites

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarRecentFavorites from a JSON string
bazaar_recent_favorites_instance = BazaarRecentFavorites.from_json(json)
# print the JSON string representation of the object
print(BazaarRecentFavorites.to_json())

# convert the object into a dict
bazaar_recent_favorites_dict = bazaar_recent_favorites_instance.to_dict()
# create an instance of BazaarRecentFavorites from a dict
bazaar_recent_favorites_from_dict = BazaarRecentFavorites.from_dict(bazaar_recent_favorites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


