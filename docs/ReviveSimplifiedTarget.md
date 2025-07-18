# ReviveSimplifiedTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**faction_id** | **int** |  | 
**hospital_reason** | **str** |  | 
**early_discharge** | **bool** |  | 
**last_action** | **int** |  | 
**online_status** | **str** |  | 

## Example

```python
from openapi_client.models.revive_simplified_target import ReviveSimplifiedTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ReviveSimplifiedTarget from a JSON string
revive_simplified_target_instance = ReviveSimplifiedTarget.from_json(json)
# print the JSON string representation of the object
print(ReviveSimplifiedTarget.to_json())

# convert the object into a dict
revive_simplified_target_dict = revive_simplified_target_instance.to_dict()
# create an instance of ReviveSimplifiedTarget from a dict
revive_simplified_target_from_dict = ReviveSimplifiedTarget.from_dict(revive_simplified_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


