# UserForumFriendsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum_friends** | [**List[ForumFeed]**](ForumFeed.md) |  | 

## Example

```python
from openapi_client.models.user_forum_friends_response import UserForumFriendsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserForumFriendsResponse from a JSON string
user_forum_friends_response_instance = UserForumFriendsResponse.from_json(json)
# print the JSON string representation of the object
print(UserForumFriendsResponse.to_json())

# convert the object into a dict
user_forum_friends_response_dict = user_forum_friends_response_instance.to_dict()
# create an instance of UserForumFriendsResponse from a dict
user_forum_friends_response_from_dict = UserForumFriendsResponse.from_dict(user_forum_friends_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


