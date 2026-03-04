# BulkQueryFilter

Object specifying filters on the alarm to which the operation will be applied. At least one of the filters must be set.

**Source:** `waylay.services.alarms.models.bulk_query_filter`




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

bulk_query_filter = BulkQueryFilter(
    type=...,
    status=...,
    severity=...,
    source=...,
    date_from=...,
    date_to=...,
    assignee=...,
    creation_time_from=...,
    creation_time_to=...,
    last_updated_from=...,
    last_updated_to=...,
    last_triggered_from=...,
    last_triggered_to=...,
)

# Create from JSON
bulk_query_filter = BulkQueryFilter.from_json(
    '{ "type": ..., "status": ..., "severity": ..., "source": ..., "dateFrom": ..., "dateTo": ..., "assignee": ..., "creationTimeFrom": ..., "creationTimeTo": ..., "lastUpdatedFrom": ..., "lastUpdatedTo": ..., "lastTriggeredFrom": ..., "lastTriggeredTo": ... }'
)

# Export to dictionary
bulk_query_filter_dict = bulk_query_filter.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


