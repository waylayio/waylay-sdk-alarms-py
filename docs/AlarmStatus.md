# AlarmStatus


**Source:** `waylay.services.alarms.models.alarm_status`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**ACTIVE** | `'ACTIVE'` |
**ACKNOWLEDGED** | `'ACKNOWLEDGED'` |
**CLEARED** | `'CLEARED'` |

## Example

```python
from waylay.services.alarms.models.alarm_status import AlarmStatus

# Use enum by value
my_alarm_status = AlarmStatus.ACTIVE
print(my_alarm_status)  # Output: 'ACTIVE'

# Or by string value
my_alarm_status = AlarmStatus("ACTIVE")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


