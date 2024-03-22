# AlarmEventAlarm

Summary representation of an alarm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique alarm identifier. | 
**tenant_id** | **str** |  | 
**creation_time** | **datetime** |  | 
**type** | **str** | Type of the alarm. | 
**text** | **str** | Description of the alarm. | 
**timestamp** | **datetime** |  | 
**source** | [**IdObject**](IdObject.md) |  | 
**severity** | [**AlarmSeverity**](AlarmSeverity.md) |  | 
**status** | [**AlarmStatus**](AlarmStatus.md) |  | 
**count** | **int** |  | 

## Example

```python
from waylay.services.alarms.models.alarm_event_alarm import AlarmEventAlarm

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmEventAlarm from a JSON string
alarm_event_alarm_instance = AlarmEventAlarm.from_json(json)
# print the JSON string representation of the object
print AlarmEventAlarm.to_json()

# convert the object into a dict
alarm_event_alarm_dict = alarm_event_alarm_instance.to_dict()
# create an instance of AlarmEventAlarm from a dict
alarm_event_alarm_form_dict = alarm_event_alarm.from_dict(alarm_event_alarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


