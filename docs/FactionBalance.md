# FactionBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faction** | [**FactionBalanceFaction**](FactionBalanceFaction.md) |  | 
**members** | [**List[FactionBalanceMembersInner]**](FactionBalanceMembersInner.md) |  | 

## Example

```python
from openapi_client.models.faction_balance import FactionBalance

# TODO update the JSON string below
json = "{}"
# create an instance of FactionBalance from a JSON string
faction_balance_instance = FactionBalance.from_json(json)
# print the JSON string representation of the object
print(FactionBalance.to_json())

# convert the object into a dict
faction_balance_dict = faction_balance_instance.to_dict()
# create an instance of FactionBalance from a dict
faction_balance_from_dict = FactionBalance.from_dict(faction_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


