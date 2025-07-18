# TornHofBasicValue

Value representing the chosen category. Traveltime is shown in seconds. If the chosen category is 'rank', the value is of type string. If the chosen category is 'racingskill', the value is of type float. Otherwise it is an integer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.torn_hof_basic_value import TornHofBasicValue

# TODO update the JSON string below
json = "{}"
# create an instance of TornHofBasicValue from a JSON string
torn_hof_basic_value_instance = TornHofBasicValue.from_json(json)
# print the JSON string representation of the object
print(TornHofBasicValue.to_json())

# convert the object into a dict
torn_hof_basic_value_dict = torn_hof_basic_value_instance.to_dict()
# create an instance of TornHofBasicValue from a dict
torn_hof_basic_value_from_dict = TornHofBasicValue.from_dict(torn_hof_basic_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


