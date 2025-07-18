# FactionOngoingChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**current** | **int** |  | 
**max** | **int** |  | 
**timeout** | **int** | Seconds until chain breaks. | 
**modifier** | **float** |  | 
**cooldown** | **int** | Timestamp until when chain is on cooldown. | 
**start** | **int** |  | 
**end** | **int** |  | 

## Example

```python
from openapi_client.models.faction_ongoing_chain import FactionOngoingChain

# TODO update the JSON string below
json = "{}"
# create an instance of FactionOngoingChain from a JSON string
faction_ongoing_chain_instance = FactionOngoingChain.from_json(json)
# print the JSON string representation of the object
print(FactionOngoingChain.to_json())

# convert the object into a dict
faction_ongoing_chain_dict = faction_ongoing_chain_instance.to_dict()
# create an instance of FactionOngoingChain from a dict
faction_ongoing_chain_from_dict = FactionOngoingChain.from_dict(faction_ongoing_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


