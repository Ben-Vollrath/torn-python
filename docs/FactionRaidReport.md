# FactionRaidReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**aggressor** | [**FactionRaidReportFaction**](FactionRaidReportFaction.md) |  | 
**defender** | [**FactionRaidReportFaction**](FactionRaidReportFaction.md) |  | 

## Example

```python
from openapi_client.models.faction_raid_report import FactionRaidReport

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRaidReport from a JSON string
faction_raid_report_instance = FactionRaidReport.from_json(json)
# print the JSON string representation of the object
print(FactionRaidReport.to_json())

# convert the object into a dict
faction_raid_report_dict = faction_raid_report_instance.to_dict()
# create an instance of FactionRaidReport from a dict
faction_raid_report_from_dict = FactionRaidReport.from_dict(faction_raid_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


