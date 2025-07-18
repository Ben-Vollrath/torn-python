# RevivesFullResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revives** | [**List[ReviveSimplified]**](ReviveSimplified.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.revives_full_response import RevivesFullResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RevivesFullResponse from a JSON string
revives_full_response_instance = RevivesFullResponse.from_json(json)
# print the JSON string representation of the object
print(RevivesFullResponse.to_json())

# convert the object into a dict
revives_full_response_dict = revives_full_response_instance.to_dict()
# create an instance of RevivesFullResponse from a dict
revives_full_response_from_dict = RevivesFullResponse.from_dict(revives_full_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


