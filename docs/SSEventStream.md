# SSEventStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventtype** | [**AlarmEventType**](AlarmEventType.md) |  | 
**eventtime** | **datetime** |  | 
**alarm** | [**AlarmEventAlarm**](AlarmEventAlarm.md) |  | 
**changes** | [**List[AlarmEventChangesInner]**](AlarmEventChangesInner.md) | Describes the changes that where done  Will only be there if &#x60;eventtype&#x60; is &#x60;io.waylay.alarm.AlarmUpdated&#x60; | [optional] 
**id** | **object** |  | [optional] 
**source** | **object** |  | [optional] 
**subject** | **str** |  | 
**type** | **str** |  | [optional] 
**data** | [**AlarmEvent**](AlarmEvent.md) |  | [optional] 
**time** | **datetime** |  | 

## Example

```python
from waylay.services.alarms.models.ss_event_stream import SSEventStream

# TODO update the JSON string below
json = "{}"
# create an instance of SSEventStream from a JSON string
ss_event_stream_instance = SSEventStream.from_json(json)
# print the JSON string representation of the object
print SSEventStream.to_json()

# convert the object into a dict
ss_event_stream_dict = ss_event_stream_instance.to_dict()
# create an instance of SSEventStream from a dict
ss_event_stream_form_dict = ss_event_stream.from_dict(ss_event_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


