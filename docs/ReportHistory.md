# ReportHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factions** | [**List[ReportHistoryFaction]**](ReportHistoryFaction.md) |  | 
**companies** | [**List[ReportHistoryCompany]**](ReportHistoryCompany.md) |  | 

## Example

```python
from openapi_client.models.report_history import ReportHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ReportHistory from a JSON string
report_history_instance = ReportHistory.from_json(json)
# print the JSON string representation of the object
print(ReportHistory.to_json())

# convert the object into a dict
report_history_dict = report_history_instance.to_dict()
# create an instance of ReportHistory from a dict
report_history_from_dict = ReportHistory.from_dict(report_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


