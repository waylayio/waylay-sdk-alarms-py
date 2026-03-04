# CreateAlarm

To create an alarm, you need to provide the following mandatory inputs.

**Source:** `waylay.services.alarms.models.create_alarm`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the alarm. | 
**text** | **str** | Description of the alarm. | 
**severity** | [**AlarmSeverity**](AlarmSeverity.md) |  | 
**source** | [**IdObject**](IdObject.md) |  | 
**status** | [**AlarmStatus**](AlarmStatus.md) |  | [optional] [default to AlarmStatus.ACTIVE]
**timestamp** | [**ISO8601TimestampOrMillis**](ISO8601TimestampOrMillis.md) |  | [optional] 
**assignee** | **str** | String field to indicate an assignee for the alarm. | [optional] 


## Example

```python
from waylay.services.alarms.models.create_alarm import CreateAlarm

create_alarm = CreateAlarm(
    type=...,
    text=...,
    severity=...,
    source=...,
    status=...,
    timestamp=...,
    assignee=...,
)

# Create from JSON
create_alarm = CreateAlarm.from_json(
    '{ "type": ..., "text": ..., "severity": ..., "source": ..., "status": ..., "timestamp": ..., "assignee": ... }'
)

# Export to dictionary
create_alarm_dict = create_alarm.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


