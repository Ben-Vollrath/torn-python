# FactionChainWarfare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**chain** | **int** |  | 
**respect** | **float** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**faction** | [**FactionChainWarfareAllOfFaction**](FactionChainWarfareAllOfFaction.md) |  | 

## Example

```python
from openapi_client.models.faction_chain_warfare import FactionChainWarfare

# TODO update the JSON string below
json = "{}"
# create an instance of FactionChainWarfare from a JSON string
faction_chain_warfare_instance = FactionChainWarfare.from_json(json)
# print the JSON string representation of the object
print(FactionChainWarfare.to_json())

# convert the object into a dict
faction_chain_warfare_dict = faction_chain_warfare_instance.to_dict()
# create an instance of FactionChainWarfare from a dict
faction_chain_warfare_from_dict = FactionChainWarfare.from_dict(faction_chain_warfare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


