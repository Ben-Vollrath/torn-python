# FactionRaidReportFaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **float** |  | 
**attackers** | [**List[FactionRaidReportAttacker]**](FactionRaidReportAttacker.md) |  | 
**non_attackers** | [**List[FactionRaidReportUser]**](FactionRaidReportUser.md) |  | 

## Example

```python
from openapi_client.models.faction_raid_report_faction import FactionRaidReportFaction

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRaidReportFaction from a JSON string
faction_raid_report_faction_instance = FactionRaidReportFaction.from_json(json)
# print the JSON string representation of the object
print(FactionRaidReportFaction.to_json())

# convert the object into a dict
faction_raid_report_faction_dict = faction_raid_report_faction_instance.to_dict()
# create an instance of FactionRaidReportFaction from a dict
faction_raid_report_faction_from_dict = FactionRaidReportFaction.from_dict(faction_raid_report_faction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


