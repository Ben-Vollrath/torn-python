# FactionChainReportAttackerAttacks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**leave** | **int** |  | 
**mug** | **int** |  | 
**hospitalize** | **int** |  | 
**assists** | **int** |  | 
**retaliations** | **int** |  | 
**overseas** | **int** |  | 
**draws** | **int** |  | 
**escapes** | **int** |  | [optional] 
**losses** | **int** |  | 
**war** | **int** |  | 
**bonuses** | **int** |  | 

## Example

```python
from openapi_client.models.faction_chain_report_attacker_attacks import FactionChainReportAttackerAttacks

# TODO update the JSON string below
json = "{}"
# create an instance of FactionChainReportAttackerAttacks from a JSON string
faction_chain_report_attacker_attacks_instance = FactionChainReportAttackerAttacks.from_json(json)
# print the JSON string representation of the object
print(FactionChainReportAttackerAttacks.to_json())

# convert the object into a dict
faction_chain_report_attacker_attacks_dict = faction_chain_report_attacker_attacks_instance.to_dict()
# create an instance of FactionChainReportAttackerAttacks from a dict
faction_chain_report_attacker_attacks_from_dict = FactionChainReportAttackerAttacks.from_dict(faction_chain_report_attacker_attacks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


