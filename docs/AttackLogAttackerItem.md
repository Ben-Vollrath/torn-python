# AttackLogAttackerItem

This object could be null if there was no item being used in this turn or during this effect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.attack_log_attacker_item import AttackLogAttackerItem

# TODO update the JSON string below
json = "{}"
# create an instance of AttackLogAttackerItem from a JSON string
attack_log_attacker_item_instance = AttackLogAttackerItem.from_json(json)
# print the JSON string representation of the object
print(AttackLogAttackerItem.to_json())

# convert the object into a dict
attack_log_attacker_item_dict = attack_log_attacker_item_instance.to_dict()
# create an instance of AttackLogAttackerItem from a dict
attack_log_attacker_item_from_dict = AttackLogAttackerItem.from_dict(attack_log_attacker_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


