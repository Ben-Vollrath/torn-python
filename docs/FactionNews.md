# FactionNews


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**timestamp** | **int** |  | 

## Example

```python
from openapi_client.models.faction_news import FactionNews

# TODO update the JSON string below
json = "{}"
# create an instance of FactionNews from a JSON string
faction_news_instance = FactionNews.from_json(json)
# print the JSON string representation of the object
print(FactionNews.to_json())

# convert the object into a dict
faction_news_dict = faction_news_instance.to_dict()
# create an instance of FactionNews from a dict
faction_news_from_dict = FactionNews.from_dict(faction_news_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


