# waylay.services.alarms.AlarmEventsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](AlarmEventsApi.md#get) | **GET** /alarms/v1/events | Alarm Events

# **get**
> get(
> query: GetQuery,
> headers
> ) -> NdJsonResponseStream

Alarm Events

Opens a data stream for all Alarm Events for this tenant.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-alarms-types` is installed
from waylay.services.alarms.models.get_eventstream_event_format_parameter import GetEventstreamEventFormatParameter
from waylay.services.alarms.models.nd_json_response_stream import NdJsonResponseStream
try:
    # Alarm Events
    # calls `GET /alarms/v1/events`
    api_response = await waylay_client.alarms.alarm_events.get(
        # query parameters:
        query = {
            'eventFormat': 'application/cloudevents+json'
        },
    )
    print("The response of alarms.alarm_events.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling alarms.alarm_events.get: %s\n" % e)
```

### Endpoint
```
GET /alarms/v1/events
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['eventFormat']** (dict) <br> **query.event_format** (Query) | [**GetEventstreamEventFormatParameter**](.md) | query parameter `"eventFormat"` | The format of events in the stream.   If specified this must be &#x60;application/cloudevents+json&#x60; (make sure to correctly URL encode the &#x60;+&#x60; as &#x60;%2B&#x60;) | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`NdJsonResponseStream`** |  | [NdJsonResponseStream](NdJsonResponseStream.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-ndjson, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alarm Events Stream |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

