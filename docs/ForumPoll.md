# ForumPoll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | 
**answers_count** | **int** |  | 
**answers** | [**List[ForumPollVote]**](ForumPollVote.md) |  | 

## Example

```python
from openapi_client.models.forum_poll import ForumPoll

# TODO update the JSON string below
json = "{}"
# create an instance of ForumPoll from a JSON string
forum_poll_instance = ForumPoll.from_json(json)
# print the JSON string representation of the object
print(ForumPoll.to_json())

# convert the object into a dict
forum_poll_dict = forum_poll_instance.to_dict()
# create an instance of ForumPoll from a dict
forum_poll_from_dict = ForumPoll.from_dict(forum_poll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


