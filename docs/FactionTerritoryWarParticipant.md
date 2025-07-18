# FactionTerritoryWarParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **int** |  | 
**chain** | **int** | Faction&#39;s current chain. | 
**is_aggressor** | **bool** |  | 
**player_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.faction_territory_war_participant import FactionTerritoryWarParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarParticipant from a JSON string
faction_territory_war_participant_instance = FactionTerritoryWarParticipant.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarParticipant.to_json())

# convert the object into a dict
faction_territory_war_participant_dict = faction_territory_war_participant_instance.to_dict()
# create an instance of FactionTerritoryWarParticipant from a dict
faction_territory_war_participant_from_dict = FactionTerritoryWarParticipant.from_dict(faction_territory_war_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


