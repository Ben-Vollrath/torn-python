# UserCrimeDetailsScammingZones


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**red** | **int** |  | [default to 0]
**neutral** | **int** |  | [default to 0]
**concern** | **int** |  | [default to 0]
**sensitivity** | **int** |  | [default to 0]
**temptation** | **int** |  | [default to 0]
**hesitation** | **int** |  | [default to 0]
**low_reward** | **int** |  | [default to 0]
**medium_reward** | **int** |  | [default to 0]
**high_reward** | **int** |  | [default to 0]

## Example

```python
from openapi_client.models.user_crime_details_scamming_zones import UserCrimeDetailsScammingZones

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeDetailsScammingZones from a JSON string
user_crime_details_scamming_zones_instance = UserCrimeDetailsScammingZones.from_json(json)
# print the JSON string representation of the object
print(UserCrimeDetailsScammingZones.to_json())

# convert the object into a dict
user_crime_details_scamming_zones_dict = user_crime_details_scamming_zones_instance.to_dict()
# create an instance of UserCrimeDetailsScammingZones from a dict
user_crime_details_scamming_zones_from_dict = UserCrimeDetailsScammingZones.from_dict(user_crime_details_scamming_zones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


