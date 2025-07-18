# FactionApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | application id | 
**user** | [**FactionApplicationUser**](FactionApplicationUser.md) |  | 
**message** | **str** |  | 
**valid_until** | **int** |  | 
**status** | [**FactionApplicationStatusEnum**](FactionApplicationStatusEnum.md) |  | 

## Example

```python
from openapi_client.models.faction_application import FactionApplication

# TODO update the JSON string below
json = "{}"
# create an instance of FactionApplication from a JSON string
faction_application_instance = FactionApplication.from_json(json)
# print the JSON string representation of the object
print(FactionApplication.to_json())

# convert the object into a dict
faction_application_dict = faction_application_instance.to_dict()
# create an instance of FactionApplication from a dict
faction_application_from_dict = FactionApplication.from_dict(faction_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


