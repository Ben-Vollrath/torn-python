# ReportFriendOrFoe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friends** | [**List[ReportFriendOrFoeUser]**](ReportFriendOrFoeUser.md) |  | 
**enemies** | [**List[ReportFriendOrFoeUser]**](ReportFriendOrFoeUser.md) |  | 

## Example

```python
from openapi_client.models.report_friend_or_foe import ReportFriendOrFoe

# TODO update the JSON string below
json = "{}"
# create an instance of ReportFriendOrFoe from a JSON string
report_friend_or_foe_instance = ReportFriendOrFoe.from_json(json)
# print the JSON string representation of the object
print(ReportFriendOrFoe.to_json())

# convert the object into a dict
report_friend_or_foe_dict = report_friend_or_foe_instance.to_dict()
# create an instance of ReportFriendOrFoe from a dict
report_friend_or_foe_from_dict = ReportFriendOrFoe.from_dict(report_friend_or_foe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


