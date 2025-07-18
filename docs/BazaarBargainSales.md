# BazaarBargainSales


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_open** | **bool** |  | 
**bargain_sales** | **int** |  | 

## Example

```python
from openapi_client.models.bazaar_bargain_sales import BazaarBargainSales

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarBargainSales from a JSON string
bazaar_bargain_sales_instance = BazaarBargainSales.from_json(json)
# print the JSON string representation of the object
print(BazaarBargainSales.to_json())

# convert the object into a dict
bazaar_bargain_sales_dict = bazaar_bargain_sales_instance.to_dict()
# create an instance of BazaarBargainSales from a dict
bazaar_bargain_sales_from_dict = BazaarBargainSales.from_dict(bazaar_bargain_sales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


