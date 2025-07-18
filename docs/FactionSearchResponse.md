# FactionSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**List[FactionSearch]**](FactionSearch.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.faction_search_response import FactionSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionSearchResponse from a JSON string
faction_search_response_instance = FactionSearchResponse.from_json(json)
# print the JSON string representation of the object
print(FactionSearchResponse.to_json())

# convert the object into a dict
faction_search_response_dict = faction_search_response_instance.to_dict()
# create an instance of FactionSearchResponse from a dict
faction_search_response_from_dict = FactionSearchResponse.from_dict(faction_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


