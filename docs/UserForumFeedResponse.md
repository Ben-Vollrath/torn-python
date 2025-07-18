# UserForumFeedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum_feed** | [**List[ForumFeed]**](ForumFeed.md) |  | 

## Example

```python
from openapi_client.models.user_forum_feed_response import UserForumFeedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserForumFeedResponse from a JSON string
user_forum_feed_response_instance = UserForumFeedResponse.from_json(json)
# print the JSON string representation of the object
print(UserForumFeedResponse.to_json())

# convert the object into a dict
user_forum_feed_response_dict = user_forum_feed_response_instance.to_dict()
# create an instance of UserForumFeedResponse from a dict
user_forum_feed_response_from_dict = UserForumFeedResponse.from_dict(user_forum_feed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


