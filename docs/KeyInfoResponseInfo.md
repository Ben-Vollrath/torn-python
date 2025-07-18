# KeyInfoResponseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selections** | [**KeyInfoResponseInfoSelections**](KeyInfoResponseInfoSelections.md) |  | 
**user** | [**KeyInfoResponseInfoUser**](KeyInfoResponseInfoUser.md) |  | 
**access** | [**KeyInfoResponseInfoAccess**](KeyInfoResponseInfoAccess.md) |  | 

## Example

```python
from openapi_client.models.key_info_response_info import KeyInfoResponseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeyInfoResponseInfo from a JSON string
key_info_response_info_instance = KeyInfoResponseInfo.from_json(json)
# print the JSON string representation of the object
print(KeyInfoResponseInfo.to_json())

# convert the object into a dict
key_info_response_info_dict = key_info_response_info_instance.to_dict()
# create an instance of KeyInfoResponseInfo from a dict
key_info_response_info_from_dict = KeyInfoResponseInfo.from_dict(key_info_response_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


