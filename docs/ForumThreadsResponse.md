# ForumThreadsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threads** | [**List[ForumThreadBase]**](ForumThreadBase.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.forum_threads_response import ForumThreadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForumThreadsResponse from a JSON string
forum_threads_response_instance = ForumThreadsResponse.from_json(json)
# print the JSON string representation of the object
print(ForumThreadsResponse.to_json())

# convert the object into a dict
forum_threads_response_dict = forum_threads_response_instance.to_dict()
# create an instance of ForumThreadsResponse from a dict
forum_threads_response_from_dict = ForumThreadsResponse.from_dict(forum_threads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


