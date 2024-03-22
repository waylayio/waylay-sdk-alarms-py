# BulkQueryFilter

Object specifying filters on the alarm to which the operation will be applied. At least one of the filters must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from waylay.services.alarms.models.bulk_query_filter import BulkQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of BulkQueryFilter from a JSON string
bulk_query_filter_instance = BulkQueryFilter.from_json(json)
# print the JSON string representation of the object
print BulkQueryFilter.to_json()

# convert the object into a dict
bulk_query_filter_dict = bulk_query_filter_instance.to_dict()
# create an instance of BulkQueryFilter from a dict
bulk_query_filter_form_dict = bulk_query_filter.from_dict(bulk_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


