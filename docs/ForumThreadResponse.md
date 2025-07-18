# ForumThreadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread** | [**ForumThreadExtended**](ForumThreadExtended.md) |  | 

## Example

```python
from openapi_client.models.forum_thread_response import ForumThreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForumThreadResponse from a JSON string
forum_thread_response_instance = ForumThreadResponse.from_json(json)
# print the JSON string representation of the object
print(ForumThreadResponse.to_json())

# convert the object into a dict
forum_thread_response_dict = forum_thread_response_instance.to_dict()
# create an instance of ForumThreadResponse from a dict
forum_thread_response_from_dict = ForumThreadResponse.from_dict(forum_thread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


