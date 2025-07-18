# UserLastAction

Details about a user's last action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**timestamp** | **int** |  | 
**relative** | **str** |  | 

## Example

```python
from openapi_client.models.user_last_action import UserLastAction

# TODO update the JSON string below
json = "{}"
# create an instance of UserLastAction from a JSON string
user_last_action_instance = UserLastAction.from_json(json)
# print the JSON string representation of the object
print(UserLastAction.to_json())

# convert the object into a dict
user_last_action_dict = user_last_action_instance.to_dict()
# create an instance of UserLastAction from a dict
user_last_action_from_dict = UserLastAction.from_dict(user_last_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


