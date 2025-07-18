# FactionChainsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chains** | [**List[FactionChain]**](FactionChain.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.faction_chains_response import FactionChainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionChainsResponse from a JSON string
faction_chains_response_instance = FactionChainsResponse.from_json(json)
# print the JSON string representation of the object
print(FactionChainsResponse.to_json())

# convert the object into a dict
faction_chains_response_dict = faction_chains_response_instance.to_dict()
# create an instance of FactionChainsResponse from a dict
faction_chains_response_from_dict = FactionChainsResponse.from_dict(faction_chains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


