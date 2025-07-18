# ReportStockAnalysisItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**CountryEnum**](CountryEnum.md) |  | 
**item** | [**ReportStockAnalysisItemsInnerItem**](ReportStockAnalysisItemsInnerItem.md) |  | 
**trip_duration** | **int** |  | 
**hourly_profit** | **int** |  | 

## Example

```python
from openapi_client.models.report_stock_analysis_items_inner import ReportStockAnalysisItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReportStockAnalysisItemsInner from a JSON string
report_stock_analysis_items_inner_instance = ReportStockAnalysisItemsInner.from_json(json)
# print the JSON string representation of the object
print(ReportStockAnalysisItemsInner.to_json())

# convert the object into a dict
report_stock_analysis_items_inner_dict = report_stock_analysis_items_inner_instance.to_dict()
# create an instance of ReportStockAnalysisItemsInner from a dict
report_stock_analysis_items_inner_from_dict = ReportStockAnalysisItemsInner.from_dict(report_stock_analysis_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


