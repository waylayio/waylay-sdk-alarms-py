# BatchUpdateAlarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | 
**action** | [**BatchUpdateAlarmAllOfAction**](BatchUpdateAlarmAllOfAction.md) |  | 
**query** | [**BulkQueryIds**](BulkQueryIds.md) |  | 
**action_parameters** | [**AlarmUpdate**](AlarmUpdate.md) |  | 

## Example

```python
from waylay.services.alarms.models.batch_update_alarm import BatchUpdateAlarm

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateAlarm from a JSON string
batch_update_alarm_instance = BatchUpdateAlarm.from_json(json)
# print the JSON string representation of the object
print BatchUpdateAlarm.to_json()

# convert the object into a dict
batch_update_alarm_dict = batch_update_alarm_instance.to_dict()
# create an instance of BatchUpdateAlarm from a dict
batch_update_alarm_form_dict = batch_update_alarm.from_dict(batch_update_alarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


