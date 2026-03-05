# AlarmsQueryResult


**Source:** `waylay.services.alarms.models.alarms_query_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Link to alarm query | 
**alarms** | [**List[AlarmEntity]**](AlarmEntity.md) |  | 
**total** | **int** | Total number of alarms that fulfill the criteria | 
**next** | **str** | Link to the next page of results (if more results are available) | [optional] 
**prev** | **str** | Link to the previous page of result (if previous page is available) | [optional] 


## Example

```python
from waylay.services.alarms.models.alarms_query_result import AlarmsQueryResult

alarms_query_result = AlarmsQueryResult(
    var_self=..., alarms=..., total=..., next=..., prev=...
)

# Create from JSON
alarms_query_result = AlarmsQueryResult.from_json(
    '{ "self": ..., "alarms": ..., "total": ..., "next": ..., "prev": ... }'
)

# Export to dictionary
alarms_query_result_dict = alarms_query_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


