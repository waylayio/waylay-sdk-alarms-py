# ISO8601TimestampOrMillis

ISO8601 timestamp or unix epoch milliseconds.

**Source:** `waylay.services.alarms.models.iso8601_timestamp_or_millis`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
**int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds.
**datetime** | -

## Example

```python
from waylay.services.alarms.models.iso8601_timestamp_or_millis import (
    ISO8601TimestampOrMillis,
)

# Use any of the accepted types (see table above)
my_iso8601_timestamp_or_millis: ISO8601TimestampOrMillis = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


