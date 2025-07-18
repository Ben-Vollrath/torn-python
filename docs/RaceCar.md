# RaceCar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**car_item_id** | **int** |  | 
**car_item_name** | **str** |  | 
**top_speed** | **int** |  | 
**acceleration** | **int** |  | 
**braking** | **int** |  | 
**dirt** | **int** |  | 
**handling** | **int** |  | 
**safety** | **int** |  | 
**tarmac** | **int** |  | 
**var_class** | [**RaceClassEnum**](RaceClassEnum.md) |  | 

## Example

```python
from openapi_client.models.race_car import RaceCar

# TODO update the JSON string below
json = "{}"
# create an instance of RaceCar from a JSON string
race_car_instance = RaceCar.from_json(json)
# print the JSON string representation of the object
print(RaceCar.to_json())

# convert the object into a dict
race_car_dict = race_car_instance.to_dict()
# create an instance of RaceCar from a dict
race_car_from_dict = RaceCar.from_dict(race_car_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


