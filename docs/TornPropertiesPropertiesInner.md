# TornPropertiesPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**cost** | **int** |  | 
**happy** | **int** |  | 
**upkeep** | **int** |  | 
**modifications** | [**List[PropertyModificationEnum]**](PropertyModificationEnum.md) |  | 
**staff** | [**List[PropertyStaffEnum]**](PropertyStaffEnum.md) |  | 

## Example

```python
from openapi_client.models.torn_properties_properties_inner import TornPropertiesPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TornPropertiesPropertiesInner from a JSON string
torn_properties_properties_inner_instance = TornPropertiesPropertiesInner.from_json(json)
# print the JSON string representation of the object
print(TornPropertiesPropertiesInner.to_json())

# convert the object into a dict
torn_properties_properties_inner_dict = torn_properties_properties_inner_instance.to_dict()
# create an instance of TornPropertiesPropertiesInner from a dict
torn_properties_properties_inner_from_dict = TornPropertiesPropertiesInner.from_dict(torn_properties_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


