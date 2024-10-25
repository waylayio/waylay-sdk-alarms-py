# BatchAlarmsSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchAlarmEntity**](BatchAlarmEntity.md) |  | 
**action** | [**BatchDeleteAlarmAllOfAction**](BatchDeleteAlarmAllOfAction.md) |  | 
**query** | [**BatchDeleteAlarmAllOfQuery**](BatchDeleteAlarmAllOfQuery.md) |  | 
**action_parameters** | [**AlarmUpdate**](AlarmUpdate.md) |  | 

## Example

```python
from waylay.services.alarms.models.batch_alarms_specification import BatchAlarmsSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAlarmsSpecification from a JSON string
batch_alarms_specification_instance = BatchAlarmsSpecification.from_json(json)
# print the JSON string representation of the object
print BatchAlarmsSpecification.to_json()

# convert the object into a dict
batch_alarms_specification_dict = batch_alarms_specification_instance.to_dict()
# create an instance of BatchAlarmsSpecification from a dict
batch_alarms_specification_form_dict = batch_alarms_specification.from_dict(batch_alarms_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


