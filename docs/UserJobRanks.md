# UserJobRanks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**army** | [**JobPositionArmyEnum**](JobPositionArmyEnum.md) |  | 
**grocer** | [**JobPositionGrocerEnum**](JobPositionGrocerEnum.md) |  | 
**casino** | [**JobPositionCasinoEnum**](JobPositionCasinoEnum.md) |  | 
**medical** | [**JobPositionMedicalEnum**](JobPositionMedicalEnum.md) |  | 
**law** | [**JobPositionLawEnum**](JobPositionLawEnum.md) |  | 
**education** | [**JobPositionEducationEnum**](JobPositionEducationEnum.md) |  | 

## Example

```python
from openapi_client.models.user_job_ranks import UserJobRanks

# TODO update the JSON string below
json = "{}"
# create an instance of UserJobRanks from a JSON string
user_job_ranks_instance = UserJobRanks.from_json(json)
# print the JSON string representation of the object
print(UserJobRanks.to_json())

# convert the object into a dict
user_job_ranks_dict = user_job_ranks_instance.to_dict()
# create an instance of UserJobRanks from a dict
user_job_ranks_from_dict = UserJobRanks.from_dict(user_job_ranks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


