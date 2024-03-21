# BatchDeleteAlarmAllOfQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 
**type** | [**AlarmTypeFilter**](AlarmTypeFilter.md) |  | [optional] 
**status** | [**AlarmStatusFilter**](AlarmStatusFilter.md) |  | [optional] 
**severity** | [**AlarmSeverityFilter**](AlarmSeverityFilter.md) |  | [optional] 
**source** | [**AlarmSourceFilter**](AlarmSourceFilter.md) |  | [optional] 
**date_from** | **int** |  | [optional] 
**date_to** | **int** |  | [optional] 
**assignee** | **str** | String field to indicate an assignee for the alarm. | [optional] 
**creation_time_from** | **int** |  | [optional] 
**creation_time_to** | **int** |  | [optional] 
**last_updated_from** | **int** |  | [optional] 
**last_updated_to** | **int** |  | [optional] 
**last_triggered_from** | **int** |  | [optional] 
**last_triggered_to** | **int** |  | [optional] 

## Example

```python
from waylay.services.alarms.models.batch_delete_alarm_all_of_query import BatchDeleteAlarmAllOfQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeleteAlarmAllOfQuery from a JSON string
batch_delete_alarm_all_of_query_instance = BatchDeleteAlarmAllOfQuery.from_json(json)
# print the JSON string representation of the object
print BatchDeleteAlarmAllOfQuery.to_json()

# convert the object into a dict
batch_delete_alarm_all_of_query_dict = batch_delete_alarm_all_of_query_instance.to_dict()
# create an instance of BatchDeleteAlarmAllOfQuery from a dict
batch_delete_alarm_all_of_query_form_dict = batch_delete_alarm_all_of_query.from_dict(batch_delete_alarm_all_of_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


