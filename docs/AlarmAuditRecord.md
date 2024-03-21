# AlarmAuditRecord


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

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmAuditRecord from a JSON string
alarm_audit_record_instance = AlarmAuditRecord.from_json(json)
# print the JSON string representation of the object
print AlarmAuditRecord.to_json()

# convert the object into a dict
alarm_audit_record_dict = alarm_audit_record_instance.to_dict()
# create an instance of AlarmAuditRecord from a dict
alarm_audit_record_form_dict = alarm_audit_record.from_dict(alarm_audit_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


