# UserCrimeDetailsCardSkimming


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_details** | [**UserCrimeDetailsCardSkimmingCardDetails**](UserCrimeDetailsCardSkimmingCardDetails.md) |  | 
**skimmers** | [**UserCrimeDetailsCardSkimmingSkimmers**](UserCrimeDetailsCardSkimmingSkimmers.md) |  | 

## Example

```python
from openapi_client.models.user_crime_details_card_skimming import UserCrimeDetailsCardSkimming

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeDetailsCardSkimming from a JSON string
user_crime_details_card_skimming_instance = UserCrimeDetailsCardSkimming.from_json(json)
# print the JSON string representation of the object
print(UserCrimeDetailsCardSkimming.to_json())

# convert the object into a dict
user_crime_details_card_skimming_dict = user_crime_details_card_skimming_instance.to_dict()
# create an instance of UserCrimeDetailsCardSkimming from a dict
user_crime_details_card_skimming_from_dict = UserCrimeDetailsCardSkimming.from_dict(user_crime_details_card_skimming_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


