# PersonalStatsCommunicationCommunication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mails_sent** | [**PersonalStatsCommunicationCommunicationMailsSent**](PersonalStatsCommunicationCommunicationMailsSent.md) |  | 
**classified_ads** | **int** |  | 
**personals** | **int** |  | 

## Example

```python
from openapi_client.models.personal_stats_communication_communication import PersonalStatsCommunicationCommunication

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalStatsCommunicationCommunication from a JSON string
personal_stats_communication_communication_instance = PersonalStatsCommunicationCommunication.from_json(json)
# print the JSON string representation of the object
print(PersonalStatsCommunicationCommunication.to_json())

# convert the object into a dict
personal_stats_communication_communication_dict = personal_stats_communication_communication_instance.to_dict()
# create an instance of PersonalStatsCommunicationCommunication from a dict
personal_stats_communication_communication_from_dict = PersonalStatsCommunicationCommunication.from_dict(personal_stats_communication_communication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


