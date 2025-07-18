# TornCalendarActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | 
**start** | **int** |  | 
**end** | **int** |  | 

## Example

```python
from openapi_client.models.torn_calendar_activity import TornCalendarActivity

# TODO update the JSON string below
json = "{}"
# create an instance of TornCalendarActivity from a JSON string
torn_calendar_activity_instance = TornCalendarActivity.from_json(json)
# print the JSON string representation of the object
print(TornCalendarActivity.to_json())

# convert the object into a dict
torn_calendar_activity_dict = torn_calendar_activity_instance.to_dict()
# create an instance of TornCalendarActivity from a dict
torn_calendar_activity_from_dict = TornCalendarActivity.from_dict(torn_calendar_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


