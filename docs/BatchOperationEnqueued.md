# BatchOperationEnqueued


**Source:** `waylay.services.alarms.models.batch_operation_enqueued`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**uri** | **str** | URI where the batch operation status can be followed | 
**entity** | [**BatchOperationEnqueuedEntity**](BatchOperationEnqueuedEntity.md) |  | 


## Example

```python
from waylay.services.alarms.models.batch_operation_enqueued import (
    BatchOperationEnqueued,
)

batch_operation_enqueued = BatchOperationEnqueued(status_code=..., uri=..., entity=...)

# Create from JSON
batch_operation_enqueued = BatchOperationEnqueued.from_json(
    '{ "statusCode": ..., "uri": ..., "entity": ... }'
)

# Export to dictionary
batch_operation_enqueued_dict = batch_operation_enqueued.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


