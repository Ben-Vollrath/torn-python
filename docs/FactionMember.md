# FactionMember

Details about a faction member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**level** | **int** |  | 
**days_in_faction** | **int** |  | 
**is_revivable** | **bool** |  | 
**is_on_wall** | **bool** | Shows if the member is currently defending territory wall. | 
**is_in_oc** | **bool** | Shows if the member is currently participating in an organized crime. Show false for members of other factions. | 
**has_early_discharge** | **bool** | Shows if the member is eligible for an early discharge from the hospital. | 
**last_action** | [**UserLastAction**](UserLastAction.md) |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**revive_setting** | [**ReviveSetting**](ReviveSetting.md) |  | 

## Example

```python
from openapi_client.models.faction_member import FactionMember

# TODO update the JSON string below
json = "{}"
# create an instance of FactionMember from a JSON string
faction_member_instance = FactionMember.from_json(json)
# print the JSON string representation of the object
print(FactionMember.to_json())

# convert the object into a dict
faction_member_dict = faction_member_instance.to_dict()
# create an instance of FactionMember from a dict
faction_member_from_dict = FactionMember.from_dict(faction_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


