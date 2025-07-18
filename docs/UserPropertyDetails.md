# UserPropertyDetails


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

## Example

```python
from openapi_client.models.user_property_details import UserPropertyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserPropertyDetails from a JSON string
user_property_details_instance = UserPropertyDetails.from_json(json)
# print the JSON string representation of the object
print(UserPropertyDetails.to_json())

# convert the object into a dict
user_property_details_dict = user_property_details_instance.to_dict()
# create an instance of UserPropertyDetails from a dict
user_property_details_from_dict = UserPropertyDetails.from_dict(user_property_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


