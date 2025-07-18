# TornHofResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hof** | [**List[TornHof]**](TornHof.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.torn_hof_response import TornHofResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornHofResponse from a JSON string
torn_hof_response_instance = TornHofResponse.from_json(json)
# print the JSON string representation of the object
print(TornHofResponse.to_json())

# convert the object into a dict
torn_hof_response_dict = torn_hof_response_instance.to_dict()
# create an instance of TornHofResponse from a dict
torn_hof_response_from_dict = TornHofResponse.from_dict(torn_hof_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


