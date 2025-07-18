# FactionRaidWarReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raidreport** | [**List[FactionRaidReport]**](FactionRaidReport.md) |  | 

## Example

```python
from openapi_client.models.faction_raid_war_report_response import FactionRaidWarReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRaidWarReportResponse from a JSON string
faction_raid_war_report_response_instance = FactionRaidWarReportResponse.from_json(json)
# print the JSON string representation of the object
print(FactionRaidWarReportResponse.to_json())

# convert the object into a dict
faction_raid_war_report_response_dict = faction_raid_war_report_response_instance.to_dict()
# create an instance of FactionRaidWarReportResponse from a dict
faction_raid_war_report_response_from_dict = FactionRaidWarReportResponse.from_dict(faction_raid_war_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


