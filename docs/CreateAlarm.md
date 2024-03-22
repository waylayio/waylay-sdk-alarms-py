# CreateAlarm

To create an alarm, you need to provide the following mandatory inputs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the alarm. | 
**text** | **str** | Description of the alarm. | 
**severity** | [**AlarmSeverity**](AlarmSeverity.md) |  | 
**source** | [**IdObject**](IdObject.md) |  | 
**status** | [**AlarmStatus**](AlarmStatus.md) |  | [optional] 
**timestamp** | [**SO8601TimestampOrMillis**](SO8601TimestampOrMillis.md) |  | [optional] 
**assignee** | **str** | String field to indicate an assignee for the alarm. | [optional] 

## Example

```python
from waylay.services.alarms.models.create_alarm import CreateAlarm

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlarm from a JSON string
create_alarm_instance = CreateAlarm.from_json(json)
# print the JSON string representation of the object
print CreateAlarm.to_json()

# convert the object into a dict
create_alarm_dict = create_alarm_instance.to_dict()
# create an instance of CreateAlarm from a dict
create_alarm_form_dict = create_alarm.from_dict(create_alarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


