# Bazaar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_open** | **bool** |  | 

## Example

```python
from openapi_client.models.bazaar import Bazaar

# TODO update the JSON string below
json = "{}"
# create an instance of Bazaar from a JSON string
bazaar_instance = Bazaar.from_json(json)
# print the JSON string representation of the object
print(Bazaar.to_json())

# convert the object into a dict
bazaar_dict = bazaar_instance.to_dict()
# create an instance of Bazaar from a dict
bazaar_from_dict = Bazaar.from_dict(bazaar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


