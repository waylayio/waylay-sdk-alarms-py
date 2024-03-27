# waylay.services.alarms.VersionApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](VersionApi.md#get) | **GET** /alarms/v1 | Version

# **get**
> get(
> headers
> ) -> VersionResponse

Version

Get the status and version of the service.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-alarms-types` is installed
from waylay.services.alarms.models.version_response import VersionResponse
try:
    # Version
    # calls `GET /alarms/v1`
    api_response = await waylay_client.alarms.version.get(
    )
    print("The response of alarms.version.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling alarms.version.get: %s\n" % e)
```

### Endpoint
```
GET /alarms/v1
```
### Parameters

This endpoint does not need any parameter.
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`VersionResponse`** |  | [VersionResponse](VersionResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

