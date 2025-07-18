# TornItemArmorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coverage** | [**List[TornItemArmorCoverage]**](TornItemArmorCoverage.md) |  | 
**base_stats** | [**TornItemBaseStats**](TornItemBaseStats.md) |  | 

## Example

```python
from openapi_client.models.torn_item_armor_details import TornItemArmorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TornItemArmorDetails from a JSON string
torn_item_armor_details_instance = TornItemArmorDetails.from_json(json)
# print the JSON string representation of the object
print(TornItemArmorDetails.to_json())

# convert the object into a dict
torn_item_armor_details_dict = torn_item_armor_details_instance.to_dict()
# create an instance of TornItemArmorDetails from a dict
torn_item_armor_details_from_dict = TornItemArmorDetails.from_dict(torn_item_armor_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


