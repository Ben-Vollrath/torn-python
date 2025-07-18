# ReportStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strength** | **int** |  | 
**speed** | **int** |  | 
**dexterity** | **int** |  | 
**defense** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.report_stats import ReportStats

# TODO update the JSON string below
json = "{}"
# create an instance of ReportStats from a JSON string
report_stats_instance = ReportStats.from_json(json)
# print the JSON string representation of the object
print(ReportStats.to_json())

# convert the object into a dict
report_stats_dict = report_stats_instance.to_dict()
# create an instance of ReportStats from a dict
report_stats_from_dict = ReportStats.from_dict(report_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


