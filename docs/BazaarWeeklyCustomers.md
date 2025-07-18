# BazaarWeeklyCustomers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_open** | **bool** |  | 
**weekly_customers** | **int** |  | 

## Example

```python
from openapi_client.models.bazaar_weekly_customers import BazaarWeeklyCustomers

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarWeeklyCustomers from a JSON string
bazaar_weekly_customers_instance = BazaarWeeklyCustomers.from_json(json)
# print the JSON string representation of the object
print(BazaarWeeklyCustomers.to_json())

# convert the object into a dict
bazaar_weekly_customers_dict = bazaar_weekly_customers_instance.to_dict()
# create an instance of BazaarWeeklyCustomers from a dict
bazaar_weekly_customers_from_dict = BazaarWeeklyCustomers.from_dict(bazaar_weekly_customers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


