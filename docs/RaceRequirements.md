# RaceRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**car_class** | [**RaceClassEnum**](RaceClassEnum.md) |  | 
**driver_class** | [**RaceClassEnum**](RaceClassEnum.md) |  | 
**car_item_id** | **int** |  | 
**requires_stock_car** | **bool** |  | 
**requires_password** | **bool** |  | 
**join_fee** | **int** |  | 

## Example

```python
from openapi_client.models.race_requirements import RaceRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of RaceRequirements from a JSON string
race_requirements_instance = RaceRequirements.from_json(json)
# print the JSON string representation of the object
print(RaceRequirements.to_json())

# convert the object into a dict
race_requirements_dict = race_requirements_instance.to_dict()
# create an instance of RaceRequirements from a dict
race_requirements_from_dict = RaceRequirements.from_dict(race_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


