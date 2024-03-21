# AlarmsQueryResult


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

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmsQueryResult from a JSON string
alarms_query_result_instance = AlarmsQueryResult.from_json(json)
# print the JSON string representation of the object
print AlarmsQueryResult.to_json()

# convert the object into a dict
alarms_query_result_dict = alarms_query_result_instance.to_dict()
# create an instance of AlarmsQueryResult from a dict
alarms_query_result_form_dict = alarms_query_result.from_dict(alarms_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


