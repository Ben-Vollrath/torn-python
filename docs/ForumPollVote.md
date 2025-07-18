# ForumPollVote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** |  | 
**votes** | **int** |  | 

## Example

```python
from openapi_client.models.forum_poll_vote import ForumPollVote

# TODO update the JSON string below
json = "{}"
# create an instance of ForumPollVote from a JSON string
forum_poll_vote_instance = ForumPollVote.from_json(json)
# print the JSON string representation of the object
print(ForumPollVote.to_json())

# convert the object into a dict
forum_poll_vote_dict = forum_poll_vote_instance.to_dict()
# create an instance of ForumPollVote from a dict
forum_poll_vote_from_dict = ForumPollVote.from_dict(forum_poll_vote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


