# AlarmTimelineInfo

The alarm as it is after the event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique alarm identifier. | 
**creation_time** | **datetime** |  | 
**timestamp** | **datetime** |  | 
**source** | [**IdObject**](IdObject.md) |  | 
**type** | **str** | Type of the alarm. | 
**text** | **str** | Description of the alarm. | 
**severity** | [**AlarmSeverity**](AlarmSeverity.md) |  | 
**status** | [**AlarmStatus**](AlarmStatus.md) |  | [default to AlarmStatus.ACTIVE]
**assignee** | **str** | String field to indicate an assignee for the alarm. | [optional] 

## Example

```python
from waylay.services.alarms.models.alarm_timeline_info import AlarmTimelineInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmTimelineInfo from a JSON string
alarm_timeline_info_instance = AlarmTimelineInfo.from_json(json)
# print the JSON string representation of the object
print AlarmTimelineInfo.to_json()

# convert the object into a dict
alarm_timeline_info_dict = alarm_timeline_info_instance.to_dict()
# create an instance of AlarmTimelineInfo from a dict
alarm_timeline_info_form_dict = alarm_timeline_info.from_dict(alarm_timeline_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


