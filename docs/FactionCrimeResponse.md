# FactionCrimeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crime** | [**FactionCrime**](FactionCrime.md) |  | 

## Example

```python
from openapi_client.models.faction_crime_response import FactionCrimeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionCrimeResponse from a JSON string
faction_crime_response_instance = FactionCrimeResponse.from_json(json)
# print the JSON string representation of the object
print(FactionCrimeResponse.to_json())

# convert the object into a dict
faction_crime_response_dict = faction_crime_response_instance.to_dict()
# create an instance of FactionCrimeResponse from a dict
faction_crime_response_from_dict = FactionCrimeResponse.from_dict(faction_crime_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


