# AttackLogDefender

This value could be null in stealthed attacks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.attack_log_defender import AttackLogDefender

# TODO update the JSON string below
json = "{}"
# create an instance of AttackLogDefender from a JSON string
attack_log_defender_instance = AttackLogDefender.from_json(json)
# print the JSON string representation of the object
print(AttackLogDefender.to_json())

# convert the object into a dict
attack_log_defender_dict = attack_log_defender_instance.to_dict()
# create an instance of AttackLogDefender from a dict
attack_log_defender_from_dict = AttackLogDefender.from_dict(attack_log_defender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


