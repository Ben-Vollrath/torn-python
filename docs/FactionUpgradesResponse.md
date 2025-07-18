# FactionUpgradesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upgrades** | [**FactionUpgrades**](FactionUpgrades.md) |  | 
**state** | [**FactionBranchStateEnum**](FactionBranchStateEnum.md) |  | 

## Example

```python
from openapi_client.models.faction_upgrades_response import FactionUpgradesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionUpgradesResponse from a JSON string
faction_upgrades_response_instance = FactionUpgradesResponse.from_json(json)
# print the JSON string representation of the object
print(FactionUpgradesResponse.to_json())

# convert the object into a dict
faction_upgrades_response_dict = faction_upgrades_response_instance.to_dict()
# create an instance of FactionUpgradesResponse from a dict
faction_upgrades_response_from_dict = FactionUpgradesResponse.from_dict(faction_upgrades_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


