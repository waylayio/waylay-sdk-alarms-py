# CloudAlarmEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**source** | **object** |  | [optional] 
**subject** | **str** |  | [optional] 
**type** | [**CloudAlarmEventDataType**](CloudAlarmEventDataType.md) |  | [optional] 
**data** | [**AlarmEvent**](AlarmEvent.md) |  | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from waylay.services.alarms.models.cloud_alarm_event_data import CloudAlarmEventData

# TODO update the JSON string below
json = "{}"
# create an instance of CloudAlarmEventData from a JSON string
cloud_alarm_event_data_instance = CloudAlarmEventData.from_json(json)
# print the JSON string representation of the object
print CloudAlarmEventData.to_json()

# convert the object into a dict
cloud_alarm_event_data_dict = cloud_alarm_event_data_instance.to_dict()
# create an instance of CloudAlarmEventData from a dict
cloud_alarm_event_data_form_dict = cloud_alarm_event_data.from_dict(cloud_alarm_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


