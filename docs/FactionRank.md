# FactionRank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | /** | 
**name** | **str** |  | 
**division** | **int** |  | 
**position** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from openapi_client.models.faction_rank import FactionRank

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRank from a JSON string
faction_rank_instance = FactionRank.from_json(json)
# print the JSON string representation of the object
print(FactionRank.to_json())

# convert the object into a dict
faction_rank_dict = faction_rank_instance.to_dict()
# create an instance of FactionRank from a dict
faction_rank_from_dict = FactionRank.from_dict(faction_rank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


