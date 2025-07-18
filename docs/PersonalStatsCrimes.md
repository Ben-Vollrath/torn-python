# PersonalStatsCrimes

Response for PersonalStatsCrimes depends on which crime version user is currently.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crimes** | [**PersonalStatsCrimesCrimes**](PersonalStatsCrimesCrimes.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_crimes import PersonalStatsCrimes

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsCrimes from a JSON string
personal_stats_crimes_instance = PersonalStatsCrimes.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsCrimes.to_json())

# convert the object into a dict
personal_stats_crimes_dict = personal_stats_crimes_instance.to_dict()
# create an instance of PersonalStatsCrimes from a dict
personal_stats_crimes_from_dict = PersonalStatsCrimes.from_dict(personal_stats_crimes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


