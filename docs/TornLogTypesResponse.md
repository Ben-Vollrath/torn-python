# TornLogTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logtypes** | [**List[TornLog]**](TornLog.md) |  | 

## Example

```python
from openapi_client.models.torn_log_types_response import TornLogTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornLogTypesResponse from a JSON string
torn_log_types_response_instance = TornLogTypesResponse.from_json(json)
# print the JSON string representation of the object
print(TornLogTypesResponse.to_json())

# convert the object into a dict
torn_log_types_response_dict = torn_log_types_response_instance.to_dict()
# create an instance of TornLogTypesResponse from a dict
torn_log_types_response_from_dict = TornLogTypesResponse.from_dict(torn_log_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


