# FactionCrimesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crimes** | [**List[FactionCrime]**](FactionCrime.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.faction_crimes_response import FactionCrimesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionCrimesResponse from a JSON string
faction_crimes_response_instance = FactionCrimesResponse.from_json(json)
# print the JSON string representation of the object
print(FactionCrimesResponse.to_json())

# convert the object into a dict
faction_crimes_response_dict = faction_crimes_response_instance.to_dict()
# create an instance of FactionCrimesResponse from a dict
faction_crimes_response_from_dict = FactionCrimesResponse.from_dict(faction_crimes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


