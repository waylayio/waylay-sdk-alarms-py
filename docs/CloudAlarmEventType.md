# CloudAlarmEventType


**Source:** `waylay.services.alarms.models.cloud_alarm_event_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**IO_DOT_WAYLAY_DOT_ALARMS_DOT_V1_DOT_ALARM_RAISED** | `'io.waylay.alarms.v1.AlarmRaised'` |
**IO_DOT_WAYLAY_DOT_ALARMS_DOT_V1_DOT_EVENT_OCCURRED_AGAIN** | `'io.waylay.alarms.v1.EventOccurredAgain'` |
**IO_DOT_WAYLAY_DOT_ALARMS_DOT_V1_DOT_ALARM_UPDATED** | `'io.waylay.alarms.v1.AlarmUpdated'` |

## Example

```python
from waylay.services.alarms.models.cloud_alarm_event_type import CloudAlarmEventType

# Use enum by value
my_cloud_alarm_event_type = (
    CloudAlarmEventType.IO_DOT_WAYLAY_DOT_ALARMS_DOT_V1_DOT_ALARM_RAISED
)
print(my_cloud_alarm_event_type)  # Output: 'io.waylay.alarms.v1.AlarmRaised'

# Or by string value
my_cloud_alarm_event_type = CloudAlarmEventType("io.waylay.alarms.v1.AlarmRaised")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


