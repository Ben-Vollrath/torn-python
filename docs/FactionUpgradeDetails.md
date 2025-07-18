# FactionUpgradeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**ability** | **str** |  | 
**level** | **int** |  | 
**cost** | **int** |  | 
**unlocked_at** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.faction_upgrade_details import FactionUpgradeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FactionUpgradeDetails from a JSON string
faction_upgrade_details_instance = FactionUpgradeDetails.from_json(json)
# print the JSON string representation of the object
print(FactionUpgradeDetails.to_json())

# convert the object into a dict
faction_upgrade_details_dict = faction_upgrade_details_instance.to_dict()
# create an instance of FactionUpgradeDetails from a dict
faction_upgrade_details_from_dict = FactionUpgradeDetails.from_dict(faction_upgrade_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


