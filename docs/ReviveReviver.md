# ReviveReviver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**faction** | [**ReviveReviverFaction**](ReviveReviverFaction.md) |  | 
**skill** | **float** |  | 

## Example

```python
from openapi_client.models.revive_reviver import ReviveReviver

# TODO update the JSON string below
json = "{}"
# create an instance of ReviveReviver from a JSON string
revive_reviver_instance = ReviveReviver.from_json(json)
# print the JSON string representation of the object
print(ReviveReviver.to_json())

# convert the object into a dict
revive_reviver_dict = revive_reviver_instance.to_dict()
# create an instance of ReviveReviver from a dict
revive_reviver_from_dict = ReviveReviver.from_dict(revive_reviver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


