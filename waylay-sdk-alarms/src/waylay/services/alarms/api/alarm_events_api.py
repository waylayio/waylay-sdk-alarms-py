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
    from waylay.services.alarms.queries.alarm_events_api import GetQuery

    from waylay.services.alarms.models import NdJsonResponseStream

    from waylay.services.alarms.models import NdJsonResponseStream


try:
    from waylay.services.alarms.queries.alarm_events_api import GetQuery

    from waylay.services.alarms.models import NdJsonResponseStream

    from waylay.services.alarms.models import NdJsonResponseStream

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        GetQuery = dict

        NdJsonResponseStream = Model


from waylay.sdk.api import ApiClient, RESTTimeout

T = TypeVar("T")


class AlarmEventsApi(WithApiClient):
    """AlarmEventsApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def get(
        self,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> NdJsonResponseStream: ...

    @overload
    async def get(
        self,
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
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> NdJsonResponseStream | T | Response | Model:
        """Alarm Events.

        Opens a data stream for all Alarm Events for this tenant.
        :param query: URL Query parameters.
        :type query: GetQuery | QueryParamTypes, optional
        :param query['eventFormat'] (dict) <br> query.event_format (Query) : The format of events in the stream.   If specified this must be `application/cloudevents+json` (make sure to correctly URL encode the `+` as `%2B`)
        :type query['eventFormat']: str
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
            query = TypeAdapter(GetQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": NdJsonResponseStream if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {}
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/alarms/v1/events",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )