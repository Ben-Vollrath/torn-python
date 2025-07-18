# Bounty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int** |  | 
**target_name** | **str** |  | 
**target_level** | **int** |  | 
**lister_id** | **int** |  | 
**lister_name** | **str** |  | 
**reward** | **int** |  | 
**reason** | **str** |  | 
**quantity** | **int** |  | 
**is_anonymous** | **bool** |  | 
**valid_until** | **int** |  | 

## Example

```python
from openapi_client.models.bounty import Bounty

# TODO update the JSON string below
json = "{}"
# create an instance of Bounty from a JSON string
bounty_instance = Bounty.from_json(json)
# print the JSON string representation of the object
print(Bounty.to_json())

# convert the object into a dict
bounty_dict = bounty_instance.to_dict()
# create an instance of Bounty from a dict
bounty_from_dict = Bounty.from_dict(bounty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


