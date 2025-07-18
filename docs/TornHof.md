# TornHof


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
**criminal_offenses** | **int** |  | 

## Example

```python
from openapi_client.models.torn_hof import TornHof

# TODO update the JSON string below
json = "{}"
# create an instance of TornHof from a JSON string
torn_hof_instance = TornHof.from_json(json)
# print the JSON string representation of the object
print(TornHof.to_json())

# convert the object into a dict
torn_hof_dict = torn_hof_instance.to_dict()
# create an instance of TornHof from a dict
torn_hof_from_dict = TornHof.from_dict(torn_hof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


