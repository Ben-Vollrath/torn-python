# FactionSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**respect** | **int** |  | 
**members** | **int** |  | 
**leader** | [**FactionSearchLeader**](FactionSearchLeader.md) |  | 
**co_leader** | [**FactionSearchLeader**](FactionSearchLeader.md) |  | 
**image** | **str** |  | 
**tag_image** | **str** |  | 
**tag** | **str** |  | 
**is_destroyed** | **bool** |  | 
**is_recruiting** | **bool** |  | 

## Example

```python
from openapi_client.models.faction_search import FactionSearch

# TODO update the JSON string below
json = "{}"
# create an instance of FactionSearch from a JSON string
faction_search_instance = FactionSearch.from_json(json)
# print the JSON string representation of the object
print(FactionSearch.to_json())

# convert the object into a dict
faction_search_dict = faction_search_instance.to_dict()
# create an instance of FactionSearch from a dict
faction_search_from_dict = FactionSearch.from_dict(faction_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


