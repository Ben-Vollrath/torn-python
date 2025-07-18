# FactionRankedWarResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rankedwars** | [**List[FactionRankedWarDetails]**](FactionRankedWarDetails.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.faction_ranked_war_response import FactionRankedWarResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRankedWarResponse from a JSON string
faction_ranked_war_response_instance = FactionRankedWarResponse.from_json(json)
# print the JSON string representation of the object
print(FactionRankedWarResponse.to_json())

# convert the object into a dict
faction_ranked_war_response_dict = faction_ranked_war_response_instance.to_dict()
# create an instance of FactionRankedWarResponse from a dict
faction_ranked_war_response_from_dict = FactionRankedWarResponse.from_dict(faction_ranked_war_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


