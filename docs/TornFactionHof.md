# TornFactionHof


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**members** | **int** |  | 
**position** | **int** |  | 
**rank** | **str** | The full rank title &amp; division of the faction. | 
**values** | [**FactionHofValues**](FactionHofValues.md) |  | 

## Example

```python
from openapi_client.models.torn_faction_hof import TornFactionHof

# TODO update the JSON string below
json = "{}"
# create an instance of TornFactionHof from a JSON string
torn_faction_hof_instance = TornFactionHof.from_json(json)
# print the JSON string representation of the object
print(TornFactionHof.to_json())

# convert the object into a dict
torn_faction_hof_dict = torn_faction_hof_instance.to_dict()
# create an instance of TornFactionHof from a dict
torn_faction_hof_from_dict = TornFactionHof.from_dict(torn_faction_hof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


