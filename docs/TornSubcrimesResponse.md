# TornSubcrimesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subcrimes** | [**List[TornSubcrime]**](TornSubcrime.md) |  | 

## Example

```python
from openapi_client.models.torn_subcrimes_response import TornSubcrimesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornSubcrimesResponse from a JSON string
torn_subcrimes_response_instance = TornSubcrimesResponse.from_json(json)
# print the JSON string representation of the object
print(TornSubcrimesResponse.to_json())

# convert the object into a dict
torn_subcrimes_response_dict = torn_subcrimes_response_instance.to_dict()
# create an instance of TornSubcrimesResponse from a dict
torn_subcrimes_response_from_dict = TornSubcrimesResponse.from_dict(torn_subcrimes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


