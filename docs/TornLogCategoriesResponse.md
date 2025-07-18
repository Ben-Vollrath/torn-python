# TornLogCategoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logcategories** | [**List[TornLogCategory]**](TornLogCategory.md) |  | 

## Example

```python
from openapi_client.models.torn_log_categories_response import TornLogCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TornLogCategoriesResponse from a JSON string
torn_log_categories_response_instance = TornLogCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(TornLogCategoriesResponse.to_json())

# convert the object into a dict
torn_log_categories_response_dict = torn_log_categories_response_instance.to_dict()
# create an instance of TornLogCategoriesResponse from a dict
torn_log_categories_response_from_dict = TornLogCategoriesResponse.from_dict(torn_log_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


