# ReportCompanyFinancials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **int** |  | 
**employees** | **int** |  | 
**wages** | [**ReportCompanyFinancialsWages**](ReportCompanyFinancialsWages.md) |  | 

## Example

```python
from openapi_client.models.report_company_financials import ReportCompanyFinancials

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCompanyFinancials from a JSON string
report_company_financials_instance = ReportCompanyFinancials.from_json(json)
# print the JSON string representation of the object
print(ReportCompanyFinancials.to_json())

# convert the object into a dict
report_company_financials_dict = report_company_financials_instance.to_dict()
# create an instance of ReportCompanyFinancials from a dict
report_company_financials_from_dict = ReportCompanyFinancials.from_dict(report_company_financials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


