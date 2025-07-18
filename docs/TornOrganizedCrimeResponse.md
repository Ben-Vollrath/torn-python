# TornOrganizedCrimeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizedcrimes** | [**List[TornOrganizedCrime]**](TornOrganizedCrime.md) |  | 

## Example

```python
from openapi_client.models.torn_organized_crime_response import TornOrganizedCrimeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornOrganizedCrimeResponse from a JSON string
torn_organized_crime_response_instance = TornOrganizedCrimeResponse.from_json(json)
# print the JSON string representation of the object
print(TornOrganizedCrimeResponse.to_json())

# convert the object into a dict
torn_organized_crime_response_dict = torn_organized_crime_response_instance.to_dict()
# create an instance of TornOrganizedCrimeResponse from a dict
torn_organized_crime_response_from_dict = TornOrganizedCrimeResponse.from_dict(torn_organized_crime_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


