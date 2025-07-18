# BazaarAdvancedItemSales


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_open** | **bool** |  | 
**advanced_item_sales** | **int** |  | 

## Example

```python
from openapi_client.models.bazaar_advanced_item_sales import BazaarAdvancedItemSales

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarAdvancedItemSales from a JSON string
bazaar_advanced_item_sales_instance = BazaarAdvancedItemSales.from_json(json)
# print the JSON string representation of the object
print(BazaarAdvancedItemSales.to_json())

# convert the object into a dict
bazaar_advanced_item_sales_dict = bazaar_advanced_item_sales_instance.to_dict()
# create an instance of BazaarAdvancedItemSales from a dict
bazaar_advanced_item_sales_from_dict = BazaarAdvancedItemSales.from_dict(bazaar_advanced_item_sales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


