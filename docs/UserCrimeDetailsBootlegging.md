# UserCrimeDetailsBootlegging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online_store** | [**UserCrimeDetailsBootleggingOnlineStore**](UserCrimeDetailsBootleggingOnlineStore.md) |  | 
**dvd_sales** | [**UserCrimeDetailsBootleggingDvdSales**](UserCrimeDetailsBootleggingDvdSales.md) |  | 
**dvds_copied** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.user_crime_details_bootlegging import UserCrimeDetailsBootlegging

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeDetailsBootlegging from a JSON string
user_crime_details_bootlegging_instance = UserCrimeDetailsBootlegging.from_json(json)
# print the JSON string representation of the object
print(UserCrimeDetailsBootlegging.to_json())

# convert the object into a dict
user_crime_details_bootlegging_dict = user_crime_details_bootlegging_instance.to_dict()
# create an instance of UserCrimeDetailsBootlegging from a dict
user_crime_details_bootlegging_from_dict = UserCrimeDetailsBootlegging.from_dict(user_crime_details_bootlegging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


