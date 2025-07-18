# UserForumPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum_posts** | [**List[ForumPost]**](ForumPost.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.user_forum_posts_response import UserForumPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserForumPostsResponse from a JSON string
user_forum_posts_response_instance = UserForumPostsResponse.from_json(json)
# print the JSON string representation of the object
print(UserForumPostsResponse.to_json())

# convert the object into a dict
user_forum_posts_response_dict = user_forum_posts_response_instance.to_dict()
# create an instance of UserForumPostsResponse from a dict
user_forum_posts_response_from_dict = UserForumPostsResponse.from_dict(user_forum_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


