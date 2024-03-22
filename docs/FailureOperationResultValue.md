# FailureOperationResultValue

The keys will be alarm ids.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | The statusCode of the operation | 
**error** | **str** | Error description of what went wrong. | 

## Example

```python
from waylay.services.alarms.models.failure_operation_result_value import FailureOperationResultValue

# TODO update the JSON string below
json = "{}"
# create an instance of FailureOperationResultValue from a JSON string
failure_operation_result_value_instance = FailureOperationResultValue.from_json(json)
# print the JSON string representation of the object
print FailureOperationResultValue.to_json()

# convert the object into a dict
failure_operation_result_value_dict = failure_operation_result_value_instance.to_dict()
# create an instance of FailureOperationResultValue from a dict
failure_operation_result_value_form_dict = failure_operation_result_value.from_dict(failure_operation_result_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


