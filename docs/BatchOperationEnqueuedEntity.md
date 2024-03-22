# BatchOperationEnqueuedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**queue_time** | **datetime** |  | 
**operation** | [**QueuedOperationSummary**](QueuedOperationSummary.md) |  | 

## Example

```python
from waylay.services.alarms.models.batch_operation_enqueued_entity import BatchOperationEnqueuedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOperationEnqueuedEntity from a JSON string
batch_operation_enqueued_entity_instance = BatchOperationEnqueuedEntity.from_json(json)
# print the JSON string representation of the object
print BatchOperationEnqueuedEntity.to_json()

# convert the object into a dict
batch_operation_enqueued_entity_dict = batch_operation_enqueued_entity_instance.to_dict()
# create an instance of BatchOperationEnqueuedEntity from a dict
batch_operation_enqueued_entity_form_dict = batch_operation_enqueued_entity.from_dict(batch_operation_enqueued_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


