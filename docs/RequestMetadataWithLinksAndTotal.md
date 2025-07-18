# RequestMetadataWithLinksAndTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**RequestLinks**](RequestLinks.md) |  | 
**total** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.request_metadata_with_links_and_total import RequestMetadataWithLinksAndTotal

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMetadataWithLinksAndTotal from a JSON string
request_metadata_with_links_and_total_instance = RequestMetadataWithLinksAndTotal.from_json(json)
# print the JSON string representation of the object
print(RequestMetadataWithLinksAndTotal.to_json())

# convert the object into a dict
request_metadata_with_links_and_total_dict = request_metadata_with_links_and_total_instance.to_dict()
# create an instance of RequestMetadataWithLinksAndTotal from a dict
request_metadata_with_links_and_total_from_dict = RequestMetadataWithLinksAndTotal.from_dict(request_metadata_with_links_and_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


