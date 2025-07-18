# BazaarDollarSales


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_open** | **bool** |  | 
**dollar_sales** | **int** |  | 

## Example

```python
from openapi_client.models.bazaar_dollar_sales import BazaarDollarSales

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarDollarSales from a JSON string
bazaar_dollar_sales_instance = BazaarDollarSales.from_json(json)
# print the JSON string representation of the object
print(BazaarDollarSales.to_json())

# convert the object into a dict
bazaar_dollar_sales_dict = bazaar_dollar_sales_instance.to_dict()
# create an instance of BazaarDollarSales from a dict
bazaar_dollar_sales_from_dict = BazaarDollarSales.from_dict(bazaar_dollar_sales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


