# FactionCrimeSlotItemRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**is_reusable** | **bool** | Shows if the item is reusable or consumed during the crime. | 
**is_available** | **bool** | Shows if user has the required item. | 

## Example

```python
from openapi_client.models.faction_crime_slot_item_requirement import FactionCrimeSlotItemRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of FactionCrimeSlotItemRequirement from a JSON string
faction_crime_slot_item_requirement_instance = FactionCrimeSlotItemRequirement.from_json(json)
# print the JSON string representation of the object
print(FactionCrimeSlotItemRequirement.to_json())

# convert the object into a dict
faction_crime_slot_item_requirement_dict = faction_crime_slot_item_requirement_instance.to_dict()
# create an instance of FactionCrimeSlotItemRequirement from a dict
faction_crime_slot_item_requirement_from_dict = FactionCrimeSlotItemRequirement.from_dict(faction_crime_slot_item_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


