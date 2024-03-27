# AlarmEventChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] 
**type** | [**AlarmEventChangesInnerType**](AlarmEventChangesInnerType.md) |  | [optional] 
**old_value** | **str** |  | [optional] 
**new_value** | **str** |  | [optional] 

## Example

```python
from waylay.services.alarms.models.alarm_event_changes_inner import AlarmEventChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmEventChangesInner from a JSON string
alarm_event_changes_inner_instance = AlarmEventChangesInner.from_json(json)
# print the JSON string representation of the object
print AlarmEventChangesInner.to_json()

# convert the object into a dict
alarm_event_changes_inner_dict = alarm_event_changes_inner_instance.to_dict()
# create an instance of AlarmEventChangesInner from a dict
alarm_event_changes_inner_form_dict = alarm_event_changes_inner.from_dict(alarm_event_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


