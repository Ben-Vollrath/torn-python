# KeyLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | [**List[KeyLogResponseLogInner]**](KeyLogResponseLogInner.md) |  | 

## Example

```python
from openapi_client.models.key_log_response import KeyLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeyLogResponse from a JSON string
key_log_response_instance = KeyLogResponse.from_json(json)
# print the JSON string representation of the object
print(KeyLogResponse.to_json())

# convert the object into a dict
key_log_response_dict = key_log_response_instance.to_dict()
# create an instance of KeyLogResponse from a dict
key_log_response_from_dict = KeyLogResponse.from_dict(key_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


