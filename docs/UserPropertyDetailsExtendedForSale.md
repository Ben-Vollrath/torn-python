# UserPropertyDetailsExtendedForSale


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

## Example

```python
from openapi_client.models.user_property_details_extended_for_sale import UserPropertyDetailsExtendedForSale

# TODO update the JSON string below
json = "{}"
# create an instance of UserPropertyDetailsExtendedForSale from a JSON string
user_property_details_extended_for_sale_instance = UserPropertyDetailsExtendedForSale.from_json(json)
# print the JSON string representation of the object
print(UserPropertyDetailsExtendedForSale.to_json())

# convert the object into a dict
user_property_details_extended_for_sale_dict = user_property_details_extended_for_sale_instance.to_dict()
# create an instance of UserPropertyDetailsExtendedForSale from a dict
user_property_details_extended_for_sale_from_dict = UserPropertyDetailsExtendedForSale.from_dict(user_property_details_extended_for_sale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


