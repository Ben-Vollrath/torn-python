# AttackPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**level** | **int** |  | 
**faction** | [**AttackPlayerFaction**](AttackPlayerFaction.md) |  | 

## Example

```python
from openapi_client.models.attack_player import AttackPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of AttackPlayer from a JSON string
attack_player_instance = AttackPlayer.from_json(json)
# print the JSON string representation of the object
print(AttackPlayer.to_json())

# convert the object into a dict
attack_player_dict = attack_player_instance.to_dict()
# create an instance of AttackPlayer from a dict
attack_player_from_dict = AttackPlayer.from_dict(attack_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


