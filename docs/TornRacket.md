# TornRacket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**level** | **int** |  | 
**description** | **str** |  | 
**reward** | [**TornRacketReward**](TornRacketReward.md) |  | 
**created_at** | **int** |  | 
**changed_at** | **int** |  | 

## Example

```python
from openapi_client.models.torn_racket import TornRacket

# TODO update the JSON string below
json = "{}"
# create an instance of TornRacket from a JSON string
torn_racket_instance = TornRacket.from_json(json)
# print the JSON string representation of the object
print(TornRacket.to_json())

# convert the object into a dict
torn_racket_dict = torn_racket_instance.to_dict()
# create an instance of TornRacket from a dict
torn_racket_from_dict = TornRacket.from_dict(torn_racket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


