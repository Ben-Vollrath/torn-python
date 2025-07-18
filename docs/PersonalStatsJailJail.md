# PersonalStatsJailJail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**times_jailed** | **int** |  | 
**busts** | [**PersonalStatsJailJailBusts**](PersonalStatsJailJailBusts.md) |  | 
**bails** | [**PersonalStatsDrugsDrugsRehabilitations**](PersonalStatsDrugsDrugsRehabilitations.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_jail_jail import PersonalStatsJailJail

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsJailJail from a JSON string
personal_stats_jail_jail_instance = PersonalStatsJailJail.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsJailJail.to_json())

# convert the object into a dict
personal_stats_jail_jail_dict = personal_stats_jail_jail_instance.to_dict()
# create an instance of PersonalStatsJailJail from a dict
personal_stats_jail_jail_from_dict = PersonalStatsJailJail.from_dict(personal_stats_jail_jail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


