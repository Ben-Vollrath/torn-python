# AttackLogSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** | Name of the participant, could be null in stealthed attacks. | 
**hits** | **int** |  | 
**misses** | **int** |  | 
**damage** | **int** |  | 

## Example

```python
from openapi_client.models.attack_log_summary import AttackLogSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AttackLogSummary from a JSON string
attack_log_summary_instance = AttackLogSummary.from_json(json)
# print the JSON string representation of the object
print(AttackLogSummary.to_json())

# convert the object into a dict
attack_log_summary_dict = attack_log_summary_instance.to_dict()
# create an instance of AttackLogSummary from a dict
attack_log_summary_from_dict = AttackLogSummary.from_dict(attack_log_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


