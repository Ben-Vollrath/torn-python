# ForumFeed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **int** |  | 
**post_id** | **int** |  | 
**user** | [**ForumThreadAuthor**](ForumThreadAuthor.md) |  | 
**title** | **str** |  | 
**text** | **str** |  | 
**timestamp** | **int** |  | 
**is_seen** | **bool** |  | 
**type** | [**ForumFeedTypeEnum**](ForumFeedTypeEnum.md) |  | 

## Example

```python
from openapi_client.models.forum_feed import ForumFeed

# TODO update the JSON string below
json = "{}"
# create an instance of ForumFeed from a JSON string
forum_feed_instance = ForumFeed.from_json(json)
# print the JSON string representation of the object
print(ForumFeed.to_json())

# convert the object into a dict
forum_feed_dict = forum_feed_instance.to_dict()
# create an instance of ForumFeed from a dict
forum_feed_from_dict = ForumFeed.from_dict(forum_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


