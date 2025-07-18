# TornItemBaseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**damage** | **int** |  | 
**accuracy** | **int** |  | 
**armor** | **int** |  | 

## Example

```python
from openapi_client.models.torn_item_base_stats import TornItemBaseStats

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemBaseStats from a JSON string
torn_item_base_stats_instance = TornItemBaseStats.from_json(json)
# print the JSON string representation of the object
print(TornItemBaseStats.to_json())

# convert the object into a dict
torn_item_base_stats_dict = torn_item_base_stats_instance.to_dict()
# create an instance of TornItemBaseStats from a dict
torn_item_base_stats_from_dict = TornItemBaseStats.from_dict(torn_item_base_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


