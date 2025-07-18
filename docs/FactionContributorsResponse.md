# FactionContributorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributors** | [**List[FactionContributor]**](FactionContributor.md) |  | 

## Example

```python
from openapi_client.models.faction_contributors_response import FactionContributorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionContributorsResponse from a JSON string
faction_contributors_response_instance = FactionContributorsResponse.from_json(json)
# print the JSON string representation of the object
print(FactionContributorsResponse.to_json())

# convert the object into a dict
faction_contributors_response_dict = faction_contributors_response_instance.to_dict()
# create an instance of FactionContributorsResponse from a dict
faction_contributors_response_from_dict = FactionContributorsResponse.from_dict(faction_contributors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


