# RacerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_id** | **int** |  | 
**position** | **int** |  | 
**car_id** | **int** |  | 
**car_item_id** | **int** |  | 
**car_item_name** | **str** |  | 
**car_class** | [**RaceClassEnum**](RaceClassEnum.md) |  | 
**has_crashed** | **bool** |  | 
**best_lap_time** | **float** |  | 
**race_time** | **float** |  | 
**time_ended** | **int** |  | 

## Example

```python
from openapi_client.models.racer_details import RacerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RacerDetails from a JSON string
racer_details_instance = RacerDetails.from_json(json)
# print the JSON string representation of the object
print(RacerDetails.to_json())

# convert the object into a dict
racer_details_dict = racer_details_instance.to_dict()
# create an instance of RacerDetails from a dict
racer_details_from_dict = RacerDetails.from_dict(racer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


