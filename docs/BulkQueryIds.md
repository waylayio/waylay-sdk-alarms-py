# BulkQueryIds


**Source:** `waylay.services.alarms.models.bulk_query_ids`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 


## Example

```python
from waylay.services.alarms.models.bulk_query_ids import BulkQueryIds

bulk_query_ids = BulkQueryIds(ids=...)

# Create from JSON
bulk_query_ids = BulkQueryIds.from_json('{ "ids": ... }')

# Export to dictionary
bulk_query_ids_dict = bulk_query_ids.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


