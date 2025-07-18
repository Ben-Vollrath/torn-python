# FactionRankedWarParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **int** |  | 
**chain** | **int** | Faction&#39;s current chain. | 

## Example

```python
from openapi_client.models.faction_ranked_war_participant import FactionRankedWarParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRankedWarParticipant from a JSON string
faction_ranked_war_participant_instance = FactionRankedWarParticipant.from_json(json)
# print the JSON string representation of the object
print(FactionRankedWarParticipant.to_json())

# convert the object into a dict
faction_ranked_war_participant_dict = faction_ranked_war_participant_instance.to_dict()
# create an instance of FactionRankedWarParticipant from a dict
faction_ranked_war_participant_from_dict = FactionRankedWarParticipant.from_dict(faction_ranked_war_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


