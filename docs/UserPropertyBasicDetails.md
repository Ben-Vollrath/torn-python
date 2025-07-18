# UserPropertyBasicDetails


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

## Example

```python
from openapi_client.models.user_property_basic_details import UserPropertyBasicDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserPropertyBasicDetails from a JSON string
user_property_basic_details_instance = UserPropertyBasicDetails.from_json(json)
# print the JSON string representation of the object
print(UserPropertyBasicDetails.to_json())

# convert the object into a dict
user_property_basic_details_dict = user_property_basic_details_instance.to_dict()
# create an instance of UserPropertyBasicDetails from a dict
user_property_basic_details_from_dict = UserPropertyBasicDetails.from_dict(user_property_basic_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


