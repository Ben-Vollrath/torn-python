# RevivesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revives** | [**List[Revive]**](Revive.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.revives_response import RevivesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RevivesResponse from a JSON string
revives_response_instance = RevivesResponse.from_json(json)
# print the JSON string representation of the object
print(RevivesResponse.to_json())

# convert the object into a dict
revives_response_dict = revives_response_instance.to_dict()
# create an instance of RevivesResponse from a dict
revives_response_from_dict = RevivesResponse.from_dict(revives_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


