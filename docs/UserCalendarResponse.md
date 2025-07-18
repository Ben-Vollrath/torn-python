# UserCalendarResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar** | [**UserCalendar**](UserCalendar.md) |  | 

## Example

```python
from openapi_client.models.user_calendar_response import UserCalendarResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserCalendarResponse from a JSON string
user_calendar_response_instance = UserCalendarResponse.from_json(json)
# print the JSON string representation of the object
print(UserCalendarResponse.to_json())

# convert the object into a dict
user_calendar_response_dict = user_calendar_response_instance.to_dict()
# create an instance of UserCalendarResponse from a dict
user_calendar_response_from_dict = UserCalendarResponse.from_dict(user_calendar_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


