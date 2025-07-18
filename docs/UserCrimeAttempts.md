# UserCrimeAttempts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**success** | **int** |  | 
**fail** | **int** |  | 
**critical_fail** | **int** |  | 
**subcrimes** | [**List[UserSubcrime]**](UserSubcrime.md) |  | 

## Example

```python
from openapi_client.models.user_crime_attempts import UserCrimeAttempts

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeAttempts from a JSON string
user_crime_attempts_instance = UserCrimeAttempts.from_json(json)
# print the JSON string representation of the object
print(UserCrimeAttempts.to_json())

# convert the object into a dict
user_crime_attempts_dict = user_crime_attempts_instance.to_dict()
# create an instance of UserCrimeAttempts from a dict
user_crime_attempts_from_dict = UserCrimeAttempts.from_dict(user_crime_attempts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


