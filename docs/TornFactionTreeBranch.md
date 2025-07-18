# TornFactionTreeBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**upgrades** | [**List[TornFactionTreeBranchUpgradesInner]**](TornFactionTreeBranchUpgradesInner.md) |  | 

## Example

```python
from openapi_client.models.torn_faction_tree_branch import TornFactionTreeBranch

# TODO update the JSON string below
json = "{}"
# create an instance of TornFactionTreeBranch from a JSON string
torn_faction_tree_branch_instance = TornFactionTreeBranch.from_json(json)
# print the JSON string representation of the object
print(TornFactionTreeBranch.to_json())

# convert the object into a dict
torn_faction_tree_branch_dict = torn_faction_tree_branch_instance.to_dict()
# create an instance of TornFactionTreeBranch from a dict
torn_faction_tree_branch_from_dict = TornFactionTreeBranch.from_dict(torn_faction_tree_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


