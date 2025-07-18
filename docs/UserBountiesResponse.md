# UserBountiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounties** | [**List[Bounty]**](Bounty.md) |  | 

## Example

```python
from openapi_client.models.user_bounties_response import UserBountiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserBountiesResponse from a JSON string
user_bounties_response_instance = UserBountiesResponse.from_json(json)
# print the JSON string representation of the object
print(UserBountiesResponse.to_json())

# convert the object into a dict
user_bounties_response_dict = user_bounties_response_instance.to_dict()
# create an instance of UserBountiesResponse from a dict
user_bounties_response_from_dict = UserBountiesResponse.from_dict(user_bounties_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


