# AlarmEvent


**Source:** `waylay.services.alarms.models.alarm_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventtype** | [**AlarmEventType**](AlarmEventType.md) |  | 
**eventtime** | **datetime** |  | 
**alarm** | [**AlarmEventAlarm**](AlarmEventAlarm.md) |  | 
**changes** | [**List[AlarmChangeRecord]**](AlarmChangeRecord.md) | Describes the changes that where done  Will only be there if &#x60;eventtype&#x60; is &#x60;io.waylay.alarm.AlarmUpdated&#x60; | [optional] 


## Example

```python
from waylay.services.alarms.models.alarm_event import AlarmEvent

alarm_event = AlarmEvent(eventtype=..., eventtime=..., alarm=..., changes=...)

# Create from JSON
alarm_event = AlarmEvent.from_json(
    '{ "eventtype": ..., "eventtime": ..., "alarm": ..., "changes": ... }'
)

# Export to dictionary
alarm_event_dict = alarm_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


