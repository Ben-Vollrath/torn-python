# TornFactionTreeBranchUpgradesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**level** | **int** |  | 
**ability** | **str** |  | 
**cost** | **int** |  | 
**challenge** | [**TornFactionTreeBranchUpgradesInnerChallenge**](TornFactionTreeBranchUpgradesInnerChallenge.md) |  | 

## Example

```python
from openapi_client.models.torn_faction_tree_branch_upgrades_inner import TornFactionTreeBranchUpgradesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TornFactionTreeBranchUpgradesInner from a JSON string
torn_faction_tree_branch_upgrades_inner_instance = TornFactionTreeBranchUpgradesInner.from_json(json)
# print the JSON string representation of the object
print(TornFactionTreeBranchUpgradesInner.to_json())

# convert the object into a dict
torn_faction_tree_branch_upgrades_inner_dict = torn_faction_tree_branch_upgrades_inner_instance.to_dict()
# create an instance of TornFactionTreeBranchUpgradesInner from a dict
torn_faction_tree_branch_upgrades_inner_from_dict = TornFactionTreeBranchUpgradesInner.from_dict(torn_faction_tree_branch_upgrades_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


