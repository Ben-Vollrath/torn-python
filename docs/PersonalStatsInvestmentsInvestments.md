# PersonalStatsInvestmentsInvestments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank** | [**PersonalStatsInvestmentsInvestmentsBank**](PersonalStatsInvestmentsInvestmentsBank.md) |  | 
**stocks** | [**PersonalStatsInvestmentsInvestmentsStocks**](PersonalStatsInvestmentsInvestmentsStocks.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_investments_investments import PersonalStatsInvestmentsInvestments

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsInvestmentsInvestments from a JSON string
personal_stats_investments_investments_instance = PersonalStatsInvestmentsInvestments.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsInvestmentsInvestments.to_json())

# convert the object into a dict
personal_stats_investments_investments_dict = personal_stats_investments_investments_instance.to_dict()
# create an instance of PersonalStatsInvestmentsInvestments from a dict
personal_stats_investments_investments_from_dict = PersonalStatsInvestmentsInvestments.from_dict(personal_stats_investments_investments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


