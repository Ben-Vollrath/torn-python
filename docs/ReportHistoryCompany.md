# ReportHistoryCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**joined** | **date** |  | 
**left** | **date** |  | 

## Example

```python
from openapi_client.models.report_history_company import ReportHistoryCompany

# TODO update the JSON string below
json = "{}"
# create an instance of ReportHistoryCompany from a JSON string
report_history_company_instance = ReportHistoryCompany.from_json(json)
# print the JSON string representation of the object
print(ReportHistoryCompany.to_json())

# convert the object into a dict
report_history_company_dict = report_history_company_instance.to_dict()
# create an instance of ReportHistoryCompany from a dict
report_history_company_from_dict = ReportHistoryCompany.from_dict(report_history_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


