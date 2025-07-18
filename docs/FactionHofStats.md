# FactionHofStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | [**HofValueString**](HofValueString.md) |  | 
**respect** | [**HofValue**](HofValue.md) |  | 
**chain** | [**HofValue**](HofValue.md) |  | 

## Example

```python
from openapi_client.models.faction_hof_stats import FactionHofStats

# TODO update the JSON string below
json = "{}"
# create an instance of FactionHofStats from a JSON string
faction_hof_stats_instance = FactionHofStats.from_json(json)
# print the JSON string representation of the object
print(FactionHofStats.to_json())

# convert the object into a dict
faction_hof_stats_dict = faction_hof_stats_instance.to_dict()
# create an instance of FactionHofStats from a dict
faction_hof_stats_from_dict = FactionHofStats.from_dict(faction_hof_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


