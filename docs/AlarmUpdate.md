# AlarmUpdate

At least one field must be specified.

**Source:** `waylay.services.alarms.models.alarm_update`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | [**AlarmSeverity**](AlarmSeverity.md) |  | [optional] 
**status** | [**AlarmStatus**](AlarmStatus.md) |  | [optional] [default to AlarmStatus.ACTIVE]
**assignee** | **str** |  | [optional] 


## Example

```python
from waylay.services.alarms.models.alarm_update import AlarmUpdate

alarm_update = AlarmUpdate(severity=..., status=..., assignee=...)

# Create from JSON
alarm_update = AlarmUpdate.from_json(
    '{ "severity": ..., "status": ..., "assignee": ... }'
)

# Export to dictionary
alarm_update_dict = alarm_update.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


