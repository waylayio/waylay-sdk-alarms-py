# BatchAlarm


**Source:** `waylay.services.alarms.models.batch_alarm`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | [optional] 
**action** | **str** |  | [optional] 
**query** | **object** |  | [optional] 


## Example

```python
from waylay.services.alarms.models.batch_alarm import BatchAlarm

batch_alarm = BatchAlarm(entity=..., action=..., query=...)

# Create from JSON
batch_alarm = BatchAlarm.from_json('{ "entity": ..., "action": ..., "query": ... }')

# Export to dictionary
batch_alarm_dict = batch_alarm.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


