# ReportStockAnalysisItemsInnerItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**price** | **int** |  | 
**value** | **int** |  | 
**due** | **int** |  | 

## Example

```python
from openapi_client.models.report_stock_analysis_items_inner_item import ReportStockAnalysisItemsInnerItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReportStockAnalysisItemsInnerItem from a JSON string
report_stock_analysis_items_inner_item_instance = ReportStockAnalysisItemsInnerItem.from_json(json)
# print the JSON string representation of the object
print(ReportStockAnalysisItemsInnerItem.to_json())

# convert the object into a dict
report_stock_analysis_items_inner_item_dict = report_stock_analysis_items_inner_item_instance.to_dict()
# create an instance of ReportStockAnalysisItemsInnerItem from a dict
report_stock_analysis_items_inner_item_from_dict = ReportStockAnalysisItemsInnerItem.from_dict(report_stock_analysis_items_inner_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


