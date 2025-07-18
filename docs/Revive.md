# Revive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**reviver** | [**ReviveReviver**](ReviveReviver.md) |  | 
**target** | [**ReviveTarget**](ReviveTarget.md) |  | 
**success_chance** | **float** |  | 
**result** | **str** |  | 
**timestamp** | **int** |  | 

## Example

```python
from openapi_client.models.revive import Revive

# TODO update the JSON string below
json = "{}"
# create an instance of Revive from a JSON string
revive_instance = Revive.from_json(json)
# print the JSON string representation of the object
print(Revive.to_json())

# convert the object into a dict
revive_dict = revive_instance.to_dict()
# create an instance of Revive from a dict
revive_from_dict = Revive.from_dict(revive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


