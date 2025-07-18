# FactionPositionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positions** | [**List[FactionPosition]**](FactionPosition.md) |  | 

## Example

```python
from openapi_client.models.faction_positions_response import FactionPositionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionPositionsResponse from a JSON string
faction_positions_response_instance = FactionPositionsResponse.from_json(json)
# print the JSON string representation of the object
print(FactionPositionsResponse.to_json())

# convert the object into a dict
faction_positions_response_dict = faction_positions_response_instance.to_dict()
# create an instance of FactionPositionsResponse from a dict
faction_positions_response_from_dict = FactionPositionsResponse.from_dict(faction_positions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


