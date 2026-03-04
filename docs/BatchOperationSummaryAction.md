# BatchOperationSummaryAction


**Source:** `waylay.services.alarms.models.batch_operation_summary_action`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**DELETE** | `'delete'` |
**UPDATE** | `'update'` |

## Example

```python
from waylay.services.alarms.models.batch_operation_summary_action import (
    BatchOperationSummaryAction,
)

# Use enum by value
my_batch_operation_summary_action = BatchOperationSummaryAction.DELETE
print(my_batch_operation_summary_action)  # Output: 'delete'

# Or by string value
my_batch_operation_summary_action = BatchOperationSummaryAction("delete")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


