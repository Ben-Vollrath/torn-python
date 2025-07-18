# RequestMetadataWithLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**RequestLinks**](RequestLinks.md) |  | 

## Example

```python
from openapi_client.models.request_metadata_with_links import RequestMetadataWithLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMetadataWithLinks from a JSON string
request_metadata_with_links_instance = RequestMetadataWithLinks.from_json(json)
# print the JSON string representation of the object
print(RequestMetadataWithLinks.to_json())

# convert the object into a dict
request_metadata_with_links_dict = request_metadata_with_links_instance.to_dict()
# create an instance of RequestMetadataWithLinks from a dict
request_metadata_with_links_from_dict = RequestMetadataWithLinks.from_dict(request_metadata_with_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


