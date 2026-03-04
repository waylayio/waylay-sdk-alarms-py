# AlarmChangeRecord


**Source:** `waylay.services.alarms.models.alarm_change_record`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] 
**type** | [**AlarmChangeType**](AlarmChangeType.md) |  | [optional] 
**old_value** | **str** |  | [optional] 
**new_value** | **str** |  | [optional] 


## Example

```python
from waylay.services.alarms.models.alarm_change_record import AlarmChangeRecord

alarm_change_record = AlarmChangeRecord(
    attribute=..., type=..., old_value=..., new_value=...
)

# Create from JSON
alarm_change_record = AlarmChangeRecord.from_json(
    '{ "attribute": ..., "type": ..., "oldValue": ..., "newValue": ... }'
)

# Export to dictionary
alarm_change_record_dict = alarm_change_record.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


