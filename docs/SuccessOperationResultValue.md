# SuccessOperationResultValue

The keys will be alarm ids.

**Source:** `waylay.services.alarms.models.success_operation_result_value`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | The statusCode of the operation | 


## Example

```python
from waylay.services.alarms.models.success_operation_result_value import (
    SuccessOperationResultValue,
)

success_operation_result_value = SuccessOperationResultValue(status_code=...)

# Create from JSON
success_operation_result_value = SuccessOperationResultValue.from_json(
    '{ "statusCode": ... }'
)

# Export to dictionary
success_operation_result_value_dict = success_operation_result_value.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


