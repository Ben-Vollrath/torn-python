# FactionWarfareDirtyBomb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**planted_at** | **int** |  | 
**detonated_at** | **int** |  | 
**faction** | [**FactionWarfareDirtyBombTargetFaction**](FactionWarfareDirtyBombTargetFaction.md) |  | 
**user** | [**FactionWarfareDirtyBombPlanter**](FactionWarfareDirtyBombPlanter.md) |  | 

## Example

```python
from openapi_client.models.faction_warfare_dirty_bomb import FactionWarfareDirtyBomb

# TODO update the JSON string below
json = "{}"
# create an instance of FactionWarfareDirtyBomb from a JSON string
faction_warfare_dirty_bomb_instance = FactionWarfareDirtyBomb.from_json(json)
# print the JSON string representation of the object
print(FactionWarfareDirtyBomb.to_json())

# convert the object into a dict
faction_warfare_dirty_bomb_dict = faction_warfare_dirty_bomb_instance.to_dict()
# create an instance of FactionWarfareDirtyBomb from a dict
faction_warfare_dirty_bomb_from_dict = FactionWarfareDirtyBomb.from_dict(faction_warfare_dirty_bomb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


