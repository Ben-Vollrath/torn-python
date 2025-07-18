# UserRacingRecordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**racingrecords** | [**List[UserRacingRecordsResponseRacingrecordsInner]**](UserRacingRecordsResponseRacingrecordsInner.md) |  | 

## Example

```python
from openapi_client.models.user_racing_records_response import UserRacingRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserRacingRecordsResponse from a JSON string
user_racing_records_response_instance = UserRacingRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(UserRacingRecordsResponse.to_json())

# convert the object into a dict
user_racing_records_response_dict = user_racing_records_response_instance.to_dict()
# create an instance of UserRacingRecordsResponse from a dict
user_racing_records_response_from_dict = UserRacingRecordsResponse.from_dict(user_racing_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


