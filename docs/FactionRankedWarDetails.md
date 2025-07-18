# FactionRankedWarDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**start** | **int** | Timestamp the war started at. | 
**end** | **int** | Timestamp the war ended at. | 
**target** | **int** |  | 
**winner** | **int** |  | 
**factions** | [**List[FactionRankedWarDetailsFactionsInner]**](FactionRankedWarDetailsFactionsInner.md) |  | 

## Example

```python
from openapi_client.models.faction_ranked_war_details import FactionRankedWarDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRankedWarDetails from a JSON string
faction_ranked_war_details_instance = FactionRankedWarDetails.from_json(json)
# print the JSON string representation of the object
print(FactionRankedWarDetails.to_json())

# convert the object into a dict
faction_ranked_war_details_dict = faction_ranked_war_details_instance.to_dict()
# create an instance of FactionRankedWarDetails from a dict
faction_ranked_war_details_from_dict = FactionRankedWarDetails.from_dict(faction_ranked_war_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


