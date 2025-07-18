# UserCrimeDetailsGraffiti


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cans_used** | **int** |  | 
**most_graffiti_in_one_area** | **int** |  | 
**most_graffiti_simultaneously** | **int** |  | 
**graffiti_removed** | **int** |  | 
**cost_to_city** | **int** |  | 

## Example

```python
from openapi_client.models.user_crime_details_graffiti import UserCrimeDetailsGraffiti

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeDetailsGraffiti from a JSON string
user_crime_details_graffiti_instance = UserCrimeDetailsGraffiti.from_json(json)
# print the JSON string representation of the object
print(UserCrimeDetailsGraffiti.to_json())

# convert the object into a dict
user_crime_details_graffiti_dict = user_crime_details_graffiti_instance.to_dict()
# create an instance of UserCrimeDetailsGraffiti from a dict
user_crime_details_graffiti_from_dict = UserCrimeDetailsGraffiti.from_dict(user_crime_details_graffiti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


