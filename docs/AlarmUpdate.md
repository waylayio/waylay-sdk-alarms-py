# AlarmUpdate

At least one field must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | [**AlarmSeverity**](AlarmSeverity.md) |  | [optional] 
**status** | [**AlarmStatus**](AlarmStatus.md) |  | [optional] [default to AlarmStatus.ACTIVE]
**assignee** | **str** |  | [optional] 

## Example

```python
from waylay.services.alarms.models.alarm_update import AlarmUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmUpdate from a JSON string
alarm_update_instance = AlarmUpdate.from_json(json)
# print the JSON string representation of the object
print AlarmUpdate.to_json()

# convert the object into a dict
alarm_update_dict = alarm_update_instance.to_dict()
# create an instance of AlarmUpdate from a dict
alarm_update_form_dict = alarm_update.from_dict(alarm_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


