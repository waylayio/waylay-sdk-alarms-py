# EventOccurredAgainEventType

An alarm happened again.

**Source:** `waylay.services.alarms.models.event_occurred_again_event_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**IO_DOT_WAYLAY_DOT_ALARM_DOT_EVENT_OCCURED_AGAIN** | `'io.waylay.alarm.EventOccuredAgain'` |

## Example

```python
from waylay.services.alarms.models.event_occurred_again_event_type import (
    EventOccurredAgainEventType,
)

# Use enum by value
my_event_occurred_again_event_type = (
    EventOccurredAgainEventType.IO_DOT_WAYLAY_DOT_ALARM_DOT_EVENT_OCCURED_AGAIN
)
print(my_event_occurred_again_event_type)  # Output: 'io.waylay.alarm.EventOccuredAgain'

# Or by string value
my_event_occurred_again_event_type = EventOccurredAgainEventType(
    "io.waylay.alarm.EventOccuredAgain"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


