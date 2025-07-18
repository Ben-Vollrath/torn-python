# AttackSimplified


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**code** | **str** |  | 
**started** | **int** | Attack start timestamp. | 
**ended** | **int** | Attack end timestamp. | 
**attacker** | [**AttackPlayerSimplified**](AttackPlayerSimplified.md) |  | 
**defender** | [**AttackPlayerSimplified**](AttackPlayerSimplified.md) |  | 
**result** | [**FactionAttackResult**](FactionAttackResult.md) |  | 
**respect_gain** | **float** |  | 
**respect_loss** | **float** |  | 

## Example

```python
from openapi_client.models.attack_simplified import AttackSimplified

# TODO update the JSON string below
json = "{}"
# create an instance of AttackSimplified from a JSON string
attack_simplified_instance = AttackSimplified.from_json(json)
# print the JSON string representation of the object
print(AttackSimplified.to_json())

# convert the object into a dict
attack_simplified_dict = attack_simplified_instance.to_dict()
# create an instance of AttackSimplified from a dict
attack_simplified_from_dict = AttackSimplified.from_dict(attack_simplified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


