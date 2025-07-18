# PersonalStatsItemsItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | [**PersonalStatsItemsItemsFound**](PersonalStatsItemsItemsFound.md) |  | 
**trashed** | **int** |  | 
**used** | [**PersonalStatsItemsItemsUsed**](PersonalStatsItemsItemsUsed.md) |  | 
**viruses_coded** | **int** |  | 

## Example

```python
from openapi_client.models.personal_stats_items_items import PersonalStatsItemsItems

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsItemsItems from a JSON string
personal_stats_items_items_instance = PersonalStatsItemsItems.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsItemsItems.to_json())

# convert the object into a dict
personal_stats_items_items_dict = personal_stats_items_items_instance.to_dict()
# create an instance of PersonalStatsItemsItems from a dict
personal_stats_items_items_from_dict = PersonalStatsItemsItems.from_dict(personal_stats_items_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


