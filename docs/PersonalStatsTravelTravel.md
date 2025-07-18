# PersonalStatsTravelTravel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**time_spent** | **int** |  | 
**items_bought** | **int** |  | 
**hunting** | [**PersonalStatsTravelTravelHunting**](PersonalStatsTravelTravelHunting.md) |  | 
**attacks_won** | **int** |  | 
**defends_lost** | **int** |  | 
**argentina** | **int** |  | 
**canada** | **int** |  | 
**cayman_islands** | **int** |  | 
**china** | **int** |  | 
**hawaii** | **int** |  | 
**japan** | **int** |  | 
**mexico** | **int** |  | 
**united_arab_emirates** | **int** |  | 
**united_kingdom** | **int** |  | 
**south_africa** | **int** |  | 
**switzerland** | **int** |  | 

## Example

```python
from openapi_client.models.personal_stats_travel_travel import PersonalStatsTravelTravel

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsTravelTravel from a JSON string
personal_stats_travel_travel_instance = PersonalStatsTravelTravel.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsTravelTravel.to_json())

# convert the object into a dict
personal_stats_travel_travel_dict = personal_stats_travel_travel_instance.to_dict()
# create an instance of PersonalStatsTravelTravel from a dict
personal_stats_travel_travel_from_dict = PersonalStatsTravelTravel.from_dict(personal_stats_travel_travel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


