# RequestMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**RequestLinks**](RequestLinks.md) |  | 

## Example

```python
from openapi_client.models.request_metadata import RequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMetadata from a JSON string
request_metadata_instance = RequestMetadata.from_json(json)
# print the JSON string representation of the object
print(RequestMetadata.to_json())

# convert the object into a dict
request_metadata_dict = request_metadata_instance.to_dict()
# create an instance of RequestMetadata from a dict
request_metadata_from_dict = RequestMetadata.from_dict(request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


