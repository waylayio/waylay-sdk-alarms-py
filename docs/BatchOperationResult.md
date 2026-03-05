# BatchOperationResult


**Source:** `waylay.services.alarms.models.batch_operation_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User id of the user who started the operation | 
**operation** | [**BatchOperationSummary**](BatchOperationSummary.md) |  | 
**queue_time** | **datetime** |  | 
**finished_time** | **datetime** |  | 
**results** | [**BatchOperationResults**](BatchOperationResults.md) |  | 


## Example

```python
from waylay.services.alarms.models.batch_operation_result import BatchOperationResult

batch_operation_result = BatchOperationResult(
    id=..., user=..., operation=..., queue_time=..., finished_time=..., results=...
)

# Create from JSON
batch_operation_result = BatchOperationResult.from_json(
    '{ "id": ..., "user": ..., "operation": ..., "queueTime": ..., "finishedTime": ..., "results": ... }'
)

# Export to dictionary
batch_operation_result_dict = batch_operation_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


