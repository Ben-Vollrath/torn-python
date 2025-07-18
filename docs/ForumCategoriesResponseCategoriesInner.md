# ForumCategoriesResponseCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**acronym** | **str** |  | 
**threads** | **int** |  | 

## Example

```python
from openapi_client.models.forum_categories_response_categories_inner import ForumCategoriesResponseCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ForumCategoriesResponseCategoriesInner from a JSON string
forum_categories_response_categories_inner_instance = ForumCategoriesResponseCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(ForumCategoriesResponseCategoriesInner.to_json())

# convert the object into a dict
forum_categories_response_categories_inner_dict = forum_categories_response_categories_inner_instance.to_dict()
# create an instance of ForumCategoriesResponseCategoriesInner from a dict
forum_categories_response_categories_inner_from_dict = ForumCategoriesResponseCategoriesInner.from_dict(forum_categories_response_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


