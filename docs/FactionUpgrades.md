# FactionUpgrades


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core** | [**FactionUpgradesCore**](FactionUpgradesCore.md) |  | 
**peace** | [**List[FactionBranchDetails]**](FactionBranchDetails.md) |  | 
**war** | [**List[FactionBranchDetails]**](FactionBranchDetails.md) |  | 

## Example

```python
from openapi_client.models.faction_upgrades import FactionUpgrades

# TODO update the JSON string below
json = "{}"
# create an instance of FactionUpgrades from a JSON string
faction_upgrades_instance = FactionUpgrades.from_json(json)
# print the JSON string representation of the object
print(FactionUpgrades.to_json())

# convert the object into a dict
faction_upgrades_dict = faction_upgrades_instance.to_dict()
# create an instance of FactionUpgrades from a dict
faction_upgrades_from_dict = FactionUpgrades.from_dict(faction_upgrades_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


