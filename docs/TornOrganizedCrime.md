# TornOrganizedCrime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**difficulty** | **int** |  | 
**spawn** | [**TornOrganizedCrimeSpawn**](TornOrganizedCrimeSpawn.md) |  | 
**scope** | [**TornOrganizedCrimeScope**](TornOrganizedCrimeScope.md) |  | 
**prerequisite** | **str** |  | 
**slots** | [**List[TornOrganizedCrimeSlot]**](TornOrganizedCrimeSlot.md) |  | 

## Example

```python
from openapi_client.models.torn_organized_crime import TornOrganizedCrime

# TODO update the JSON string below
json = "{}"
# create an instance of TornOrganizedCrime from a JSON string
torn_organized_crime_instance = TornOrganizedCrime.from_json(json)
# print the JSON string representation of the object
print(TornOrganizedCrime.to_json())

# convert the object into a dict
torn_organized_crime_dict = torn_organized_crime_instance.to_dict()
# create an instance of TornOrganizedCrime from a dict
torn_organized_crime_from_dict = TornOrganizedCrime.from_dict(torn_organized_crime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


