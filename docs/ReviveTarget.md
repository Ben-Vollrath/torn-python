# ReviveTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**faction** | [**ReviveReviverFaction**](ReviveReviverFaction.md) |  | 
**hospital_reason** | **str** |  | 
**early_discharge** | **bool** |  | 
**last_action** | **int** |  | 
**online_status** | **str** |  | 

## Example

```python
from openapi_client.models.revive_target import ReviveTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ReviveTarget from a JSON string
revive_target_instance = ReviveTarget.from_json(json)
# print the JSON string representation of the object
print(ReviveTarget.to_json())

# convert the object into a dict
revive_target_dict = revive_target_instance.to_dict()
# create an instance of ReviveTarget from a dict
revive_target_from_dict = ReviveTarget.from_dict(revive_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


