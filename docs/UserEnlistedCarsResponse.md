# UserEnlistedCarsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enlistedcars** | [**List[UserRaceCarDetails]**](UserRaceCarDetails.md) |  | 

## Example

```python
from openapi_client.models.user_enlisted_cars_response import UserEnlistedCarsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserEnlistedCarsResponse from a JSON string
user_enlisted_cars_response_instance = UserEnlistedCarsResponse.from_json(json)
# print the JSON string representation of the object
print(UserEnlistedCarsResponse.to_json())

# convert the object into a dict
user_enlisted_cars_response_dict = user_enlisted_cars_response_instance.to_dict()
# create an instance of UserEnlistedCarsResponse from a dict
user_enlisted_cars_response_from_dict = UserEnlistedCarsResponse.from_dict(user_enlisted_cars_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


