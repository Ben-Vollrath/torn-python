# FactionChainReportAttacker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**respect** | [**FactionChainReportAttackerRespect**](FactionChainReportAttackerRespect.md) |  | 
**attacks** | [**FactionChainReportAttackerAttacks**](FactionChainReportAttackerAttacks.md) |  | 

## Example

```python
from openapi_client.models.faction_chain_report_attacker import FactionChainReportAttacker

# TODO update the JSON string below
json = "{}"
# create an instance of FactionChainReportAttacker from a JSON string
faction_chain_report_attacker_instance = FactionChainReportAttacker.from_json(json)
# print the JSON string representation of the object
print(FactionChainReportAttacker.to_json())

# convert the object into a dict
faction_chain_report_attacker_dict = faction_chain_report_attacker_instance.to_dict()
# create an instance of FactionChainReportAttacker from a dict
faction_chain_report_attacker_from_dict = FactionChainReportAttacker.from_dict(faction_chain_report_attacker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


