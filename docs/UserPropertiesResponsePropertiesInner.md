# UserPropertiesResponsePropertiesInner


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
**renter_asked** | [**BasicUser**](BasicUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_properties_response_properties_inner import UserPropertiesResponsePropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserPropertiesResponsePropertiesInner from a JSON string
user_properties_response_properties_inner_instance = UserPropertiesResponsePropertiesInner.from_json(json)
# print the JSON string representation of the object
print(UserPropertiesResponsePropertiesInner.to_json())

# convert the object into a dict
user_properties_response_properties_inner_dict = user_properties_response_properties_inner_instance.to_dict()
# create an instance of UserPropertiesResponsePropertiesInner from a dict
user_properties_response_properties_inner_from_dict = UserPropertiesResponsePropertiesInner.from_dict(user_properties_response_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


