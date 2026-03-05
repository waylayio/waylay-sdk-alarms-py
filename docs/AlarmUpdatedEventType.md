# AlarmUpdatedEventType

An alarm was updated.

**Source:** `waylay.services.alarms.models.alarm_updated_event_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**IO_DOT_WAYLAY_DOT_ALARM_DOT_ALARM_UPDATED** | `'io.waylay.alarm.AlarmUpdated'` |

## Example

```python
from waylay.services.alarms.models.alarm_updated_event_type import AlarmUpdatedEventType

# Use enum by value
my_alarm_updated_event_type = (
    AlarmUpdatedEventType.IO_DOT_WAYLAY_DOT_ALARM_DOT_ALARM_UPDATED
)
print(my_alarm_updated_event_type)  # Output: 'io.waylay.alarm.AlarmUpdated'

# Or by string value
my_alarm_updated_event_type = AlarmUpdatedEventType("io.waylay.alarm.AlarmUpdated")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


