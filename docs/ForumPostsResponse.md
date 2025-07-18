# ForumPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | [**List[ForumPost]**](ForumPost.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.forum_posts_response import ForumPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForumPostsResponse from a JSON string
forum_posts_response_instance = ForumPostsResponse.from_json(json)
# print the JSON string representation of the object
print(ForumPostsResponse.to_json())

# convert the object into a dict
forum_posts_response_dict = forum_posts_response_instance.to_dict()
# create an instance of ForumPostsResponse from a dict
forum_posts_response_from_dict = ForumPostsResponse.from_dict(forum_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


