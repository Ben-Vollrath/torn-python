# UserJobRanksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobranks** | [**UserJobRanks**](UserJobRanks.md) |  | 

## Example

```python
from openapi_client.models.user_job_ranks_response import UserJobRanksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserJobRanksResponse from a JSON string
user_job_ranks_response_instance = UserJobRanksResponse.from_json(json)
# print the JSON string representation of the object
print(UserJobRanksResponse.to_json())

# convert the object into a dict
user_job_ranks_response_dict = user_job_ranks_response_instance.to_dict()
# create an instance of UserJobRanksResponse from a dict
user_job_ranks_response_from_dict = UserJobRanksResponse.from_dict(user_job_ranks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


