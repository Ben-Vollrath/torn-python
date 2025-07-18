# Attack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**code** | **str** |  | 
**started** | **int** | Attack start timestamp. | 
**ended** | **int** | Attack end timestamp. | 
**attacker** | [**AttackPlayer**](AttackPlayer.md) |  | 
**defender** | [**AttackPlayer**](AttackPlayer.md) |  | 
**result** | [**FactionAttackResult**](FactionAttackResult.md) |  | 
**respect_gain** | **float** |  | 
**respect_loss** | **float** |  | 
**chain** | **int** |  | 
**is_interrupted** | **bool** | This is an experimental flag which should help determine &#39;assist&#39; attacks which have not contributed to the chain. For example, attacks such as where the opponent lost to someoene else before the attacker could finish the attack. This flag might not work entirely correctly, so use with caution. | 
**is_stealthed** | **bool** |  | 
**is_raid** | **bool** |  | 
**is_ranked_war** | **bool** |  | 
**finishing_hit_effects** | [**List[AttackingFinishingHitEffects]**](AttackingFinishingHitEffects.md) |  | 
**modifiers** | [**AttackModifiers**](AttackModifiers.md) |  | 

## Example

```python
from openapi_client.models.attack import Attack

# TODO update the JSON string below
json = "{}"
# create an instance of Attack from a JSON string
attack_instance = Attack.from_json(json)
# print the JSON string representation of the object
print(Attack.to_json())

# convert the object into a dict
attack_dict = attack_instance.to_dict()
# create an instance of Attack from a dict
attack_from_dict = Attack.from_dict(attack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


