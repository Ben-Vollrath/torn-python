# ForumSubscribedThread


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**forum_id** | **int** |  | 
**author** | [**ForumThreadAuthor**](ForumThreadAuthor.md) |  | 
**title** | **str** |  | 
**posts** | [**ForumSubscribedThreadPostsCount**](ForumSubscribedThreadPostsCount.md) |  | 

## Example

```python
from openapi_client.models.forum_subscribed_thread import ForumSubscribedThread

# TODO update the JSON string below
json = "{}"
# create an instance of ForumSubscribedThread from a JSON string
forum_subscribed_thread_instance = ForumSubscribedThread.from_json(json)
# print the JSON string representation of the object
print(ForumSubscribedThread.to_json())

# convert the object into a dict
forum_subscribed_thread_dict = forum_subscribed_thread_instance.to_dict()
# create an instance of ForumSubscribedThread from a dict
forum_subscribed_thread_from_dict = ForumSubscribedThread.from_dict(forum_subscribed_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


