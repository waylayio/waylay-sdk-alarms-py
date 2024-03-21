# BatchOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User id of the user who started the operation | 
**operation** | [**BatchOperationOperation**](BatchOperationOperation.md) |  | 
**queue_time** | **datetime** |  | 

## Example

```python
from waylay.services.alarms.models.batch_operation import BatchOperation

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOperation from a JSON string
batch_operation_instance = BatchOperation.from_json(json)
# print the JSON string representation of the object
print BatchOperation.to_json()

# convert the object into a dict
batch_operation_dict = batch_operation_instance.to_dict()
# create an instance of BatchOperation from a dict
batch_operation_form_dict = batch_operation.from_dict(batch_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


