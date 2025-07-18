# ForumCategoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[ForumCategoriesResponseCategoriesInner]**](ForumCategoriesResponseCategoriesInner.md) |  | 

## Example

```python
from openapi_client.models.forum_categories_response import ForumCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForumCategoriesResponse from a JSON string
forum_categories_response_instance = ForumCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(ForumCategoriesResponse.to_json())

# convert the object into a dict
forum_categories_response_dict = forum_categories_response_instance.to_dict()
# create an instance of ForumCategoriesResponse from a dict
forum_categories_response_from_dict = ForumCategoriesResponse.from_dict(forum_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


