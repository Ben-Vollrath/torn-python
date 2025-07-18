# TornCalendarResponseCalendar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competitions** | [**List[TornCalendarActivity]**](TornCalendarActivity.md) |  | 
**events** | [**List[TornCalendarActivity]**](TornCalendarActivity.md) |  | 

## Example

```python
from openapi_client.models.torn_calendar_response_calendar import TornCalendarResponseCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of TornCalendarResponseCalendar from a JSON string
torn_calendar_response_calendar_instance = TornCalendarResponseCalendar.from_json(json)
# print the JSON string representation of the object
print(TornCalendarResponseCalendar.to_json())

# convert the object into a dict
torn_calendar_response_calendar_dict = torn_calendar_response_calendar_instance.to_dict()
# create an instance of TornCalendarResponseCalendar from a dict
torn_calendar_response_calendar_from_dict = TornCalendarResponseCalendar.from_dict(torn_calendar_response_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


