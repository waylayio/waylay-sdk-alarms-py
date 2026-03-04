# AlarmSeverity


**Source:** `waylay.services.alarms.models.alarm_severity`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**CRITICAL** | `'CRITICAL'` |
**MAJOR** | `'MAJOR'` |
**MINOR** | `'MINOR'` |
**WARNING** | `'WARNING'` |

## Example

```python
from waylay.services.alarms.models.alarm_severity import AlarmSeverity

# Use enum by value
my_alarm_severity = AlarmSeverity.CRITICAL
print(my_alarm_severity)  # Output: 'CRITICAL'

# Or by string value
my_alarm_severity = AlarmSeverity("CRITICAL")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


