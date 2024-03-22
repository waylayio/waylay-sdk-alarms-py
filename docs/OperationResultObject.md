# OperationResultObject

Finished Batch Operation results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finished_time** | **datetime** |  | 
**results** | [**OperationResultObjectResults**](OperationResultObjectResults.md) |  | 

## Example

```python
from waylay.services.alarms.models.operation_result_object import OperationResultObject

# TODO update the JSON string below
json = "{}"
# create an instance of OperationResultObject from a JSON string
operation_result_object_instance = OperationResultObject.from_json(json)
# print the JSON string representation of the object
print OperationResultObject.to_json()

# convert the object into a dict
operation_result_object_dict = operation_result_object_instance.to_dict()
# create an instance of OperationResultObject from a dict
operation_result_object_form_dict = operation_result_object.from_dict(operation_result_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


