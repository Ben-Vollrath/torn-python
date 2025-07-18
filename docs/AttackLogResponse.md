# AttackLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacklog** | [**AttackLogResponseAttacklog**](AttackLogResponseAttacklog.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from openapi_client.models.attack_log_response import AttackLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttackLogResponse from a JSON string
attack_log_response_instance = AttackLogResponse.from_json(json)
# print the JSON string representation of the object
print(AttackLogResponse.to_json())

# convert the object into a dict
attack_log_response_dict = attack_log_response_instance.to_dict()
# create an instance of AttackLogResponse from a dict
attack_log_response_from_dict = AttackLogResponse.from_dict(attack_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


