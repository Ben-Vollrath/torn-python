# FactionPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_default** | **bool** |  | 
**abilities** | [**List[FactionPositionAbilityEnum]**](FactionPositionAbilityEnum.md) |  | 

## Example

```python
from openapi_client.models.faction_position import FactionPosition

# TODO update the JSON string below
json = "{}"
# create an instance of FactionPosition from a JSON string
faction_position_instance = FactionPosition.from_json(json)
# print the JSON string representation of the object
print(FactionPosition.to_json())

# convert the object into a dict
faction_position_dict = faction_position_instance.to_dict()
# create an instance of FactionPosition from a dict
faction_position_from_dict = FactionPosition.from_dict(faction_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


