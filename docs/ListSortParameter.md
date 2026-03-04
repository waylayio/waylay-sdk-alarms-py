# ListSortParameter


**Source:** `waylay.services.alarms.models.list_sort_parameter`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**TIMESTAMP** | `'timestamp'` |
**LASTUPDATETIME** | `'lastUpdateTime'` |
**LASTTRIGGEREDTIME** | `'lastTriggeredTime'` |

## Example

```python
from waylay.services.alarms.models.list_sort_parameter import ListSortParameter

# Use enum by value
my_list_sort_parameter = ListSortParameter.TIMESTAMP
print(my_list_sort_parameter)  # Output: 'timestamp'

# Or by string value
my_list_sort_parameter = ListSortParameter("timestamp")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


