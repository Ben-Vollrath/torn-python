# UserCrimeDetailsScamming


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**most_responses** | **int** |  | [default to 0]
**zones** | [**UserCrimeDetailsScammingZones**](UserCrimeDetailsScammingZones.md) |  | 
**concerns** | [**UserCrimeDetailsScammingConcerns**](UserCrimeDetailsScammingConcerns.md) |  | 
**payouts** | [**UserCrimeDetailsScammingPayouts**](UserCrimeDetailsScammingPayouts.md) |  | 
**emails** | [**UserCrimeDetailsScammingEmails**](UserCrimeDetailsScammingEmails.md) |  | 

## Example

```python
from openapi_client.models.user_crime_details_scamming import UserCrimeDetailsScamming

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeDetailsScamming from a JSON string
user_crime_details_scamming_instance = UserCrimeDetailsScamming.from_json(json)
# print the JSON string representation of the object
print(UserCrimeDetailsScamming.to_json())

# convert the object into a dict
user_crime_details_scamming_dict = user_crime_details_scamming_instance.to_dict()
# create an instance of UserCrimeDetailsScamming from a dict
user_crime_details_scamming_from_dict = UserCrimeDetailsScamming.from_dict(user_crime_details_scamming_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


