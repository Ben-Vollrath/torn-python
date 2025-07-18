# FactionNewsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**news** | [**List[FactionNews]**](FactionNews.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.faction_news_response import FactionNewsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionNewsResponse from a JSON string
faction_news_response_instance = FactionNewsResponse.from_json(json)
# print the JSON string representation of the object
print(FactionNewsResponse.to_json())

# convert the object into a dict
faction_news_response_dict = faction_news_response_instance.to_dict()
# create an instance of FactionNewsResponse from a dict
faction_news_response_from_dict = FactionNewsResponse.from_dict(faction_news_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


