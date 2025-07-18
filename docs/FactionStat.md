# FactionStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**FactionStatEnum**](FactionStatEnum.md) |  | 
**value** | **int** |  | 

## Example

```python
from openapi_client.models.faction_stat import FactionStat

# TODO update the JSON string below
json = "{}"
# create an instance of FactionStat from a JSON string
faction_stat_instance = FactionStat.from_json(json)
# print the JSON string representation of the object
print(FactionStat.to_json())

# convert the object into a dict
faction_stat_dict = faction_stat_instance.to_dict()
# create an instance of FactionStat from a dict
faction_stat_from_dict = FactionStat.from_dict(faction_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


