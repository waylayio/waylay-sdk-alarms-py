# AlarmTimelineInfo

The alarm as it is after the event

**Source:** `waylay.services.alarms.models.alarm_timeline_info`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique alarm identifier. | 
**creation_time** | **datetime** |  | 
**timestamp** | **datetime** |  | 
**source** | [**IdObject**](IdObject.md) |  | 
**type** | **str** | Type of the alarm. | 
**text** | **str** | Description of the alarm. | 
**severity** | [**AlarmSeverity**](AlarmSeverity.md) |  | 
**status** | [**AlarmStatus**](AlarmStatus.md) |  | [default to AlarmStatus.ACTIVE]
**assignee** | **str** | String field to indicate an assignee for the alarm. | [optional] 


## Example

```python
from waylay.services.alarms.models.alarm_timeline_info import AlarmTimelineInfo

alarm_timeline_info = AlarmTimelineInfo(
    id=...,
    creation_time=...,
    timestamp=...,
    source=...,
    type=...,
    text=...,
    severity=...,
    status=...,
    assignee=...,
)

# Create from JSON
alarm_timeline_info = AlarmTimelineInfo.from_json(
    '{ "id": ..., "creationTime": ..., "timestamp": ..., "source": ..., "type": ..., "text": ..., "severity": ..., "status": ..., "assignee": ... }'
)

# Export to dictionary
alarm_timeline_info_dict = alarm_timeline_info.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


