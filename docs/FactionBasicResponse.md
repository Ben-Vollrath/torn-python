# FactionBasicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | [**FactionBasic**](FactionBasic.md) |  | 

## Example

```python
from openapi_client.models.faction_basic_response import FactionBasicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionBasicResponse from a JSON string
faction_basic_response_instance = FactionBasicResponse.from_json(json)
# print the JSON string representation of the object
print(FactionBasicResponse.to_json())

# convert the object into a dict
faction_basic_response_dict = faction_basic_response_instance.to_dict()
# create an instance of FactionBasicResponse from a dict
faction_basic_response_from_dict = FactionBasicResponse.from_dict(faction_basic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


