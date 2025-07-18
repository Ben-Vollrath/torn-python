# FactionPact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faction_id** | **int** |  | 
**faction_name** | **str** |  | 
**until** | **str** | The duration until when is the non-aggression pact valid. | 

## Example

```python
from openapi_client.models.faction_pact import FactionPact

# TODO update the JSON string below
json = "{}"
# create an instance of FactionPact from a JSON string
faction_pact_instance = FactionPact.from_json(json)
# print the JSON string representation of the object
print(FactionPact.to_json())

# convert the object into a dict
faction_pact_dict = faction_pact_instance.to_dict()
# create an instance of FactionPact from a dict
faction_pact_from_dict = FactionPact.from_dict(faction_pact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


