# FactionBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**FactionBalance**](FactionBalance.md) |  | 

## Example

```python
from openapi_client.models.faction_balance_response import FactionBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionBalanceResponse from a JSON string
faction_balance_response_instance = FactionBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(FactionBalanceResponse.to_json())

# convert the object into a dict
faction_balance_response_dict = faction_balance_response_instance.to_dict()
# create an instance of FactionBalanceResponse from a dict
faction_balance_response_from_dict = FactionBalanceResponse.from_dict(faction_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


