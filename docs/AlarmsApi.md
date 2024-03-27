# waylay.services.alarms.AlarmsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AlarmsApi.md#create) | **POST** /alarms/v1/alarms | Create Alarm
[**delete**](AlarmsApi.md#delete) | **DELETE** /alarms/v1/alarms/{alarmId} | Delete Alarm
[**get**](AlarmsApi.md#get) | **GET** /alarms/v1/alarms/{alarmId} | Get Alarm
[**list**](AlarmsApi.md#list) | **GET** /alarms/v1/alarms | Query Multiple Alarms
[**update**](AlarmsApi.md#update) | **PUT** /alarms/v1/alarms/{alarmId} | Update Alarm

# **create**
> create(
> headers
> ) -> AlarmEntity

Create Alarm

Create an alarm.  If an `ACTIVE` or `ACKNOWLEDGED` alarm with the same `source.id` and `type` exists,  no new alarm is created.   Instead, the existing alarm is updated by incrementing the `count` property  and a new audit record of type `io.waylay.alarm.EventOccuredAgain` is added to the history.   Only the latest 1000 `io.waylay.alarm.EventOccuredAgain` audit records are kept in the history.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-alarms-types` is installed
from waylay.services.alarms.models.alarm_entity import AlarmEntity
from waylay.services.alarms.models.create_alarm import CreateAlarm
try:
    # Create Alarm
    # calls `POST /alarms/v1/alarms`
    api_response = await waylay_client.alarms.alarms.create(
    )
    print("The response of alarms.alarms.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling alarms.alarms.create: %s\n" % e)
```

### Endpoint
```
POST /alarms/v1/alarms
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`AlarmEntity`** |  | [AlarmEntity](AlarmEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(
> alarm_id: str,
> headers
> ) -> void (empty response body)

Delete Alarm

Delete an Alarm.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-alarms-types` is installed
try:
    # Delete Alarm
    # calls `DELETE /alarms/v1/alarms/{alarmId}`
    await waylay_client.alarms.alarms.delete(
        'alarm_id_example', # alarm_id | path param "alarmId"
    )
except ApiError as e:
    print("Exception when calling alarms.alarms.delete: %s\n" % e)
```

### Endpoint
```
DELETE /alarms/v1/alarms/{alarmId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**alarm_id** | **str** | path parameter `"alarmId"` | Unique Alarm Identifier | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | void (empty response body) |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Alarm Deleted |  -  |
**404** | Alarm Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> alarm_id: str,
> headers
> ) -> AlarmEntity

Get Alarm

Get an alarm.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-alarms-types` is installed
from waylay.services.alarms.models.alarm_entity import AlarmEntity
try:
    # Get Alarm
    # calls `GET /alarms/v1/alarms/{alarmId}`
    api_response = await waylay_client.alarms.alarms.get(
        'alarm_id_example', # alarm_id | path param "alarmId"
    )
    print("The response of alarms.alarms.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling alarms.alarms.get: %s\n" % e)
```

### Endpoint
```
GET /alarms/v1/alarms/{alarmId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**alarm_id** | **str** | path parameter `"alarmId"` | Unique Alarm Identifier | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`AlarmEntity`** |  | [AlarmEntity](AlarmEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alarm Fetched |  -  |
**404** | Alarm Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> AlarmsQueryResult

Query Multiple Alarms

Query multiple alarms using a query language. The response contains the total number of alarms that fulfill the criteria.  By default, returns the first 50 alarms.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-alarms-types` is installed
from waylay.services.alarms.models.alarm_severity import AlarmSeverity
from waylay.services.alarms.models.alarm_status import AlarmStatus
from waylay.services.alarms.models.alarms_query_result import AlarmsQueryResult
from waylay.services.alarms.models.list_additional_query_params_parameter_value import ListAdditionalQueryParamsParameterValue
from waylay.services.alarms.models.list_order_parameter import ListOrderParameter
from waylay.services.alarms.models.list_sort_parameter import ListSortParameter
try:
    # Query Multiple Alarms
    # calls `GET /alarms/v1/alarms`
    api_response = await waylay_client.alarms.alarms.list(
        # query parameters:
        query = {
            'dateFrom': 56
            'dateTo': 56
            'from': 56
            'to': 56
            'creationTimeFrom': 56
            'creationTimeTo': 56
            'lastUpdatedFrom': 56
            'lastUpdatedTo': 56
            'lastTriggeredFrom': 56
            'lastTriggeredTo': 56
            'sort': 'timestamp'
            'order': 'asc'
            'page': 1
            'size': 50
            'additionalQueryParams': {'key': waylay.services.alarms.ListAdditionalQueryParamsParameterValue()}
        },
    )
    print("The response of alarms.alarms.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling alarms.alarms.list: %s\n" % e)
```

### Endpoint
```
GET /alarms/v1/alarms
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['type']** (dict) <br> **query.type** (Query) | [**List[str]**](str.md) | query parameter `"type"` | Filter on one or more alarm types. | [optional] 
**query['status']** (dict) <br> **query.status** (Query) | [**List[AlarmStatus]**](AlarmStatus.md) | query parameter `"status"` | Filter on one or more alarm statuses. | [optional] 
**query['severity']** (dict) <br> **query.severity** (Query) | [**List[AlarmSeverity]**](AlarmSeverity.md) | query parameter `"severity"` | Filter on one or more alarm severities. | [optional] 
**query['source']** (dict) <br> **query.source** (Query) | [**List[str]**](str.md) | query parameter `"source"` | Filter on one or more source ids.  At least one source id is mandatory in combination with &#x60;Accept: application/vnd.waylay.alarms.timeseries+json&#x60; | [optional] 
**query['dateFrom']** (dict) <br> **query.date_from** (Query) | **int** | query parameter `"dateFrom"` | Filter on alarm timestamp (equal or above). | [optional] 
**query['dateTo']** (dict) <br> **query.date_to** (Query) | **int** | query parameter `"dateTo"` | Filter on alarm timestamp (equal or below). | [optional] 
**query['from']** (dict) <br> **query.var_from** (Query) | **int** | query parameter `"from"` | Only applicable in combination with &#x60;Accept: application/vnd.waylay.alarms.timeseries+json&#x60;  Limits the timestamp of the Alarm Audit Records to be &gt;&#x3D; &#x60;from&#x60; | [optional] 
**query['to']** (dict) <br> **query.to** (Query) | **int** | query parameter `"to"` | Only applicable in combination with &#x60;Accept: application/vnd.waylay.alarms.timeseries+json&#x60;  Limits the timestamp of the Alarm Audit Records to be &lt;&#x3D; &#x60;to&#x60; | [optional] 
**query['creationTimeFrom']** (dict) <br> **query.creation_time_from** (Query) | **int** | query parameter `"creationTimeFrom"` | Filter on alarm creationTime (equal or above). | [optional] 
**query['creationTimeTo']** (dict) <br> **query.creation_time_to** (Query) | **int** | query parameter `"creationTimeTo"` | Filter on alarm creationTime (equal or below). | [optional] 
**query['lastUpdatedFrom']** (dict) <br> **query.last_updated_from** (Query) | **int** | query parameter `"lastUpdatedFrom"` | Filter on alarm lastUpdateTime (equal or above). | [optional] 
**query['lastUpdatedTo']** (dict) <br> **query.last_updated_to** (Query) | **int** | query parameter `"lastUpdatedTo"` | Filter on alarm lastUpdateTime (equal or below). | [optional] 
**query['lastTriggeredFrom']** (dict) <br> **query.last_triggered_from** (Query) | **int** | query parameter `"lastTriggeredFrom"` | Filter on alarm lastTriggeredTime (equal or above). | [optional] 
**query['lastTriggeredTo']** (dict) <br> **query.last_triggered_to** (Query) | **int** | query parameter `"lastTriggeredTo"` | Filter on alarm lastTriggeredTime (equal or below). | [optional] 
**query['sort']** (dict) <br> **query.sort** (Query) | [**ListSortParameter**](.md) | query parameter `"sort"` | (Pagination) field used to sort the alarms  Ignored in combination with &#x60;Accept: application/vnd.waylay.alarms.timeseries+json&#x60; | [optional] 
**query['order']** (dict) <br> **query.order** (Query) | [**ListOrderParameter**](.md) | query parameter `"order"` | (Pagination) sort order  Ignored in combination with &#x60;Accept: application/vnd.waylay.alarms.timeseries+json&#x60; | [optional] 
**query['page']** (dict) <br> **query.page** (Query) | **int** | query parameter `"page"` | (Pagination) page Number   Ignored in combination with &#x60;Accept: application/vnd.waylay.alarms.timeseries+json&#x60; | [optional] [default 1]
**query['size']** (dict) <br> **query.size** (Query) | **int** | query parameter `"size"` | (Pagination) size of a page  Ignored in combination with &#x60;Accept: application/vnd.waylay.alarms.timeseries+json&#x60; | [optional] [default 50]
**query['additionalQueryParams']** (dict) <br> **query.additional_query_params** (Query) | [**Dict[str, ListAdditionalQueryParamsParameterValue]**](ListAdditionalQueryParamsParameterValue.md) | query parameter `"additionalQueryParams"` | To query the alarms based on the value of an additional property of the alarm,  you can add the key of the additional property as query parameter  with value the value you expect the alarm to have. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`AlarmsQueryResult`** |  | [AlarmsQueryResult](AlarmsQueryResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.waylay.alarms.timeseries+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Count - Total number of alarms that fulfill the criteria <br>  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(
> alarm_id: str,
> headers
> ) -> AlarmEntity

Update Alarm

Update an alarm.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-alarms-types` is installed
from waylay.services.alarms.models.alarm_entity import AlarmEntity
from waylay.services.alarms.models.alarm_update import AlarmUpdate
try:
    # Update Alarm
    # calls `PUT /alarms/v1/alarms/{alarmId}`
    api_response = await waylay_client.alarms.alarms.update(
        'alarm_id_example', # alarm_id | path param "alarmId"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.alarms.AlarmUpdate() # AlarmUpdate | 
    )
    print("The response of alarms.alarms.update:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling alarms.alarms.update: %s\n" % e)
```

### Endpoint
```
PUT /alarms/v1/alarms/{alarmId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**alarm_id** | **str** | path parameter `"alarmId"` | Unique Alarm Identifier | 
**json** | [**AlarmUpdate**](AlarmUpdate.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`AlarmEntity`** |  | [AlarmEntity](AlarmEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alarm Updated |  -  |
**400** | Error Response |  -  |
**404** | Alarm Not Found |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

