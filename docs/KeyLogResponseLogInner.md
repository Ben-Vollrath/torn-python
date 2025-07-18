# KeyLogResponseLogInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**type** | **str** |  | 
**selections** | **str** |  | 
**id** | [**KeyLogResponseLogInnerId**](KeyLogResponseLogInnerId.md) |  | 
**comment** | **str** |  | [optional] 
**ip** | **str** |  | 

## Example

```python
from openapi_client.models.key_log_response_log_inner import KeyLogResponseLogInner

# TODO update the JSON string below
json = "{}"
# create an instance of KeyLogResponseLogInner from a JSON string
key_log_response_log_inner_instance = KeyLogResponseLogInner.from_json(json)
# print the JSON string representation of the object
print(KeyLogResponseLogInner.to_json())

# convert the object into a dict
key_log_response_log_inner_dict = key_log_response_log_inner_instance.to_dict()
# create an instance of KeyLogResponseLogInner from a dict
key_log_response_log_inner_from_dict = KeyLogResponseLogInner.from_dict(key_log_response_log_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


