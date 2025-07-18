# FactionRaidWarfareFaction

The field 'chain' exists only if the field 'end' is NOT populated in FactionRaidWarfare schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**score** | **float** |  | 
**chain** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.faction_raid_warfare_faction import FactionRaidWarfareFaction

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRaidWarfareFaction from a JSON string
faction_raid_warfare_faction_instance = FactionRaidWarfareFaction.from_json(json)
# print the JSON string representation of the object
print(FactionRaidWarfareFaction.to_json())

# convert the object into a dict
faction_raid_warfare_faction_dict = faction_raid_warfare_faction_instance.to_dict()
# create an instance of FactionRaidWarfareFaction from a dict
faction_raid_warfare_faction_from_dict = FactionRaidWarfareFaction.from_dict(faction_raid_warfare_faction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


