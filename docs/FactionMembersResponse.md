# FactionMembersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[FactionMember]**](FactionMember.md) |  | 

## Example

```python
from openapi_client.models.faction_members_response import FactionMembersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionMembersResponse from a JSON string
faction_members_response_instance = FactionMembersResponse.from_json(json)
# print the JSON string representation of the object
print(FactionMembersResponse.to_json())

# convert the object into a dict
faction_members_response_dict = faction_members_response_instance.to_dict()
# create an instance of FactionMembersResponse from a dict
faction_members_response_from_dict = FactionMembersResponse.from_dict(faction_members_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


