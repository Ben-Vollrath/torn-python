# FactionChainReportDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **int** |  | 
**respect** | **float** |  | 
**members** | **int** |  | 
**targets** | **int** |  | 
**war** | **int** |  | 
**best** | **float** |  | 
**leave** | **int** |  | 
**mug** | **int** |  | 
**hospitalize** | **int** |  | 
**assists** | **int** |  | 
**retaliations** | **int** |  | 
**overseas** | **int** |  | 
**draws** | **int** |  | 
**escapes** | **int** |  | 
**losses** | **int** |  | 

## Example

```python
from openapi_client.models.faction_chain_report_details import FactionChainReportDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FactionChainReportDetails from a JSON string
faction_chain_report_details_instance = FactionChainReportDetails.from_json(json)
# print the JSON string representation of the object
print(FactionChainReportDetails.to_json())

# convert the object into a dict
faction_chain_report_details_dict = faction_chain_report_details_instance.to_dict()
# create an instance of FactionChainReportDetails from a dict
faction_chain_report_details_from_dict = FactionChainReportDetails.from_dict(faction_chain_report_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


