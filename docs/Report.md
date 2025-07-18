# Report


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ReportTypeEnum**](ReportTypeEnum.md) |  | 
**target_id** | **int** |  | 
**reporter_id** | **int** |  | 
**faction_id** | **int** |  | 
**timestamp** | **int** |  | 
**report** | [**ReportReportReport**](ReportReportReport.md) |  | 

## Example

```python
from openapi_client.models.report import Report

# TODO update the JSON string below
json = "{}"
# create an instance of Report from a JSON string
report_instance = Report.from_json(json)
# print the JSON string representation of the object
print(Report.to_json())

# convert the object into a dict
report_dict = report_instance.to_dict()
# create an instance of Report from a dict
report_from_dict = Report.from_dict(report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


