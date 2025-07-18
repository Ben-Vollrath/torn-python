# UserRaceCarDetails


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
**id** | **int** |  | 
**name** | **str** |  | 
**worth** | **int** |  | 
**points_spent** | **int** |  | 
**races_entered** | **int** |  | 
**races_won** | **int** |  | 
**is_removed** | **bool** |  | 
**parts** | **List[int]** |  | 

## Example

```python
from openapi_client.models.user_race_car_details import UserRaceCarDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserRaceCarDetails from a JSON string
user_race_car_details_instance = UserRaceCarDetails.from_json(json)
# print the JSON string representation of the object
print(UserRaceCarDetails.to_json())

# convert the object into a dict
user_race_car_details_dict = user_race_car_details_instance.to_dict()
# create an instance of UserRaceCarDetails from a dict
user_race_car_details_from_dict = UserRaceCarDetails.from_dict(user_race_car_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


