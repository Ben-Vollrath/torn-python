# FactionRaidsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raids** | [**List[FactionRaidWarfare]**](FactionRaidWarfare.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.faction_raids_response import FactionRaidsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRaidsResponse from a JSON string
faction_raids_response_instance = FactionRaidsResponse.from_json(json)
# print the JSON string representation of the object
print(FactionRaidsResponse.to_json())

# convert the object into a dict
faction_raids_response_dict = faction_raids_response_instance.to_dict()
# create an instance of FactionRaidsResponse from a dict
faction_raids_response_from_dict = FactionRaidsResponse.from_dict(faction_raids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


