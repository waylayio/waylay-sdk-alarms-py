# CloudAlarmEvent


**Source:** `waylay.services.alarms.models.cloud_alarm_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**source** | **object** |  | [optional] 
**subject** | **str** |  | 
**type** | [**CloudAlarmEventType**](CloudAlarmEventType.md) |  | [optional] 
**data** | [**AlarmEvent**](AlarmEvent.md) |  | [optional] 
**time** | **datetime** |  | 


## Example

```python
from waylay.services.alarms.models.cloud_alarm_event import CloudAlarmEvent

cloud_alarm_event = CloudAlarmEvent(
    id=..., source=..., subject=..., type=..., data=..., time=...
)

# Create from JSON
cloud_alarm_event = CloudAlarmEvent.from_json(
    '{ "id": ..., "source": ..., "subject": ..., "type": ..., "data": ..., "time": ... }'
)

# Export to dictionary
cloud_alarm_event_dict = cloud_alarm_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


