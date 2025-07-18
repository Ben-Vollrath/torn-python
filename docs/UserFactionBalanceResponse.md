# UserFactionBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faction_balance** | [**UserFactionBalance**](UserFactionBalance.md) |  | 

## Example

```python
from openapi_client.models.user_faction_balance_response import UserFactionBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactionBalanceResponse from a JSON string
user_faction_balance_response_instance = UserFactionBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(UserFactionBalanceResponse.to_json())

# convert the object into a dict
user_faction_balance_response_dict = user_faction_balance_response_instance.to_dict()
# create an instance of UserFactionBalanceResponse from a dict
user_faction_balance_response_from_dict = UserFactionBalanceResponse.from_dict(user_faction_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


