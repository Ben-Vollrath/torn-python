# ReportBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ReportTypeEnum**](ReportTypeEnum.md) |  | 
**target_id** | **int** |  | 
**reporter_id** | **int** |  | 
**faction_id** | **int** |  | 
**timestamp** | **int** |  | 

## Example

```python
from openapi_client.models.report_base import ReportBase

# TODO update the JSON string below
json = "{}"
# create an instance of ReportBase from a JSON string
report_base_instance = ReportBase.from_json(json)
# print the JSON string representation of the object
print(ReportBase.to_json())

# convert the object into a dict
report_base_dict = report_base_instance.to_dict()
# create an instance of ReportBase from a dict
report_base_from_dict = ReportBase.from_dict(report_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


