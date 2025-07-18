# TornFactionTree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**branches** | [**List[TornFactionTreeBranch]**](TornFactionTreeBranch.md) |  | 

## Example

```python
from openapi_client.models.torn_faction_tree import TornFactionTree

# TODO update the JSON string below
json = "{}"
# create an instance of TornFactionTree from a JSON string
torn_faction_tree_instance = TornFactionTree.from_json(json)
# print the JSON string representation of the object
print(TornFactionTree.to_json())

# convert the object into a dict
torn_faction_tree_dict = torn_faction_tree_instance.to_dict()
# create an instance of TornFactionTree from a dict
torn_faction_tree_from_dict = TornFactionTree.from_dict(torn_faction_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


