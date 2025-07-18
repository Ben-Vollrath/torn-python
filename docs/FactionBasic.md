# FactionBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**tag** | **str** |  | 
**tag_image** | **str** |  | 
**leader_id** | **int** |  | 
**co_leader_id** | **int** |  | 
**respect** | **int** |  | 
**days_old** | **int** |  | 
**capacity** | **int** |  | 
**members** | **int** |  | 
**is_enlisted** | **bool** |  | 
**rank** | [**FactionRank**](FactionRank.md) |  | 
**best_chain** | **int** |  | 

## Example

```python
from openapi_client.models.faction_basic import FactionBasic

# TODO update the JSON string below
json = "{}"
# create an instance of FactionBasic from a JSON string
faction_basic_instance = FactionBasic.from_json(json)
# print the JSON string representation of the object
print(FactionBasic.to_json())

# convert the object into a dict
faction_basic_dict = faction_basic_instance.to_dict()
# create an instance of FactionBasic from a dict
faction_basic_from_dict = FactionBasic.from_dict(faction_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


