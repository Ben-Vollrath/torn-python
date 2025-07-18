# FactionTerritoryWarReportMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**username** | **str** |  | 
**level** | **int** |  | 
**score** | **int** |  | 
**joins** | **int** |  | 
**clears** | **int** |  | 

## Example

```python
from openapi_client.models.faction_territory_war_report_members import FactionTerritoryWarReportMembers

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarReportMembers from a JSON string
faction_territory_war_report_members_instance = FactionTerritoryWarReportMembers.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarReportMembers.to_json())

# convert the object into a dict
faction_territory_war_report_members_dict = faction_territory_war_report_members_instance.to_dict()
# create an instance of FactionTerritoryWarReportMembers from a dict
faction_territory_war_report_members_from_dict = FactionTerritoryWarReportMembers.from_dict(faction_territory_war_report_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


