# BatchUpdateAlarm


**Source:** `waylay.services.alarms.models.batch_update_alarm`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | 
**action** | [**BatchUpdateAction**](BatchUpdateAction.md) |  | 
**query** | [**BulkQueryIds**](BulkQueryIds.md) |  | 
**action_parameters** | [**AlarmUpdate**](AlarmUpdate.md) |  | 


## Example

```python
from waylay.services.alarms.models.batch_update_alarm import BatchUpdateAlarm

batch_update_alarm = BatchUpdateAlarm(
    entity=..., action=..., query=..., action_parameters=...
)

# Create from JSON
batch_update_alarm = BatchUpdateAlarm.from_json(
    '{ "entity": ..., "action": ..., "query": ..., "actionParameters": ... }'
)

# Export to dictionary
batch_update_alarm_dict = batch_update_alarm.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


