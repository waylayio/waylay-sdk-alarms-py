# CloudAlarmEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**source** | **object** |  | [optional] 
**subject** | **str** |  | 
**type** | **str** |  | [optional] 
**data** | [**AlarmEvent**](AlarmEvent.md) |  | [optional] 
**time** | **datetime** |  | 

## Example

```python
from waylay.services.alarms.models.cloud_alarm_event import CloudAlarmEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CloudAlarmEvent from a JSON string
cloud_alarm_event_instance = CloudAlarmEvent.from_json(json)
# print the JSON string representation of the object
print CloudAlarmEvent.to_json()

# convert the object into a dict
cloud_alarm_event_dict = cloud_alarm_event_instance.to_dict()
# create an instance of CloudAlarmEvent from a dict
cloud_alarm_event_form_dict = cloud_alarm_event.from_dict(cloud_alarm_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


