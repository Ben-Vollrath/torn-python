# UserPropertyDetailsExtendedRented


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**owner** | [**BasicUser**](BasicUser.md) |  | 
**var_property** | [**BasicProperty**](BasicProperty.md) |  | 
**happy** | **int** |  | 
**upkeep** | [**UserPropertyBasicDetailsUpkeep**](UserPropertyBasicDetailsUpkeep.md) |  | 
**market_price** | **int** |  | 
**modifications** | [**List[PropertyModificationEnum]**](PropertyModificationEnum.md) |  | 
**staff** | [**List[UserPropertyBasicDetailsStaffInner]**](UserPropertyBasicDetailsStaffInner.md) |  | 
**used_by** | [**List[BasicUser]**](BasicUser.md) |  | 
**status** | **str** |  | 
**cost** | **int** |  | 
**cost_per_day** | **int** |  | 
**rental_period** | **int** |  | 
**rental_period_remaining** | **int** |  | 

## Example

```python
from openapi_client.models.user_property_details_extended_rented import UserPropertyDetailsExtendedRented

# TODO update the JSON string below
json = "{}"
# create an instance of UserPropertyDetailsExtendedRented from a JSON string
user_property_details_extended_rented_instance = UserPropertyDetailsExtendedRented.from_json(json)
# print the JSON string representation of the object
print(UserPropertyDetailsExtendedRented.to_json())

# convert the object into a dict
user_property_details_extended_rented_dict = user_property_details_extended_rented_instance.to_dict()
# create an instance of UserPropertyDetailsExtendedRented from a dict
user_property_details_extended_rented_from_dict = UserPropertyDetailsExtendedRented.from_dict(user_property_details_extended_rented_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


