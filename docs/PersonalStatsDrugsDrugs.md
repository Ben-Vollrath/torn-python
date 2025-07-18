# PersonalStatsDrugsDrugs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cannabis** | **int** |  | 
**ecstasy** | **int** |  | 
**ketamine** | **int** |  | 
**lsd** | **int** |  | 
**opium** | **int** |  | 
**pcp** | **int** |  | 
**shrooms** | **int** |  | 
**speed** | **int** |  | 
**vicodin** | **int** |  | 
**xanax** | **int** |  | 
**total** | **int** |  | 
**overdoses** | **int** |  | 
**rehabilitations** | [**PersonalStatsDrugsDrugsRehabilitations**](PersonalStatsDrugsDrugsRehabilitations.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_drugs_drugs import PersonalStatsDrugsDrugs

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsDrugsDrugs from a JSON string
personal_stats_drugs_drugs_instance = PersonalStatsDrugsDrugs.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsDrugsDrugs.to_json())

# convert the object into a dict
personal_stats_drugs_drugs_dict = personal_stats_drugs_drugs_instance.to_dict()
# create an instance of PersonalStatsDrugsDrugs from a dict
personal_stats_drugs_drugs_from_dict = PersonalStatsDrugsDrugs.from_dict(personal_stats_drugs_drugs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


