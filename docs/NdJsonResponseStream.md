# NdJsonResponseStream


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
from waylay.services.alarms.models.nd_json_response_stream import NdJsonResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of NdJsonResponseStream from a JSON string
nd_json_response_stream_instance = NdJsonResponseStream.from_json(json)
# print the JSON string representation of the object
print NdJsonResponseStream.to_json()

# convert the object into a dict
nd_json_response_stream_dict = nd_json_response_stream_instance.to_dict()
# create an instance of NdJsonResponseStream from a dict
nd_json_response_stream_form_dict = nd_json_response_stream.from_dict(nd_json_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


