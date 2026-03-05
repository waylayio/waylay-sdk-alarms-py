# QueuedOperationSummaryAction


**Source:** `waylay.services.alarms.models.queued_operation_summary_action`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**UPDATE** | `'update'` |
**DELETE** | `'delete'` |

## Example

```python
from waylay.services.alarms.models.queued_operation_summary_action import (
    QueuedOperationSummaryAction,
)

# Use enum by value
my_queued_operation_summary_action = QueuedOperationSummaryAction.UPDATE
print(my_queued_operation_summary_action)  # Output: 'update'

# Or by string value
my_queued_operation_summary_action = QueuedOperationSummaryAction("update")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


