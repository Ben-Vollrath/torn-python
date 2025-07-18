# ReportWarrantDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**warrant** | **int** |  | 

## Example

```python
from openapi_client.models.report_warrant_details import ReportWarrantDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReportWarrantDetails from a JSON string
report_warrant_details_instance = ReportWarrantDetails.from_json(json)
# print the JSON string representation of the object
print(ReportWarrantDetails.to_json())

# convert the object into a dict
report_warrant_details_dict = report_warrant_details_instance.to_dict()
# create an instance of ReportWarrantDetails from a dict
report_warrant_details_from_dict = ReportWarrantDetails.from_dict(report_warrant_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


