# AlarmRaisedEventType

A new alarm was created.

**Source:** `waylay.services.alarms.models.alarm_raised_event_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**IO_DOT_WAYLAY_DOT_ALARM_DOT_ALARM_RAISED** | `'io.waylay.alarm.AlarmRaised'` |

## Example

```python
from waylay.services.alarms.models.alarm_raised_event_type import AlarmRaisedEventType

# Use enum by value
my_alarm_raised_event_type = (
    AlarmRaisedEventType.IO_DOT_WAYLAY_DOT_ALARM_DOT_ALARM_RAISED
)
print(my_alarm_raised_event_type)  # Output: 'io.waylay.alarm.AlarmRaised'

# Or by string value
my_alarm_raised_event_type = AlarmRaisedEventType("io.waylay.alarm.AlarmRaised")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


