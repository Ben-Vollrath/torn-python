# ForumLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selections** | [**List[ForumSelectionName]**](ForumSelectionName.md) |  | 

## Example

```python
from openapi_client.models.forum_lookup_response import ForumLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForumLookupResponse from a JSON string
forum_lookup_response_instance = ForumLookupResponse.from_json(json)
# print the JSON string representation of the object
print(ForumLookupResponse.to_json())

# convert the object into a dict
forum_lookup_response_dict = forum_lookup_response_instance.to_dict()
# create an instance of ForumLookupResponse from a dict
forum_lookup_response_from_dict = ForumLookupResponse.from_dict(forum_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


