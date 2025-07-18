# FactionChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**chain** | **int** |  | 
**respect** | **float** |  | 
**start** | **int** |  | 
**end** | **int** |  | 

## Example

```python
from openapi_client.models.faction_chain import FactionChain

# TODO update the JSON string below
json = "{}"
# create an instance of FactionChain from a JSON string
faction_chain_instance = FactionChain.from_json(json)
# print the JSON string representation of the object
print(FactionChain.to_json())

# convert the object into a dict
faction_chain_dict = faction_chain_instance.to_dict()
# create an instance of FactionChain from a dict
faction_chain_from_dict = FactionChain.from_dict(faction_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


