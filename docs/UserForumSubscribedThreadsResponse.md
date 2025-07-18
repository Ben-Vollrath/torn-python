# UserForumSubscribedThreadsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum_subscribed_threads** | [**List[ForumSubscribedThread]**](ForumSubscribedThread.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_forum_subscribed_threads_response import UserForumSubscribedThreadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserForumSubscribedThreadsResponse from a JSON string
user_forum_subscribed_threads_response_instance = UserForumSubscribedThreadsResponse.from_json(json)
# print the JSON string representation of the object
print(UserForumSubscribedThreadsResponse.to_json())

# convert the object into a dict
user_forum_subscribed_threads_response_dict = user_forum_subscribed_threads_response_instance.to_dict()
# create an instance of UserForumSubscribedThreadsResponse from a dict
user_forum_subscribed_threads_response_from_dict = UserForumSubscribedThreadsResponse.from_dict(user_forum_subscribed_threads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


