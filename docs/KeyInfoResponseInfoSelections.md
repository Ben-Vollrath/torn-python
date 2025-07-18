# KeyInfoResponseInfoSelections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **List[str]** |  | 
**faction** | [**List[FactionSelectionName]**](FactionSelectionName.md) |  | 
**market** | [**List[MarketSelectionName]**](MarketSelectionName.md) |  | 
**var_property** | **List[str]** |  | 
**torn** | [**List[TornSelectionName]**](TornSelectionName.md) |  | 
**user** | [**List[UserSelectionName]**](UserSelectionName.md) |  | 
**racing** | [**List[RacingSelectionName]**](RacingSelectionName.md) |  | 
**forum** | [**List[ForumSelectionName]**](ForumSelectionName.md) |  | 
**key** | [**List[KeySelectionName]**](KeySelectionName.md) |  | 

## Example

```python
from openapi_client.models.key_info_response_info_selections import KeyInfoResponseInfoSelections

# TODO update the JSON string below
json = "{}"
# create an instance of KeyInfoResponseInfoSelections from a JSON string
key_info_response_info_selections_instance = KeyInfoResponseInfoSelections.from_json(json)
# print the JSON string representation of the object
print(KeyInfoResponseInfoSelections.to_json())

# convert the object into a dict
key_info_response_info_selections_dict = key_info_response_info_selections_instance.to_dict()
# create an instance of KeyInfoResponseInfoSelections from a dict
key_info_response_info_selections_from_dict = KeyInfoResponseInfoSelections.from_dict(key_info_response_info_selections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


