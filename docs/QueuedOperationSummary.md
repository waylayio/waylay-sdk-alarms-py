# QueuedOperationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | 
**action** | [**QueuedOperationSummaryAction**](QueuedOperationSummaryAction.md) |  | 

## Example

```python
from waylay.services.alarms.models.queued_operation_summary import QueuedOperationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of QueuedOperationSummary from a JSON string
queued_operation_summary_instance = QueuedOperationSummary.from_json(json)
# print the JSON string representation of the object
print QueuedOperationSummary.to_json()

# convert the object into a dict
queued_operation_summary_dict = queued_operation_summary_instance.to_dict()
# create an instance of QueuedOperationSummary from a dict
queued_operation_summary_form_dict = queued_operation_summary.from_dict(queued_operation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


