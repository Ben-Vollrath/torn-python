# FactionContributor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**username** | **str** |  | 
**value** | **int** |  | 
**in_faction** | **bool** |  | 

## Example

```python
from openapi_client.models.faction_contributor import FactionContributor

# TODO update the JSON string below
json = "{}"
# create an instance of FactionContributor from a JSON string
faction_contributor_instance = FactionContributor.from_json(json)
# print the JSON string representation of the object
print(FactionContributor.to_json())

# convert the object into a dict
faction_contributor_dict = faction_contributor_instance.to_dict()
# create an instance of FactionContributor from a dict
faction_contributor_from_dict = FactionContributor.from_dict(faction_contributor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


