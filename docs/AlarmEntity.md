# AlarmEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique alarm identifier. | 
**creation_time** | **datetime** |  | 
**last_update_time** | **datetime** |  | 
**last_triggered_time** | **datetime** |  | 
**type** | **str** | Type of the alarm. | 
**text** | **str** | Description of the alarm. | 
**timestamp** | **datetime** |  | 
**source** | [**IdObject**](IdObject.md) |  | 
**severity** | [**AlarmSeverity**](AlarmSeverity.md) |  | 
**status** | [**AlarmStatus**](AlarmStatus.md) |  | 
**count** | **int** | The number of times this alarm has been sent | 
**assignee** | **str** | String field to indicate an assignee for the alarm. | [optional] 
**history** | [**List[AlarmAuditRecord]**](AlarmAuditRecord.md) |  | [optional] 
**var_self** | **str** |  | [optional] 
**additional_properties** | **object** | Additional properties that were present in the creation payload | [optional] 

## Example

```python
from waylay.services.alarms.models.alarm_entity import AlarmEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmEntity from a JSON string
alarm_entity_instance = AlarmEntity.from_json(json)
# print the JSON string representation of the object
print AlarmEntity.to_json()

# convert the object into a dict
alarm_entity_dict = alarm_entity_instance.to_dict()
# create an instance of AlarmEntity from a dict
alarm_entity_form_dict = alarm_entity.from_dict(alarm_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


