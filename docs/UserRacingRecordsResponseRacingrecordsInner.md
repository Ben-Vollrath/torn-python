# UserRacingRecordsResponseRacingrecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track** | [**UserRacingRecordsResponseRacingrecordsInnerTrack**](UserRacingRecordsResponseRacingrecordsInnerTrack.md) |  | 
**records** | [**List[UserRacingRecordsResponseRacingrecordsInnerRecordsInner]**](UserRacingRecordsResponseRacingrecordsInnerRecordsInner.md) |  | 

## Example

```python
from openapi_client.models.user_racing_records_response_racingrecords_inner import UserRacingRecordsResponseRacingrecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserRacingRecordsResponseRacingrecordsInner from a JSON string
user_racing_records_response_racingrecords_inner_instance = UserRacingRecordsResponseRacingrecordsInner.from_json(json)
# print the JSON string representation of the object
print(UserRacingRecordsResponseRacingrecordsInner.to_json())

# convert the object into a dict
user_racing_records_response_racingrecords_inner_dict = user_racing_records_response_racingrecords_inner_instance.to_dict()
# create an instance of UserRacingRecordsResponseRacingrecordsInner from a dict
user_racing_records_response_racingrecords_inner_from_dict = UserRacingRecordsResponseRacingrecordsInner.from_dict(user_racing_records_response_racingrecords_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


