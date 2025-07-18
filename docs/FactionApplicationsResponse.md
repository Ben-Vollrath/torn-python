# FactionApplicationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[FactionApplication]**](FactionApplication.md) |  | 

## Example

```python
from openapi_client.models.faction_applications_response import FactionApplicationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionApplicationsResponse from a JSON string
faction_applications_response_instance = FactionApplicationsResponse.from_json(json)
# print the JSON string representation of the object
print(FactionApplicationsResponse.to_json())

# convert the object into a dict
faction_applications_response_dict = faction_applications_response_instance.to_dict()
# create an instance of FactionApplicationsResponse from a dict
faction_applications_response_from_dict = FactionApplicationsResponse.from_dict(faction_applications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


