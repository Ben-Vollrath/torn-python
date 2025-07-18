# AttackLogAttacker

This value could be null in stealthed attacks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**item** | [**AttackLogAttackerItem**](AttackLogAttackerItem.md) |  | 

## Example

```python
from openapi_client.models.attack_log_attacker import AttackLogAttacker

# TODO update the JSON string below
json = "{}"
# create an instance of AttackLogAttacker from a JSON string
attack_log_attacker_instance = AttackLogAttacker.from_json(json)
# print the JSON string representation of the object
print(AttackLogAttacker.to_json())

# convert the object into a dict
attack_log_attacker_dict = attack_log_attacker_instance.to_dict()
# create an instance of AttackLogAttacker from a dict
attack_log_attacker_from_dict = AttackLogAttacker.from_dict(attack_log_attacker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


