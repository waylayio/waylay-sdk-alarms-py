# AlarmsTimelineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Timestamp of the event | 
**type** | [**AlarmEventType**](AlarmEventType.md) |  | 
**alarm** | [**AlarmTimelineInfo**](AlarmTimelineInfo.md) |  | 

## Example

```python
from waylay.services.alarms.models.alarms_timeline_item import AlarmsTimelineItem

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmsTimelineItem from a JSON string
alarms_timeline_item_instance = AlarmsTimelineItem.from_json(json)
# print the JSON string representation of the object
print AlarmsTimelineItem.to_json()

# convert the object into a dict
alarms_timeline_item_dict = alarms_timeline_item_instance.to_dict()
# create an instance of AlarmsTimelineItem from a dict
alarms_timeline_item_form_dict = alarms_timeline_item.from_dict(alarms_timeline_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


