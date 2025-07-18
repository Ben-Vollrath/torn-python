# FactionRaidReportAttacker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**FactionRaidReportUser**](FactionRaidReportUser.md) |  | 
**attacks** | **int** |  | 
**damage** | **float** |  | 

## Example

```python
from openapi_client.models.faction_raid_report_attacker import FactionRaidReportAttacker

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRaidReportAttacker from a JSON string
faction_raid_report_attacker_instance = FactionRaidReportAttacker.from_json(json)
# print the JSON string representation of the object
print(FactionRaidReportAttacker.to_json())

# convert the object into a dict
faction_raid_report_attacker_dict = faction_raid_report_attacker_instance.to_dict()
# create an instance of FactionRaidReportAttacker from a dict
faction_raid_report_attacker_from_dict = FactionRaidReportAttacker.from_dict(faction_raid_report_attacker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


