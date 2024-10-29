# waylay.services.alarms.AlarmsBatchOperationsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](AlarmsBatchOperationsApi.md#get) | **GET** /alarms/v1/batch/{batchId} | Get Alarms Batch Operation Status
[**start**](AlarmsBatchOperationsApi.md#start) | **POST** /alarms/v1/batch | Start Alarms Batch Operation

# **get**
> get(
> batch_id: str,
> headers
> ) -> BatchOperationResults

Get Alarms Batch Operation Status

Get the results of the Alarms Batch Operation.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-alarms-types` is installed
from waylay.services.alarms.models.batch_operation_results import BatchOperationResults
try:
    # Get Alarms Batch Operation Status
    # calls `GET /alarms/v1/batch/{batchId}`
    api_response = await waylay_client.alarms.alarms_batch_operations.get(
        'batch_id_example', # batch_id | path param "batchId"
    )
    print("The response of alarms.alarms_batch_operations.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling alarms.alarms_batch_operations.get: %s\n" % e)
```

### Endpoint
```
GET /alarms/v1/batch/{batchId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**batch_id** | **str** | path parameter `"batchId"` | Unique Batch Operation identifier | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`BatchOperationResults`** |  | [BatchOperationResults](BatchOperationResults.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Batch Operation |  -  |
**404** | Batch Operation Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(
> headers
> ) -> BatchOperationEnqueued

Start Alarms Batch Operation

Start Alarms Batch Operation.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-alarms-types` is installed
from waylay.services.alarms.models.batch_alarms_specification import BatchAlarmsSpecification
from waylay.services.alarms.models.batch_operation_enqueued import BatchOperationEnqueued
try:
    # Start Alarms Batch Operation
    # calls `POST /alarms/v1/batch`
    api_response = await waylay_client.alarms.alarms_batch_operations.start(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.alarms.BatchAlarmsSpecification() # BatchAlarmsSpecification | Batch Alarm Operation
    )
    print("The response of alarms.alarms_batch_operations.start:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling alarms.alarms_batch_operations.start: %s\n" % e)
```

### Endpoint
```
POST /alarms/v1/batch
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**BatchAlarmsSpecification**](BatchAlarmsSpecification.md) | json request body | Batch Alarm Operation | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`BatchOperationEnqueued`** |  | [BatchOperationEnqueued](BatchOperationEnqueued.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Batch Operation Started |  * Location - URI where the batch operation status can be followed <br>  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

