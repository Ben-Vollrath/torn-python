# PersonalStatsAttackingPublicAttacking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacks** | [**PersonalStatsAttackingPublicAttackingAttacks**](PersonalStatsAttackingPublicAttackingAttacks.md) |  | 
**defends** | [**PersonalStatsAttackingPublicAttackingDefends**](PersonalStatsAttackingPublicAttackingDefends.md) |  | 
**elo** | **int** |  | 
**unarmored_wins** | **int** |  | 
**highest_level_beaten** | **int** |  | 
**escapes** | [**PersonalStatsAttackingPublicAttackingEscapes**](PersonalStatsAttackingPublicAttackingEscapes.md) |  | [optional] 
**killstreak** | [**PersonalStatsAttackingPublicAttackingKillstreak**](PersonalStatsAttackingPublicAttackingKillstreak.md) |  | 
**hits** | [**PersonalStatsAttackingPublicAttackingHits**](PersonalStatsAttackingPublicAttackingHits.md) |  | 
**damage** | [**PersonalStatsAttackingPublicAttackingDamage**](PersonalStatsAttackingPublicAttackingDamage.md) |  | 
**networth** | [**PersonalStatsAttackingPublicAttackingNetworth**](PersonalStatsAttackingPublicAttackingNetworth.md) |  | 
**ammunition** | [**PersonalStatsAttackingPublicAttackingAmmunition**](PersonalStatsAttackingPublicAttackingAmmunition.md) |  | 
**faction** | [**PersonalStatsAttackingPublicAttackingFaction**](PersonalStatsAttackingPublicAttackingFaction.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_attacking_public_attacking import PersonalStatsAttackingPublicAttacking

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsAttackingPublicAttacking from a JSON string
personal_stats_attacking_public_attacking_instance = PersonalStatsAttackingPublicAttacking.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsAttackingPublicAttacking.to_json())

# convert the object into a dict
personal_stats_attacking_public_attacking_dict = personal_stats_attacking_public_attacking_instance.to_dict()
# create an instance of PersonalStatsAttackingPublicAttacking from a dict
personal_stats_attacking_public_attacking_from_dict = PersonalStatsAttackingPublicAttacking.from_dict(personal_stats_attacking_public_attacking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


