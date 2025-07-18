# FactionStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**List[FactionStat]**](FactionStat.md) |  | 

## Example

```python
from openapi_client.models.faction_stats_response import FactionStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionStatsResponse from a JSON string
faction_stats_response_instance = FactionStatsResponse.from_json(json)
# print the JSON string representation of the object
print(FactionStatsResponse.to_json())

# convert the object into a dict
faction_stats_response_dict = faction_stats_response_instance.to_dict()
# create an instance of FactionStatsResponse from a dict
faction_stats_response_from_dict = FactionStatsResponse.from_dict(faction_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


