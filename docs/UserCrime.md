# UserCrime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nerve_spent** | **int** |  | 
**skill** | **int** |  | 
**progression_bonus** | **int** |  | 
**rewards** | [**UserCrimeRewards**](UserCrimeRewards.md) |  | 
**attempts** | [**UserCrimeAttempts**](UserCrimeAttempts.md) |  | 
**uniques** | [**List[UserCrimeUniques]**](UserCrimeUniques.md) |  | 
**miscellaneous** | [**UserCrimeMiscellaneous**](UserCrimeMiscellaneous.md) |  | 

## Example

```python
from openapi_client.models.user_crime import UserCrime

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrime from a JSON string
user_crime_instance = UserCrime.from_json(json)
# print the JSON string representation of the object
print(UserCrime.to_json())

# convert the object into a dict
user_crime_dict = user_crime_instance.to_dict()
# create an instance of UserCrime from a dict
user_crime_from_dict = UserCrime.from_dict(user_crime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


