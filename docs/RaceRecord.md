# RaceRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_id** | **int** |  | 
**driver_name** | **str** |  | 
**car_item_id** | **int** |  | 
**lap_time** | **float** |  | 
**car_item_name** | **str** |  | 

## Example

```python
from openapi_client.models.race_record import RaceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of RaceRecord from a JSON string
race_record_instance = RaceRecord.from_json(json)
# print the JSON string representation of the object
print(RaceRecord.to_json())

# convert the object into a dict
race_record_dict = race_record_instance.to_dict()
# create an instance of RaceRecord from a dict
race_record_from_dict = RaceRecord.from_dict(race_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


