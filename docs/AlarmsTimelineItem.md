# AlarmsTimelineItem


**Source:** `waylay.services.alarms.models.alarms_timeline_item`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Timestamp of the event | 
**type** | [**AlarmEventType**](AlarmEventType.md) |  | 
**alarm** | [**AlarmTimelineInfo**](AlarmTimelineInfo.md) |  | 


## Example

```python
from waylay.services.alarms.models.alarms_timeline_item import AlarmsTimelineItem

alarms_timeline_item = AlarmsTimelineItem(timestamp=..., type=..., alarm=...)

# Create from JSON
alarms_timeline_item = AlarmsTimelineItem.from_json(
    '{ "timestamp": ..., "type": ..., "alarm": ... }'
)

# Export to dictionary
alarms_timeline_item_dict = alarms_timeline_item.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


