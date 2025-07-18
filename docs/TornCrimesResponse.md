# TornCrimesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crimes** | [**List[TornCrime]**](TornCrime.md) |  | 

## Example

```python
from openapi_client.models.torn_crimes_response import TornCrimesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornCrimesResponse from a JSON string
torn_crimes_response_instance = TornCrimesResponse.from_json(json)
# print the JSON string representation of the object
print(TornCrimesResponse.to_json())

# convert the object into a dict
torn_crimes_response_dict = torn_crimes_response_instance.to_dict()
# create an instance of TornCrimesResponse from a dict
torn_crimes_response_from_dict = TornCrimesResponse.from_dict(torn_crimes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


