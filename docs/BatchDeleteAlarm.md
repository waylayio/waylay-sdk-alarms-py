# BatchDeleteAlarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | 
**action** | [**BatchDeleteAlarmAllOfAction**](BatchDeleteAlarmAllOfAction.md) |  | 
**query** | [**BatchDeleteAlarmAllOfQuery**](BatchDeleteAlarmAllOfQuery.md) |  | 

## Example

```python
from waylay.services.alarms.models.batch_delete_alarm import BatchDeleteAlarm

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeleteAlarm from a JSON string
batch_delete_alarm_instance = BatchDeleteAlarm.from_json(json)
# print the JSON string representation of the object
print BatchDeleteAlarm.to_json()

# convert the object into a dict
batch_delete_alarm_dict = batch_delete_alarm_instance.to_dict()
# create an instance of BatchDeleteAlarm from a dict
batch_delete_alarm_form_dict = batch_delete_alarm.from_dict(batch_delete_alarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


