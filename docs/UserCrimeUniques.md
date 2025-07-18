# UserCrimeUniques


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique result id. | 
**rewards** | [**UserCrimeUniquesReward**](UserCrimeUniquesReward.md) |  | 

## Example

```python
from openapi_client.models.user_crime_uniques import UserCrimeUniques

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeUniques from a JSON string
user_crime_uniques_instance = UserCrimeUniques.from_json(json)
# print the JSON string representation of the object
print(UserCrimeUniques.to_json())

# convert the object into a dict
user_crime_uniques_dict = user_crime_uniques_instance.to_dict()
# create an instance of UserCrimeUniques from a dict
user_crime_uniques_from_dict = UserCrimeUniques.from_dict(user_crime_uniques_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


