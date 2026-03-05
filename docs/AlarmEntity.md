# AlarmEntity


**Source:** `waylay.services.alarms.models.alarm_entity`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique alarm identifier. | 
**creation_time** | **datetime** |  | 
**last_update_time** | **datetime** |  | 
**last_triggered_time** | **datetime** |  | 
**type** | **str** | Type of the alarm. | 
**text** | **str** | Description of the alarm. | 
**timestamp** | **datetime** |  | 
**source** | [**IdObject**](IdObject.md) |  | 
**severity** | [**AlarmSeverity**](AlarmSeverity.md) |  | 
**status** | [**AlarmStatus**](AlarmStatus.md) |  | [default to AlarmStatus.ACTIVE]
**count** | **int** | The number of times this alarm has been sent | 
**assignee** | **str** | String field to indicate an assignee for the alarm. | [optional] 
**history** | [**List[AlarmAuditRecord]**](AlarmAuditRecord.md) |  | [optional] 
**var_self** | **str** |  | [optional] 
**additional_properties** | **object** | Additional properties that were present in the creation payload | [optional] 


## Example

```python
from waylay.services.alarms.models.alarm_entity import AlarmEntity

alarm_entity = AlarmEntity(
    id=...,
    creation_time=...,
    last_update_time=...,
    last_triggered_time=...,
    type=...,
    text=...,
    timestamp=...,
    source=...,
    severity=...,
    status=...,
    count=...,
    assignee=...,
    history=...,
    var_self=...,
    additional_properties=...,
)

# Create from JSON
alarm_entity = AlarmEntity.from_json(
    '{ "id": ..., "creationTime": ..., "lastUpdateTime": ..., "lastTriggeredTime": ..., "type": ..., "text": ..., "timestamp": ..., "source": ..., "severity": ..., "status": ..., "count": ..., "assignee": ..., "history": ..., "self": ..., "additionalProperties": ... }'
)

# Export to dictionary
alarm_entity_dict = alarm_entity.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


