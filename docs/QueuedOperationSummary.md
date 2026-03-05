# QueuedOperationSummary


**Source:** `waylay.services.alarms.models.queued_operation_summary`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | 
**action** | [**QueuedOperationSummaryAction**](QueuedOperationSummaryAction.md) |  | 


## Example

```python
from waylay.services.alarms.models.queued_operation_summary import (
    QueuedOperationSummary,
)

queued_operation_summary = QueuedOperationSummary(entity=..., action=...)

# Create from JSON
queued_operation_summary = QueuedOperationSummary.from_json(
    '{ "entity": ..., "action": ... }'
)

# Export to dictionary
queued_operation_summary_dict = queued_operation_summary.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


