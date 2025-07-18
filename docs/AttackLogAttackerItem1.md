# AttackLogAttackerItem1

This field only exists if the attacker is stealthed and they used a temporary item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.attack_log_attacker_item1 import AttackLogAttackerItem1

# TODO update the JSON string below
json = "{}"
# create an instance of AttackLogAttackerItem1 from a JSON string
attack_log_attacker_item1_instance = AttackLogAttackerItem1.from_json(json)
# print the JSON string representation of the object
print(AttackLogAttackerItem1.to_json())

# convert the object into a dict
attack_log_attacker_item1_dict = attack_log_attacker_item1_instance.to_dict()
# create an instance of AttackLogAttackerItem1 from a dict
attack_log_attacker_item1_from_dict = AttackLogAttackerItem1.from_dict(attack_log_attacker_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


