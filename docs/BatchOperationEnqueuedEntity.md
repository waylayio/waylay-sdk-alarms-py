# BatchOperationEnqueuedEntity


**Source:** `waylay.services.alarms.models.batch_operation_enqueued_entity`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**queue_time** | **datetime** |  | 
**operation** | [**QueuedOperationSummary**](QueuedOperationSummary.md) |  | 


## Example

```python
from waylay.services.alarms.models.batch_operation_enqueued_entity import (
    BatchOperationEnqueuedEntity,
)

batch_operation_enqueued_entity = BatchOperationEnqueuedEntity(
    id=..., queue_time=..., operation=...
)

# Create from JSON
batch_operation_enqueued_entity = BatchOperationEnqueuedEntity.from_json(
    '{ "id": ..., "queueTime": ..., "operation": ... }'
)

# Export to dictionary
batch_operation_enqueued_entity_dict = batch_operation_enqueued_entity.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


