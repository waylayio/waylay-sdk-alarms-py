# coding: utf-8
"""Waylay Alarms api.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9
import io
import warnings

import enum
from enum import Enum
from pydantic import (
    validate_call,
    Field,
    StrictFloat,
    StrictStr,
    StrictInt,
    StrictBool,
    StrictBytes,
    ConfigDict,
    TypeAdapter,
)
from typing import (
    Dict,
    List,
    Literal,
    Optional,
    Tuple,
    Union,
    Any,
    overload,
    TYPE_CHECKING,
    Type,
    TypeVar,
)
from typing_extensions import (
    Annotated,  # >=3.9,
    NotRequired,  # >=3.11
)

from waylay.sdk.plugin import WithApiClient
from waylay.sdk.api import (
    ApiValueError,
    Request,
    Response,
    HeaderTypes,
    QueryParamTypes,
    RequestFiles,
    RequestData,
    RequestContent,
)
from waylay.sdk.api._models import Model

if TYPE_CHECKING:
    from waylay.services.alarms.models import CreateAlarm

    from waylay.services.alarms.queries.alarms_api import CreateQuery

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import ErrorResponseWithDetails

    from waylay.services.alarms.queries.alarms_api import DeleteQuery

    from waylay.services.alarms.models import ErrorResponse

    from waylay.services.alarms.queries.alarms_api import GetQuery

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import ErrorResponse

    from waylay.services.alarms.queries.alarms_api import ListQuery

    from waylay.services.alarms.models import AlarmsQueryResult

    from waylay.services.alarms.models import AlarmsQueryResult

    from waylay.services.alarms.models import ErrorResponse

    from waylay.services.alarms.models import AlarmUpdate

    from waylay.services.alarms.queries.alarms_api import UpdateQuery

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import ErrorResponseWithDetails

    from waylay.services.alarms.models import ErrorResponse

    from waylay.services.alarms.models import ErrorResponse


try:
    from waylay.services.alarms.models import CreateAlarm

    from waylay.services.alarms.queries.alarms_api import CreateQuery

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import ErrorResponseWithDetails

    from waylay.services.alarms.queries.alarms_api import DeleteQuery

    from waylay.services.alarms.models import ErrorResponse

    from waylay.services.alarms.queries.alarms_api import GetQuery

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import ErrorResponse

    from waylay.services.alarms.queries.alarms_api import ListQuery

    from waylay.services.alarms.models import AlarmsQueryResult

    from waylay.services.alarms.models import AlarmsQueryResult

    from waylay.services.alarms.models import ErrorResponse

    from waylay.services.alarms.models import AlarmUpdate

    from waylay.services.alarms.queries.alarms_api import UpdateQuery

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import AlarmEntity

    from waylay.services.alarms.models import ErrorResponseWithDetails

    from waylay.services.alarms.models import ErrorResponse

    from waylay.services.alarms.models import ErrorResponse

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        CreateAlarm = Model

        CreateQuery = dict

        AlarmEntity = Model

        ErrorResponseWithDetails = Model

        DeleteQuery = dict

        ErrorResponse = Model

        GetQuery = dict

        AlarmEntity = Model

        ErrorResponse = Model

        ListQuery = dict

        AlarmsQueryResult = Model

        ErrorResponse = Model

        AlarmUpdate = Model

        UpdateQuery = dict

        AlarmEntity = Model

        ErrorResponseWithDetails = Model

        ErrorResponse = Model

        ErrorResponse = Model


from waylay.sdk.api import ApiClient, RESTTimeout

T = TypeVar("T")


class AlarmsApi(WithApiClient):
    """AlarmsApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def create(
        self,
        *,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> AlarmEntity: ...

    @overload
    async def create(
        self,
        *,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def create(
        self,
        *,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def create(
        self,
        *,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def create(
        self,
        *,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def create(
        self,
        *,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> AlarmEntity | T | Response | Model:
        """Create Alarm.

        Create an alarm.  If an `ACTIVE` or `ACKNOWLEDGED` alarm with the same `source.id` and `type` exists,  no new alarm is created.   Instead, the existing alarm is updated by incrementing the `count` property  and a new audit record of type `io.waylay.alarm.EventOccuredAgain` is added to the history.   Only the latest 1000 `io.waylay.alarm.EventOccuredAgain` audit records are kept in the history.
        :param query: URL Query parameters.
        :type query: CreateQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(CreateQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": AlarmEntity if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ErrorResponseWithDetails,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/alarms/v1/alarms",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def delete(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> None: ...

    @overload
    async def delete(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def delete(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def delete(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> None: ...

    @overload
    async def delete(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def delete(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> None | T | Response:
        """Delete Alarm.

        Delete an Alarm.
        :param alarm_id: Unique Alarm Identifier (required)
        :type alarm_id: str
        :param query: URL Query parameters.
        :type query: DeleteQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "alarmId": str(alarm_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(DeleteQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "204": None,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="DELETE",
            resource_path="/alarms/v1/alarms/{alarmId}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def get(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> AlarmEntity: ...

    @overload
    async def get(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def get(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def get(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def get(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def get(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> AlarmEntity | T | Response | Model:
        """Get Alarm.

        Get an alarm.
        :param alarm_id: Unique Alarm Identifier (required)
        :type alarm_id: str
        :param query: URL Query parameters.
        :type query: GetQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "alarmId": str(alarm_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(GetQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": AlarmEntity if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/alarms/v1/alarms/{alarmId}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> AlarmsQueryResult: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> AlarmsQueryResult | T | Response | Model:
        """Query Multiple Alarms.

        Query multiple alarms using a query language. The response contains the total number of alarms that fulfill the criteria.  By default, returns the first 50 alarms.
        :param query: URL Query parameters.
        :type query: ListQuery | QueryParamTypes, optional
        :param query['type'] (dict) <br> query.type (Query) : Filter on one or more alarm types.
        :type query['type']: List[str]
        :param query['status'] (dict) <br> query.status (Query) : Filter on one or more alarm statuses.
        :type query['status']: List[AlarmStatus]
        :param query['severity'] (dict) <br> query.severity (Query) : Filter on one or more alarm severities.
        :type query['severity']: List[AlarmSeverity]
        :param query['source'] (dict) <br> query.source (Query) : Filter on one or more source ids.  At least one source id is mandatory in combination with `Accept: application/vnd.waylay.alarms.timeseries+json`
        :type query['source']: List[str]
        :param query['dateFrom'] (dict) <br> query.date_from (Query) : Filter on alarm timestamp (equal or above).
        :type query['dateFrom']: int
        :param query['dateTo'] (dict) <br> query.date_to (Query) : Filter on alarm timestamp (equal or below).
        :type query['dateTo']: int
        :param query['from'] (dict) <br> query.var_from (Query) : Only applicable in combination with `Accept: application/vnd.waylay.alarms.timeseries+json`  Limits the timestamp of the Alarm Audit Records to be >= `from`
        :type query['from']: int
        :param query['to'] (dict) <br> query.to (Query) : Only applicable in combination with `Accept: application/vnd.waylay.alarms.timeseries+json`  Limits the timestamp of the Alarm Audit Records to be <= `to`
        :type query['to']: int
        :param query['creationTimeFrom'] (dict) <br> query.creation_time_from (Query) : Filter on alarm creationTime (equal or above).
        :type query['creationTimeFrom']: int
        :param query['creationTimeTo'] (dict) <br> query.creation_time_to (Query) : Filter on alarm creationTime (equal or below).
        :type query['creationTimeTo']: int
        :param query['lastUpdatedFrom'] (dict) <br> query.last_updated_from (Query) : Filter on alarm lastUpdateTime (equal or above).
        :type query['lastUpdatedFrom']: int
        :param query['lastUpdatedTo'] (dict) <br> query.last_updated_to (Query) : Filter on alarm lastUpdateTime (equal or below).
        :type query['lastUpdatedTo']: int
        :param query['lastTriggeredFrom'] (dict) <br> query.last_triggered_from (Query) : Filter on alarm lastTriggeredTime (equal or above).
        :type query['lastTriggeredFrom']: int
        :param query['lastTriggeredTo'] (dict) <br> query.last_triggered_to (Query) : Filter on alarm lastTriggeredTime (equal or below).
        :type query['lastTriggeredTo']: int
        :param query['sort'] (dict) <br> query.sort (Query) : (Pagination) field used to sort the alarms  Ignored in combination with `Accept: application/vnd.waylay.alarms.timeseries+json`
        :type query['sort']: str
        :param query['order'] (dict) <br> query.order (Query) : (Pagination) sort order  Ignored in combination with `Accept: application/vnd.waylay.alarms.timeseries+json`
        :type query['order']: str
        :param query['page'] (dict) <br> query.page (Query) : (Pagination) page Number   Ignored in combination with `Accept: application/vnd.waylay.alarms.timeseries+json`
        :type query['page']: int
        :param query['size'] (dict) <br> query.size (Query) : (Pagination) size of a page  Ignored in combination with `Accept: application/vnd.waylay.alarms.timeseries+json`
        :type query['size']: int
        :param query['additionalQueryParams'] (dict) <br> query.additional_query_params (Query) : To query the alarms based on the value of an additional property of the alarm,  you can add the key of the additional property as query parameter  with value the value you expect the alarm to have.
        :type query['additionalQueryParams']: Dict[str, ListAdditionalQueryParamsParameterValue]
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(ListQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": AlarmsQueryResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/alarms/v1/alarms",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def update(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        json: AlarmUpdate,
        query: UpdateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> AlarmEntity: ...

    @overload
    async def update(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        json: AlarmUpdate,
        query: UpdateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def update(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        json: AlarmUpdate,
        query: UpdateQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def update(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        json: AlarmUpdate,
        query: UpdateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def update(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        json: AlarmUpdate,
        query: UpdateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def update(
        self,
        alarm_id: Annotated[StrictStr, Field(description="Unique Alarm Identifier")],
        *,
        json: AlarmUpdate,
        query: UpdateQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> AlarmEntity | T | Response | Model:
        """Update Alarm.

        Update an alarm.
        :param alarm_id: Unique Alarm Identifier (required)
        :type alarm_id: str
        :param json: The json request body.
        :type json: AlarmUpdate, optional
        :param query: URL Query parameters.
        :type query: UpdateQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "alarmId": str(alarm_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}
        if json is not None and should_validate:
            body_adapter = TypeAdapter(AlarmUpdate)
            json = body_adapter.validate_python(json)  # type: ignore # https://github.com/pydantic/pydantic/discussions/7094
        body_args["json"] = json

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(UpdateQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": AlarmEntity if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ErrorResponseWithDetails,
            "404": ErrorResponse,
            "412": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="PUT",
            resource_path="/alarms/v1/alarms/{alarmId}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )