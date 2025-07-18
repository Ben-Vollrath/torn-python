# FactionHofResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hof** | [**FactionHofStats**](FactionHofStats.md) |  | 

## Example

```python
from openapi_client.models.faction_hof_response import FactionHofResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionHofResponse from a JSON string
faction_hof_response_instance = FactionHofResponse.from_json(json)
# print the JSON string representation of the object
print(FactionHofResponse.to_json())

# convert the object into a dict
faction_hof_response_dict = faction_hof_response_instance.to_dict()
# create an instance of FactionHofResponse from a dict
faction_hof_response_from_dict = FactionHofResponse.from_dict(faction_hof_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


