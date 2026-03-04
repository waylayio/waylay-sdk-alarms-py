# BatchDeleteAlarm


**Source:** `waylay.services.alarms.models.batch_delete_alarm`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | 
**action** | [**BatchDeleteAction**](BatchDeleteAction.md) |  | 
**query** | [**BatchDeleteQuery**](BatchDeleteQuery.md) |  | 


## Example

```python
from waylay.services.alarms.models.batch_delete_alarm import BatchDeleteAlarm

batch_delete_alarm = BatchDeleteAlarm(entity=..., action=..., query=...)

# Create from JSON
batch_delete_alarm = BatchDeleteAlarm.from_json(
    '{ "entity": ..., "action": ..., "query": ... }'
)

# Export to dictionary
batch_delete_alarm_dict = batch_delete_alarm.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


