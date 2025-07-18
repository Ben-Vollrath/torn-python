# UserCalendar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | Event start time displayed in TCT. | 

## Example

```python
from openapi_client.models.user_calendar import UserCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of UserCalendar from a JSON string
user_calendar_instance = UserCalendar.from_json(json)
# print the JSON string representation of the object
print(UserCalendar.to_json())

# convert the object into a dict
user_calendar_dict = user_calendar_instance.to_dict()
# create an instance of UserCalendar from a dict
user_calendar_from_dict = UserCalendar.from_dict(user_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


