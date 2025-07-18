# KeyInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**KeyInfoResponseInfo**](KeyInfoResponseInfo.md) |  | 

## Example

```python
from openapi_client.models.key_info_response import KeyInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeyInfoResponse from a JSON string
key_info_response_instance = KeyInfoResponse.from_json(json)
# print the JSON string representation of the object
print(KeyInfoResponse.to_json())

# convert the object into a dict
key_info_response_dict = key_info_response_instance.to_dict()
# create an instance of KeyInfoResponse from a dict
key_info_response_from_dict = KeyInfoResponse.from_dict(key_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


