# FactionRankedWar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**war_id** | **int** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**target** | **int** | The score target of the war. | 
**winner** | **int** |  | 
**factions** | [**List[FactionRankedWarParticipant]**](FactionRankedWarParticipant.md) | The factions involved in the ranked war. | 

## Example

```python
from openapi_client.models.faction_ranked_war import FactionRankedWar

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRankedWar from a JSON string
faction_ranked_war_instance = FactionRankedWar.from_json(json)
# print the JSON string representation of the object
print(FactionRankedWar.to_json())

# convert the object into a dict
faction_ranked_war_dict = faction_ranked_war_instance.to_dict()
# create an instance of FactionRankedWar from a dict
faction_ranked_war_from_dict = FactionRankedWar.from_dict(faction_ranked_war_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


