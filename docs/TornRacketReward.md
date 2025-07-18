# TornRacketReward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TornRacketType**](TornRacketType.md) |  | 
**quantity** | **int** |  | 
**id** | **int** |  | 

## Example

```python
from openapi_client.models.torn_racket_reward import TornRacketReward

# TODO update the JSON string below
json = "{}"
# create an instance of TornRacketReward from a JSON string
torn_racket_reward_instance = TornRacketReward.from_json(json)
# print the JSON string representation of the object
print(TornRacketReward.to_json())

# convert the object into a dict
torn_racket_reward_dict = torn_racket_reward_instance.to_dict()
# create an instance of TornRacketReward from a dict
torn_racket_reward_from_dict = TornRacketReward.from_dict(torn_racket_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


