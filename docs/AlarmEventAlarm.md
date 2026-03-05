# AlarmEventAlarm

Summary representation of an alarm.

**Source:** `waylay.services.alarms.models.alarm_event_alarm`




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
**status** | [**AlarmStatus**](AlarmStatus.md) |  | [default to AlarmStatus.ACTIVE]
**count** | **int** |  | 


## Example

```python
from waylay.services.alarms.models.alarm_event_alarm import AlarmEventAlarm

alarm_event_alarm = AlarmEventAlarm(
    id=...,
    tenant_id=...,
    creation_time=...,
    type=...,
    text=...,
    timestamp=...,
    source=...,
    severity=...,
    status=...,
    count=...,
)

# Create from JSON
alarm_event_alarm = AlarmEventAlarm.from_json(
    '{ "id": ..., "tenantId": ..., "creationTime": ..., "type": ..., "text": ..., "timestamp": ..., "source": ..., "severity": ..., "status": ..., "count": ... }'
)

# Export to dictionary
alarm_event_alarm_dict = alarm_event_alarm.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


