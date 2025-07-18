# BazaarTotalFavorites


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_open** | **bool** |  | 
**total_favorites** | **int** |  | 

## Example

```python
from openapi_client.models.bazaar_total_favorites import BazaarTotalFavorites

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarTotalFavorites from a JSON string
bazaar_total_favorites_instance = BazaarTotalFavorites.from_json(json)
# print the JSON string representation of the object
print(BazaarTotalFavorites.to_json())

# convert the object into a dict
bazaar_total_favorites_dict = bazaar_total_favorites_instance.to_dict()
# create an instance of BazaarTotalFavorites from a dict
bazaar_total_favorites_from_dict = BazaarTotalFavorites.from_dict(bazaar_total_favorites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


