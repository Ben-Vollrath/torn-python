# TornCalendarResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar** | [**TornCalendarResponseCalendar**](TornCalendarResponseCalendar.md) |  | 

## Example

```python
from openapi_client.models.torn_calendar_response import TornCalendarResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornCalendarResponse from a JSON string
torn_calendar_response_instance = TornCalendarResponse.from_json(json)
# print the JSON string representation of the object
print(TornCalendarResponse.to_json())

# convert the object into a dict
torn_calendar_response_dict = torn_calendar_response_instance.to_dict()
# create an instance of TornCalendarResponse from a dict
torn_calendar_response_from_dict = TornCalendarResponse.from_dict(torn_calendar_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


