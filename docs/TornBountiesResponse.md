# TornBountiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounties** | [**List[Bounty]**](Bounty.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.torn_bounties_response import TornBountiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornBountiesResponse from a JSON string
torn_bounties_response_instance = TornBountiesResponse.from_json(json)
# print the JSON string representation of the object
print(TornBountiesResponse.to_json())

# convert the object into a dict
torn_bounties_response_dict = torn_bounties_response_instance.to_dict()
# create an instance of TornBountiesResponse from a dict
torn_bounties_response_from_dict = TornBountiesResponse.from_dict(torn_bounties_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


