# AlarmAuditRecord


**Source:** `waylay.services.alarms.models.alarm_audit_record`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | [**AlarmEventType**](AlarmEventType.md) |  | 
**text** | **str** | Text describing the change | 
**timestamp** | **datetime** |  | 


## Example

```python
from waylay.services.alarms.models.alarm_audit_record import AlarmAuditRecord

alarm_audit_record = AlarmAuditRecord(id=..., type=..., text=..., timestamp=...)

# Create from JSON
alarm_audit_record = AlarmAuditRecord.from_json(
    '{ "id": ..., "type": ..., "text": ..., "timestamp": ... }'
)

# Export to dictionary
alarm_audit_record_dict = alarm_audit_record.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


