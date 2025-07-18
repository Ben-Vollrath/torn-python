# ReportMostWanted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | [**List[ReportWarrantDetails]**](ReportWarrantDetails.md) |  | 
**notable** | [**List[ReportWarrantDetails]**](ReportWarrantDetails.md) |  | 

## Example

```python
from openapi_client.models.report_most_wanted import ReportMostWanted

# TODO update the JSON string below
json = "{}"
# create an instance of ReportMostWanted from a JSON string
report_most_wanted_instance = ReportMostWanted.from_json(json)
# print the JSON string representation of the object
print(ReportMostWanted.to_json())

# convert the object into a dict
report_most_wanted_dict = report_most_wanted_instance.to_dict()
# create an instance of ReportMostWanted from a dict
report_most_wanted_from_dict = ReportMostWanted.from_dict(report_most_wanted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


