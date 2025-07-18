# FactionBalanceMembersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**username** | **str** |  | 
**money** | **int** |  | 
**points** | **int** |  | 

## Example

```python
from openapi_client.models.faction_balance_members_inner import FactionBalanceMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of FactionBalanceMembersInner from a JSON string
faction_balance_members_inner_instance = FactionBalanceMembersInner.from_json(json)
# print the JSON string representation of the object
print(FactionBalanceMembersInner.to_json())

# convert the object into a dict
faction_balance_members_inner_dict = faction_balance_members_inner_instance.to_dict()
# create an instance of FactionBalanceMembersInner from a dict
faction_balance_members_inner_from_dict = FactionBalanceMembersInner.from_dict(faction_balance_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


