# UserCrimeDetailsCardSkimmingCardDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recoverable** | **int** |  | 
**recovered** | **int** |  | 
**sold** | **int** |  | 
**lost** | **int** |  | 
**areas** | [**List[UserCrimeDetailsCardSkimmingCardDetailsAreasInner]**](UserCrimeDetailsCardSkimmingCardDetailsAreasInner.md) |  | 

## Example

```python
from openapi_client.models.user_crime_details_card_skimming_card_details import UserCrimeDetailsCardSkimmingCardDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeDetailsCardSkimmingCardDetails from a JSON string
user_crime_details_card_skimming_card_details_instance = UserCrimeDetailsCardSkimmingCardDetails.from_json(json)
# print the JSON string representation of the object
print(UserCrimeDetailsCardSkimmingCardDetails.to_json())

# convert the object into a dict
user_crime_details_card_skimming_card_details_dict = user_crime_details_card_skimming_card_details_instance.to_dict()
# create an instance of UserCrimeDetailsCardSkimmingCardDetails from a dict
user_crime_details_card_skimming_card_details_from_dict = UserCrimeDetailsCardSkimmingCardDetails.from_dict(user_crime_details_card_skimming_card_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


