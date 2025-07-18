# FactionRaidWarfare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**aggressor** | [**FactionRaidWarfareFaction**](FactionRaidWarfareFaction.md) |  | 
**defender** | [**FactionRaidWarfareFaction**](FactionRaidWarfareFaction.md) |  | 

## Example

```python
from openapi_client.models.faction_raid_warfare import FactionRaidWarfare

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRaidWarfare from a JSON string
faction_raid_warfare_instance = FactionRaidWarfare.from_json(json)
# print the JSON string representation of the object
print(FactionRaidWarfare.to_json())

# convert the object into a dict
faction_raid_warfare_dict = faction_raid_warfare_instance.to_dict()
# create an instance of FactionRaidWarfare from a dict
faction_raid_warfare_from_dict = FactionRaidWarfare.from_dict(faction_raid_warfare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


