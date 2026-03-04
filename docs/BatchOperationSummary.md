# BatchOperationSummary

Summary of the batch operation

**Source:** `waylay.services.alarms.models.batch_operation_summary`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | 
**action** | [**BatchOperationSummaryAction**](BatchOperationSummaryAction.md) |  | 
**description** | **str** | Description of the operation | 


## Example

```python
from waylay.services.alarms.models.batch_operation_summary import BatchOperationSummary

batch_operation_summary = BatchOperationSummary(entity=..., action=..., description=...)

# Create from JSON
batch_operation_summary = BatchOperationSummary.from_json(
    '{ "entity": ..., "action": ..., "description": ... }'
)

# Export to dictionary
batch_operation_summary_dict = batch_operation_summary.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


