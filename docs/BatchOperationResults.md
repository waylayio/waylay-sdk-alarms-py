# BatchOperationResults


**Source:** `waylay.services.alarms.models.batch_operation_results`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | [**Dict[str, SuccessOperationResultValue]**](SuccessOperationResultValue.md) | Object containing the successful operation results. The keys will be alarm ids. | 
**failure** | [**Dict[str, FailureOperationResultValue]**](FailureOperationResultValue.md) | Object containing the unsuccessful operation results. The keys will be alarm ids. | 


## Example

```python
from waylay.services.alarms.models.batch_operation_results import BatchOperationResults

batch_operation_results = BatchOperationResults(success=..., failure=...)

# Create from JSON
batch_operation_results = BatchOperationResults.from_json(
    '{ "success": ..., "failure": ... }'
)

# Export to dictionary
batch_operation_results_dict = batch_operation_results.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


