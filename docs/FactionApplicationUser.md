# FactionApplicationUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**level** | **int** |  | 
**stats** | [**FactionApplicationUserStats**](FactionApplicationUserStats.md) |  | 

## Example

```python
from openapi_client.models.faction_application_user import FactionApplicationUser

# TODO update the JSON string below
json = "{}"
# create an instance of FactionApplicationUser from a JSON string
faction_application_user_instance = FactionApplicationUser.from_json(json)
# print the JSON string representation of the object
print(FactionApplicationUser.to_json())

# convert the object into a dict
faction_application_user_dict = faction_application_user_instance.to_dict()
# create an instance of FactionApplicationUser from a dict
faction_application_user_from_dict = FactionApplicationUser.from_dict(faction_application_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


