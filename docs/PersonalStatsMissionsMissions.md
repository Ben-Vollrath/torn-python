# PersonalStatsMissionsMissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missions** | **int** |  | 
**contracts** | [**PersonalStatsMissionsMissionsContracts**](PersonalStatsMissionsMissionsContracts.md) |  | 
**credits** | **int** |  | 

## Example

```python
from openapi_client.models.personal_stats_missions_missions import PersonalStatsMissionsMissions

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsMissionsMissions from a JSON string
personal_stats_missions_missions_instance = PersonalStatsMissionsMissions.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsMissionsMissions.to_json())

# convert the object into a dict
personal_stats_missions_missions_dict = personal_stats_missions_missions_instance.to_dict()
# create an instance of PersonalStatsMissionsMissions from a dict
personal_stats_missions_missions_from_dict = PersonalStatsMissionsMissions.from_dict(personal_stats_missions_missions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


