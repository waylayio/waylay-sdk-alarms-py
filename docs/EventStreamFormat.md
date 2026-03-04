# EventStreamFormat


**Source:** `waylay.services.alarms.models.event_stream_format`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**APPLICATION_SLASH_CLOUDEVENTS_PLUS_JSON** | `'application/cloudevents+json'` |

## Example

```python
from waylay.services.alarms.models.event_stream_format import EventStreamFormat

# Use enum by value
my_event_stream_format = EventStreamFormat.APPLICATION_SLASH_CLOUDEVENTS_PLUS_JSON
print(my_event_stream_format)  # Output: 'application/cloudevents+json'

# Or by string value
my_event_stream_format = EventStreamFormat("application/cloudevents+json")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


