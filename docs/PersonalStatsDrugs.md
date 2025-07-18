# PersonalStatsDrugs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drugs** | [**PersonalStatsDrugsDrugs**](PersonalStatsDrugsDrugs.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_drugs import PersonalStatsDrugs

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsDrugs from a JSON string
personal_stats_drugs_instance = PersonalStatsDrugs.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsDrugs.to_json())

# convert the object into a dict
personal_stats_drugs_dict = personal_stats_drugs_instance.to_dict()
# create an instance of PersonalStatsDrugs from a dict
personal_stats_drugs_from_dict = PersonalStatsDrugs.from_dict(personal_stats_drugs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


