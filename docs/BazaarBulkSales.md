# BazaarBulkSales


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_open** | **bool** |  | 
**bulk_sales** | **int** |  | 

## Example

```python
from openapi_client.models.bazaar_bulk_sales import BazaarBulkSales

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarBulkSales from a JSON string
bazaar_bulk_sales_instance = BazaarBulkSales.from_json(json)
# print the JSON string representation of the object
print(BazaarBulkSales.to_json())

# convert the object into a dict
bazaar_bulk_sales_dict = bazaar_bulk_sales_instance.to_dict()
# create an instance of BazaarBulkSales from a dict
bazaar_bulk_sales_from_dict = BazaarBulkSales.from_dict(bazaar_bulk_sales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


