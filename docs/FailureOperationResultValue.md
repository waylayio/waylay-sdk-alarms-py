# FailureOperationResultValue

The keys will be alarm ids.

**Source:** `waylay.services.alarms.models.failure_operation_result_value`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | The statusCode of the operation | 
**error** | **str** | Error description of what went wrong. | 


## Example

```python
from waylay.services.alarms.models.failure_operation_result_value import (
    FailureOperationResultValue,
)

failure_operation_result_value = FailureOperationResultValue(status_code=..., error=...)

# Create from JSON
failure_operation_result_value = FailureOperationResultValue.from_json(
    '{ "statusCode": ..., "error": ... }'
)

# Export to dictionary
failure_operation_result_value_dict = failure_operation_result_value.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


