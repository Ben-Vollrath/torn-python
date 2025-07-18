# BazaarWeeklyIncome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_open** | **bool** |  | 
**weekly_income** | **int** |  | 

## Example

```python
from openapi_client.models.bazaar_weekly_income import BazaarWeeklyIncome

# TODO update the JSON string below
json = "{}"
# create an instance of BazaarWeeklyIncome from a JSON string
bazaar_weekly_income_instance = BazaarWeeklyIncome.from_json(json)
# print the JSON string representation of the object
print(BazaarWeeklyIncome.to_json())

# convert the object into a dict
bazaar_weekly_income_dict = bazaar_weekly_income_instance.to_dict()
# create an instance of BazaarWeeklyIncome from a dict
bazaar_weekly_income_from_dict = BazaarWeeklyIncome.from_dict(bazaar_weekly_income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


