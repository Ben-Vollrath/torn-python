# ForumPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**thread_id** | **int** |  | 
**author** | [**ForumThreadAuthor**](ForumThreadAuthor.md) |  | 
**is_legacy** | **bool** | Indicates whether post was made using the old formatting engine which doesn&#39;t use HTML. | 
**is_topic** | **bool** |  | 
**is_edited** | **bool** |  | 
**is_pinned** | **bool** |  | 
**created_time** | **int** |  | 
**edited_by** | **int** |  | 
**has_quote** | **bool** |  | 
**quoted_post_id** | **int** |  | 
**content** | **str** | depending on the input &#39;cat&#39; parameter, this will either return raw value (with HTML) or plain text. Legacy posts are returned as is, they can&#39;t be stripped of tags. | 
**likes** | **int** |  | 
**dislikes** | **int** |  | 

## Example

```python
from openapi_client.models.forum_post import ForumPost

# TODO update the JSON string below
json = "{}"
# create an instance of ForumPost from a JSON string
forum_post_instance = ForumPost.from_json(json)
# print the JSON string representation of the object
print(ForumPost.to_json())

# convert the object into a dict
forum_post_dict = forum_post_instance.to_dict()
# create an instance of ForumPost from a dict
forum_post_from_dict = ForumPost.from_dict(forum_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


