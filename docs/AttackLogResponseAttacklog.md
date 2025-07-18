# AttackLogResponseAttacklog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | [**List[AttackLog]**](AttackLog.md) |  | 
**summary** | [**List[AttackLogSummary]**](AttackLogSummary.md) |  | 

## Example

```python
from openapi_client.models.attack_log_response_attacklog import AttackLogResponseAttacklog

# TODO update the JSON string below
json = "{}"
# create an instance of AttackLogResponseAttacklog from a JSON string
attack_log_response_attacklog_instance = AttackLogResponseAttacklog.from_json(json)
# print the JSON string representation of the object
print(AttackLogResponseAttacklog.to_json())

# convert the object into a dict
attack_log_response_attacklog_dict = attack_log_response_attacklog_instance.to_dict()
# create an instance of AttackLogResponseAttacklog from a dict
attack_log_response_attacklog_from_dict = AttackLogResponseAttacklog.from_dict(attack_log_response_attacklog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


