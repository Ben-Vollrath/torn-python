# TornHofBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**username** | **str** |  | 
**faction_id** | **int** |  | 
**level** | **int** |  | 
**last_action** | **int** |  | 
**rank_name** | **str** |  | 
**rank_number** | **int** |  | 
**position** | **int** |  | 
**signed_up** | **int** |  | 
**age_in_days** | **int** |  | 
**value** | [**TornHofBasicValue**](TornHofBasicValue.md) |  | 
**rank** | **str** |  | 

## Example

```python
from openapi_client.models.torn_hof_basic import TornHofBasic

# TODO update the JSON string below
json = "{}"
# create an instance of TornHofBasic from a JSON string
torn_hof_basic_instance = TornHofBasic.from_json(json)
# print the JSON string representation of the object
print(TornHofBasic.to_json())

# convert the object into a dict
torn_hof_basic_dict = torn_hof_basic_instance.to_dict()
# create an instance of TornHofBasic from a dict
torn_hof_basic_from_dict = TornHofBasic.from_dict(torn_hof_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


