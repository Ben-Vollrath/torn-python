# PersonalStatsItemsPopularItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | [**PersonalStatsItemsPopularItemsFound**](PersonalStatsItemsPopularItemsFound.md) |  | 
**used** | [**PersonalStatsItemsItemsUsed**](PersonalStatsItemsItemsUsed.md) |  | 

## Example

```python
from openapi_client.models.personal_stats_items_popular_items import PersonalStatsItemsPopularItems

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsItemsPopularItems from a JSON string
personal_stats_items_popular_items_instance = PersonalStatsItemsPopularItems.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsItemsPopularItems.to_json())

# convert the object into a dict
personal_stats_items_popular_items_dict = personal_stats_items_popular_items_instance.to_dict()
# create an instance of PersonalStatsItemsPopularItems from a dict
personal_stats_items_popular_items_from_dict = PersonalStatsItemsPopularItems.from_dict(personal_stats_items_popular_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


