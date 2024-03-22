# BatchOperationEnqueued


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**uri** | **str** | URI where the batch operation status can be followed | 
**entity** | [**BatchOperationEnqueuedEntity**](BatchOperationEnqueuedEntity.md) |  | 

## Example

```python
from waylay.services.alarms.models.batch_operation_enqueued import BatchOperationEnqueued

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOperationEnqueued from a JSON string
batch_operation_enqueued_instance = BatchOperationEnqueued.from_json(json)
# print the JSON string representation of the object
print BatchOperationEnqueued.to_json()

# convert the object into a dict
batch_operation_enqueued_dict = batch_operation_enqueued_instance.to_dict()
# create an instance of BatchOperationEnqueued from a dict
batch_operation_enqueued_form_dict = batch_operation_enqueued.from_dict(batch_operation_enqueued_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


