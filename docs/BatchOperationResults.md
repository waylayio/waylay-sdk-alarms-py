# BatchOperationResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User id of the user who started the operation | 
**operation** | [**BatchOperationOperation**](BatchOperationOperation.md) |  | 
**queue_time** | **datetime** |  | 
**finished_time** | **datetime** |  | 
**results** | [**OperationResultObjectResults**](OperationResultObjectResults.md) |  | 

## Example

```python
from waylay.services.alarms.models.batch_operation_results import BatchOperationResults

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOperationResults from a JSON string
batch_operation_results_instance = BatchOperationResults.from_json(json)
# print the JSON string representation of the object
print BatchOperationResults.to_json()

# convert the object into a dict
batch_operation_results_dict = batch_operation_results_instance.to_dict()
# create an instance of BatchOperationResults from a dict
batch_operation_results_form_dict = batch_operation_results.from_dict(batch_operation_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


