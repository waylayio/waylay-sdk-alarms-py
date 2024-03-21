# ABatchAlarmsSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | 
**action** | **str** |  | 
**query** | [**BatchDeleteAlarmAllOfQuery**](BatchDeleteAlarmAllOfQuery.md) |  | 
**action_parameters** | [**AlarmUpdate**](AlarmUpdate.md) |  | 

## Example

```python
from waylay.services.alarms.models.a_batch_alarms_specification import ABatchAlarmsSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ABatchAlarmsSpecification from a JSON string
a_batch_alarms_specification_instance = ABatchAlarmsSpecification.from_json(json)
# print the JSON string representation of the object
print ABatchAlarmsSpecification.to_json()

# convert the object into a dict
a_batch_alarms_specification_dict = a_batch_alarms_specification_instance.to_dict()
# create an instance of ABatchAlarmsSpecification from a dict
a_batch_alarms_specification_form_dict = a_batch_alarms_specification.from_dict(a_batch_alarms_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


