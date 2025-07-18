# ReportAnonymousBounties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounties** | [**List[ReportAnonymousBountiesBountiesInner]**](ReportAnonymousBountiesBountiesInner.md) |  | 

## Example

```python
from openapi_client.models.report_anonymous_bounties import ReportAnonymousBounties

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAnonymousBounties from a JSON string
report_anonymous_bounties_instance = ReportAnonymousBounties.from_json(json)
# print the JSON string representation of the object
print(ReportAnonymousBounties.to_json())

# convert the object into a dict
report_anonymous_bounties_dict = report_anonymous_bounties_instance.to_dict()
# create an instance of ReportAnonymousBounties from a dict
report_anonymous_bounties_from_dict = ReportAnonymousBounties.from_dict(report_anonymous_bounties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


