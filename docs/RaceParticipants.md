# RaceParticipants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum** | **int** |  | 
**maximum** | **int** |  | 
**current** | **int** |  | 

## Example

```python
from openapi_client.models.race_participants import RaceParticipants

# TODO update the JSON string below
json = "{}"
# create an instance of RaceParticipants from a JSON string
race_participants_instance = RaceParticipants.from_json(json)
# print the JSON string representation of the object
print(RaceParticipants.to_json())

# convert the object into a dict
race_participants_dict = race_participants_instance.to_dict()
# create an instance of RaceParticipants from a dict
race_participants_from_dict = RaceParticipants.from_dict(race_participants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


