# AlarmEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventtype** | [**AlarmEventType**](AlarmEventType.md) |  | 
**eventtime** | **datetime** |  | 
**alarm** | [**AlarmEventAlarm**](AlarmEventAlarm.md) |  | 
**changes** | [**List[AlarmEventChangesInner]**](AlarmEventChangesInner.md) | Describes the changes that where done  Will only be there if &#x60;eventtype&#x60; is &#x60;io.waylay.alarm.AlarmUpdated&#x60; | [optional] 

## Example

```python
from waylay.services.alarms.models.alarm_event import AlarmEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmEvent from a JSON string
alarm_event_instance = AlarmEvent.from_json(json)
# print the JSON string representation of the object
print AlarmEvent.to_json()

# convert the object into a dict
alarm_event_dict = alarm_event_instance.to_dict()
# create an instance of AlarmEvent from a dict
alarm_event_form_dict = alarm_event.from_dict(alarm_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


