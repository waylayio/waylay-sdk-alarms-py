# CloudAlarmEventData


**Source:** `waylay.services.alarms.models.cloud_alarm_event_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**source** | **object** |  | [optional] 
**subject** | **str** |  | [optional] 
**type** | [**CloudAlarmEventType**](CloudAlarmEventType.md) |  | [optional] 
**data** | [**AlarmEvent**](AlarmEvent.md) |  | [optional] 
**time** | **datetime** |  | [optional] 


## Example

```python
from waylay.services.alarms.models.cloud_alarm_event_data import CloudAlarmEventData

cloud_alarm_event_data = CloudAlarmEventData(
    id=..., source=..., subject=..., type=..., data=..., time=...
)

# Create from JSON
cloud_alarm_event_data = CloudAlarmEventData.from_json(
    '{ "id": ..., "source": ..., "subject": ..., "type": ..., "data": ..., "time": ... }'
)

# Export to dictionary
cloud_alarm_event_data_dict = cloud_alarm_event_data.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


