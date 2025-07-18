# FactionRaidWarParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **int** |  | 
**chain** | **int** | Faction&#39;s current chain. | 
**is_aggressor** | **bool** |  | 

## Example

```python
from openapi_client.models.faction_raid_war_participant import FactionRaidWarParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRaidWarParticipant from a JSON string
faction_raid_war_participant_instance = FactionRaidWarParticipant.from_json(json)
# print the JSON string representation of the object
print(FactionRaidWarParticipant.to_json())

# convert the object into a dict
faction_raid_war_participant_dict = faction_raid_war_participant_instance.to_dict()
# create an instance of FactionRaidWarParticipant from a dict
faction_raid_war_participant_from_dict = FactionRaidWarParticipant.from_dict(faction_raid_war_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


