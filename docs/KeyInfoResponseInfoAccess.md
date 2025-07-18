# KeyInfoResponseInfoAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** |  | 
**type** | [**ApiKeyAccessTypeEnum**](ApiKeyAccessTypeEnum.md) |  | 
**faction** | **bool** |  | 
**faction_id** | **int** |  | [optional] 
**company** | **bool** |  | 
**company_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.key_info_response_info_access import KeyInfoResponseInfoAccess

# TODO update the JSON string below
json = "{}"
# create an instance of KeyInfoResponseInfoAccess from a JSON string
key_info_response_info_access_instance = KeyInfoResponseInfoAccess.from_json(json)
# print the JSON string representation of the object
print(KeyInfoResponseInfoAccess.to_json())

# convert the object into a dict
key_info_response_info_access_dict = key_info_response_info_access_instance.to_dict()
# create an instance of KeyInfoResponseInfoAccess from a dict
key_info_response_info_access_from_dict = KeyInfoResponseInfoAccess.from_dict(key_info_response_info_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


