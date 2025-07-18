# ReviveSimplified


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**reviver** | [**ReviveSimplifiedReviver**](ReviveSimplifiedReviver.md) |  | 
**target** | [**ReviveSimplifiedTarget**](ReviveSimplifiedTarget.md) |  | 
**success_chance** | **float** |  | 
**result** | **str** |  | 
**timestamp** | **int** |  | 

## Example

```python
from openapi_client.models.revive_simplified import ReviveSimplified

# TODO update the JSON string below
json = "{}"
# create an instance of ReviveSimplified from a JSON string
revive_simplified_instance = ReviveSimplified.from_json(json)
# print the JSON string representation of the object
print(ReviveSimplified.to_json())

# convert the object into a dict
revive_simplified_dict = revive_simplified_instance.to_dict()
# create an instance of ReviveSimplified from a dict
revive_simplified_from_dict = ReviveSimplified.from_dict(revive_simplified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


