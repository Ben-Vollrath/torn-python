# FactionWarfareResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warfare** | [**FactionWarfareResponseWarfare**](FactionWarfareResponseWarfare.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.faction_warfare_response import FactionWarfareResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionWarfareResponse from a JSON string
faction_warfare_response_instance = FactionWarfareResponse.from_json(json)
# print the JSON string representation of the object
print(FactionWarfareResponse.to_json())

# convert the object into a dict
faction_warfare_response_dict = faction_warfare_response_instance.to_dict()
# create an instance of FactionWarfareResponse from a dict
faction_warfare_response_from_dict = FactionWarfareResponse.from_dict(faction_warfare_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


