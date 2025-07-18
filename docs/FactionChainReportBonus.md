# FactionChainReportBonus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacker_id** | **int** |  | 
**defender_id** | **int** |  | 
**chain** | **int** |  | 
**respect** | **int** |  | 

## Example

```python
from openapi_client.models.faction_chain_report_bonus import FactionChainReportBonus

# TODO update the JSON string below
json = "{}"
# create an instance of FactionChainReportBonus from a JSON string
faction_chain_report_bonus_instance = FactionChainReportBonus.from_json(json)
# print the JSON string representation of the object
print(FactionChainReportBonus.to_json())

# convert the object into a dict
faction_chain_report_bonus_dict = faction_chain_report_bonus_instance.to_dict()
# create an instance of FactionChainReportBonus from a dict
faction_chain_report_bonus_from_dict = FactionChainReportBonus.from_dict(faction_chain_report_bonus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


