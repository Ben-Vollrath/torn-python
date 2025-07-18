# TornHofWithOffenses


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
from openapi_client.models.torn_hof_with_offenses import TornHofWithOffenses

# TODO update the JSON string below
json = "{}"
# create an instance of TornHofWithOffenses from a JSON string
torn_hof_with_offenses_instance = TornHofWithOffenses.from_json(json)
# print the JSON string representation of the object
print(TornHofWithOffenses.to_json())

# convert the object into a dict
torn_hof_with_offenses_dict = torn_hof_with_offenses_instance.to_dict()
# create an instance of TornHofWithOffenses from a dict
torn_hof_with_offenses_from_dict = TornHofWithOffenses.from_dict(torn_hof_with_offenses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


