# SuccessOperationResultValue

The keys will be alarm ids.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | The statusCode of the operation | 

## Example

```python
from waylay.services.alarms.models.success_operation_result_value import SuccessOperationResultValue

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessOperationResultValue from a JSON string
success_operation_result_value_instance = SuccessOperationResultValue.from_json(json)
# print the JSON string representation of the object
print SuccessOperationResultValue.to_json()

# convert the object into a dict
success_operation_result_value_dict = success_operation_result_value_instance.to_dict()
# create an instance of SuccessOperationResultValue from a dict
success_operation_result_value_form_dict = success_operation_result_value.from_dict(success_operation_result_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


