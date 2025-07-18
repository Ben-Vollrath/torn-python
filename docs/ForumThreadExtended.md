# ForumThreadExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**forum_id** | **int** |  | 
**posts** | **int** |  | 
**rating** | **int** |  | 
**views** | **int** | Total number of times players have opened this thread. | 
**author** | [**ForumThreadAuthor**](ForumThreadAuthor.md) |  | 
**last_poster** | [**ForumThreadAuthor**](ForumThreadAuthor.md) |  | 
**first_post_time** | **int** |  | 
**last_post_time** | **int** |  | 
**has_poll** | **bool** |  | 
**is_locked** | **bool** |  | 
**is_sticky** | **bool** |  | 
**content** | **str** |  | 
**content_raw** | **str** |  | 
**poll** | [**ForumPoll**](ForumPoll.md) |  | 

## Example

```python
from openapi_client.models.forum_thread_extended import ForumThreadExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ForumThreadExtended from a JSON string
forum_thread_extended_instance = ForumThreadExtended.from_json(json)
# print the JSON string representation of the object
print(ForumThreadExtended.to_json())

# convert the object into a dict
forum_thread_extended_dict = forum_thread_extended_instance.to_dict()
# create an instance of ForumThreadExtended from a dict
forum_thread_extended_from_dict = ForumThreadExtended.from_dict(forum_thread_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


