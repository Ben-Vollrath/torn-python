# FactionRaidWar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**war_id** | **int** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**factions** | [**List[FactionRaidWarParticipant]**](FactionRaidWarParticipant.md) | The factions involved in the raid war. | 

## Example

```python
from openapi_client.models.faction_raid_war import FactionRaidWar

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRaidWar from a JSON string
faction_raid_war_instance = FactionRaidWar.from_json(json)
# print the JSON string representation of the object
print(FactionRaidWar.to_json())

# convert the object into a dict
faction_raid_war_dict = faction_raid_war_instance.to_dict()
# create an instance of FactionRaidWar from a dict
faction_raid_war_from_dict = FactionRaidWar.from_dict(faction_raid_war_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


