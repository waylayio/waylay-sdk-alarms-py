# AlarmSeverityFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.alarms.models.alarm_severity_filter import AlarmSeverityFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmSeverityFilter from a JSON string
alarm_severity_filter_instance = AlarmSeverityFilter.from_json(json)
# print the JSON string representation of the object
print AlarmSeverityFilter.to_json()

# convert the object into a dict
alarm_severity_filter_dict = alarm_severity_filter_instance.to_dict()
# create an instance of AlarmSeverityFilter from a dict
alarm_severity_filter_form_dict = alarm_severity_filter.from_dict(alarm_severity_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


