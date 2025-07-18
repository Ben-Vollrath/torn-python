# UserOrganizedCrimeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organized_crime** | [**FactionCrime**](FactionCrime.md) |  | 

## Example

```python
from openapi_client.models.user_organized_crime_response import UserOrganizedCrimeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserOrganizedCrimeResponse from a JSON string
user_organized_crime_response_instance = UserOrganizedCrimeResponse.from_json(json)
# print the JSON string representation of the object
print(UserOrganizedCrimeResponse.to_json())

# convert the object into a dict
user_organized_crime_response_dict = user_organized_crime_response_instance.to_dict()
# create an instance of UserOrganizedCrimeResponse from a dict
user_organized_crime_response_from_dict = UserOrganizedCrimeResponse.from_dict(user_organized_crime_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


