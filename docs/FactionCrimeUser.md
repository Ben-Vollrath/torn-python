# FactionCrimeUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**outcome** | [**FactionCrimeUserOutcome**](FactionCrimeUserOutcome.md) |  | 
**joined_at** | **int** | The timestamp at which the user joined the slot. | 
**progress** | **float** | Current planning progress on the slot. | 

## Example

```python
from openapi_client.models.faction_crime_user import FactionCrimeUser

# TODO update the JSON string below
json = "{}"
# create an instance of FactionCrimeUser from a JSON string
faction_crime_user_instance = FactionCrimeUser.from_json(json)
# print the JSON string representation of the object
print(FactionCrimeUser.to_json())

# convert the object into a dict
faction_crime_user_dict = faction_crime_user_instance.to_dict()
# create an instance of FactionCrimeUser from a dict
faction_crime_user_from_dict = FactionCrimeUser.from_dict(faction_crime_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


