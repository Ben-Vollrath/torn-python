# AttackLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**timestamp** | **int** |  | 
**action** | [**AttackActionEnum**](AttackActionEnum.md) |  | 
**icon** | **str** |  | 
**attacker** | [**AttackLogAttacker**](AttackLogAttacker.md) |  | 
**defender** | [**AttackLogDefender**](AttackLogDefender.md) |  | 
**attacker_item** | [**AttackLogAttackerItem1**](AttackLogAttackerItem1.md) |  | [optional] 

## Example

```python
from openapi_client.models.attack_log import AttackLog

# TODO update the JSON string below
json = "{}"
# create an instance of AttackLog from a JSON string
attack_log_instance = AttackLog.from_json(json)
# print the JSON string representation of the object
print(AttackLog.to_json())

# convert the object into a dict
attack_log_dict = attack_log_instance.to_dict()
# create an instance of AttackLog from a dict
attack_log_from_dict = AttackLog.from_dict(attack_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


