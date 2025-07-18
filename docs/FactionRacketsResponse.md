# FactionRacketsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rackets** | [**List[TornRacket]**](TornRacket.md) |  | 

## Example

```python
from openapi_client.models.faction_rackets_response import FactionRacketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRacketsResponse from a JSON string
faction_rackets_response_instance = FactionRacketsResponse.from_json(json)
# print the JSON string representation of the object
print(FactionRacketsResponse.to_json())

# convert the object into a dict
faction_rackets_response_dict = faction_rackets_response_instance.to_dict()
# create an instance of FactionRacketsResponse from a dict
faction_rackets_response_from_dict = FactionRacketsResponse.from_dict(faction_rackets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


