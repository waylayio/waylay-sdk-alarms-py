# OperationResultObjectResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | [**Dict[str, SuccessOperationResultValue]**](SuccessOperationResultValue.md) | Object containing the successful operation results.  The keys will be alarm ids. | 
**failure** | [**Dict[str, FailureOperationResultValue]**](FailureOperationResultValue.md) | Object containing the unsuccessful operation results.  The keys will be alarm ids. | 

## Example

```python
from waylay.services.alarms.models.operation_result_object_results import OperationResultObjectResults

# TODO update the JSON string below
json = "{}"
# create an instance of OperationResultObjectResults from a JSON string
operation_result_object_results_instance = OperationResultObjectResults.from_json(json)
# print the JSON string representation of the object
print OperationResultObjectResults.to_json()

# convert the object into a dict
operation_result_object_results_dict = operation_result_object_results_instance.to_dict()
# create an instance of OperationResultObjectResults from a dict
operation_result_object_results_form_dict = operation_result_object_results.from_dict(operation_result_object_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


