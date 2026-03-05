# AlarmChangeType

Indication of what has changed

**Source:** `waylay.services.alarms.models.alarm_change_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**IO_DOT_WAYLAY_DOT_ALARM_DOT_CHANGE_DOT_SEVERITY** | `'io.waylay.alarm.change.severity'` |
**IO_DOT_WAYLAY_DOT_ALARM_DOT_CHANGE_DOT_STATUS** | `'io.waylay.alarm.change.status'` |
**IO_DOT_WAYLAY_DOT_ALARM_DOT_CHANGE_DOT_ATTRIBUTE** | `'io.waylay.alarm.change.attribute'` |

## Example

```python
from waylay.services.alarms.models.alarm_change_type import AlarmChangeType

# Use enum by value
my_alarm_change_type = AlarmChangeType.IO_DOT_WAYLAY_DOT_ALARM_DOT_CHANGE_DOT_SEVERITY
print(my_alarm_change_type)  # Output: 'io.waylay.alarm.change.severity'

# Or by string value
my_alarm_change_type = AlarmChangeType("io.waylay.alarm.change.severity")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


