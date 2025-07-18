# FactionBranchDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**order** | **int** |  | 
**multiplier** | **int** | Respect cost multiplier. | 
**upgrades** | [**List[FactionUpgradeDetails]**](FactionUpgradeDetails.md) |  | 

## Example

```python
from openapi_client.models.faction_branch_details import FactionBranchDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FactionBranchDetails from a JSON string
faction_branch_details_instance = FactionBranchDetails.from_json(json)
# print the JSON string representation of the object
print(FactionBranchDetails.to_json())

# convert the object into a dict
faction_branch_details_dict = faction_branch_details_instance.to_dict()
# create an instance of FactionBranchDetails from a dict
faction_branch_details_from_dict = FactionBranchDetails.from_dict(faction_branch_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


