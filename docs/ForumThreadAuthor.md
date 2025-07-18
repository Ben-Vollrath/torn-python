# ForumThreadAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**username** | **str** |  | 
**karma** | **int** |  | 

## Example

```python
from openapi_client.models.forum_thread_author import ForumThreadAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of ForumThreadAuthor from a JSON string
forum_thread_author_instance = ForumThreadAuthor.from_json(json)
# print the JSON string representation of the object
print(ForumThreadAuthor.to_json())

# convert the object into a dict
forum_thread_author_dict = forum_thread_author_instance.to_dict()
# create an instance of ForumThreadAuthor from a dict
forum_thread_author_from_dict = ForumThreadAuthor.from_dict(forum_thread_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


