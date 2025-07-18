# PersonalStatsAttackingPopularAttacking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacks** | [**PersonalStatsAttackingPopularAttackingAttacks**](PersonalStatsAttackingPopularAttackingAttacks.md) |  | 
**defends** | [**PersonalStatsAttackingPopularAttackingDefends**](PersonalStatsAttackingPopularAttackingDefends.md) |  | 
**elo** | **int** |  | 
**escapes** | [**PersonalStatsAttackingPublicAttackingEscapes**](PersonalStatsAttackingPublicAttackingEscapes.md) |  | 
**killstreak** | [**PersonalStatsAttackingPublicAttackingKillstreak**](PersonalStatsAttackingPublicAttackingKillstreak.md) |  | 
**hits** | [**PersonalStatsAttackingPublicAttackingHits**](PersonalStatsAttackingPublicAttackingHits.md) |  | 
**damage** | [**PersonalStatsAttackingPublicAttackingDamage**](PersonalStatsAttackingPublicAttackingDamage.md) |  | 
**networth** | [**PersonalStatsAttackingPublicAttackingNetworth**](PersonalStatsAttackingPublicAttackingNetworth.md) |  | 
**ammunition** | [**PersonalStatsAttackingPublicAttackingAmmunition**](PersonalStatsAttackingPublicAttackingAmmunition.md) |  | 
**faction** | [**PersonalStatsAttackingPopularAttackingFaction**](PersonalStatsAttackingPopularAttackingFaction.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_attacking_popular_attacking import PersonalStatsAttackingPopularAttacking

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsAttackingPopularAttacking from a JSON string
personal_stats_attacking_popular_attacking_instance = PersonalStatsAttackingPopularAttacking.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsAttackingPopularAttacking.to_json())

# convert the object into a dict
personal_stats_attacking_popular_attacking_dict = personal_stats_attacking_popular_attacking_instance.to_dict()
# create an instance of PersonalStatsAttackingPopularAttacking from a dict
personal_stats_attacking_popular_attacking_from_dict = PersonalStatsAttackingPopularAttacking.from_dict(personal_stats_attacking_popular_attacking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


