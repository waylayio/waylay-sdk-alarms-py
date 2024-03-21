# BatchAlarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | [optional] 
**action** | **str** |  | [optional] 
**query** | **object** |  | [optional] 

## Example

```python
from waylay.services.alarms.models.batch_alarm import BatchAlarm

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAlarm from a JSON string
batch_alarm_instance = BatchAlarm.from_json(json)
# print the JSON string representation of the object
print BatchAlarm.to_json()

# convert the object into a dict
batch_alarm_dict = batch_alarm_instance.to_dict()
# create an instance of BatchAlarm from a dict
batch_alarm_form_dict = batch_alarm.from_dict(batch_alarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


