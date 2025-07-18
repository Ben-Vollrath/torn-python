# AttackModifiers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fair_fight** | **float** |  | 
**war** | **float** |  | 
**retaliation** | **float** |  | 
**group** | **float** |  | 
**overseas** | **float** |  | 
**chain** | **float** |  | 
**warlord** | **float** |  | 

## Example

```python
from openapi_client.models.attack_modifiers import AttackModifiers

# TODO update the JSON string below
json = "{}"
# create an instance of AttackModifiers from a JSON string
attack_modifiers_instance = AttackModifiers.from_json(json)
# print the JSON string representation of the object
print(AttackModifiers.to_json())

# convert the object into a dict
attack_modifiers_dict = attack_modifiers_instance.to_dict()
# create an instance of AttackModifiers from a dict
attack_modifiers_from_dict = AttackModifiers.from_dict(attack_modifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


