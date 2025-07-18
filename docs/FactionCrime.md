# FactionCrime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**previous_crime_id** | **int** |  | 
**name** | **str** |  | 
**difficulty** | **int** |  | 
**status** | [**FactionCrimeStatusEnum**](FactionCrimeStatusEnum.md) |  | 
**created_at** | **int** | The timestamp at which the crime was created. | 
**planning_at** | **int** |  | 
**ready_at** | **int** |  | 
**expired_at** | **int** | The timestamp at which the crime will expire. | 
**executed_at** | **int** |  | 
**slots** | [**List[FactionCrimeSlot]**](FactionCrimeSlot.md) |  | 
**rewards** | [**FactionCrimeReward**](FactionCrimeReward.md) |  | 

## Example

```python
from openapi_client.models.faction_crime import FactionCrime

# TODO update the JSON string below
json = "{}"
# create an instance of FactionCrime from a JSON string
faction_crime_instance = FactionCrime.from_json(json)
# print the JSON string representation of the object
print(FactionCrime.to_json())

# convert the object into a dict
faction_crime_dict = faction_crime_instance.to_dict()
# create an instance of FactionCrime from a dict
faction_crime_from_dict = FactionCrime.from_dict(faction_crime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


