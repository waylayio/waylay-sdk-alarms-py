# coding: utf-8
"""Waylay Alarms api tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import re
from importlib.util import find_spec
from typing import Union

import pytest
from pytest_httpx import HTTPXMock
from typeguard import check_type
from waylay.sdk import ApiClient, WaylayClient
from waylay.sdk.api._models import Model
from waylay.services.alarms.api import AlarmEventsApi
from waylay.services.alarms.service import AlarmsService

from ..types.nd_json_response_stream_stub import NdJsonResponseStreamStub

MODELS_AVAILABLE = (
    True if find_spec("waylay.services.alarms.models") is not None else False
)

if MODELS_AVAILABLE:
    from waylay.services.alarms.models import NdJsonResponseStream
    from waylay.services.alarms.queries.alarm_events_api import GetQuery


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def alarm_events_api(waylay_api_client: ApiClient) -> AlarmEventsApi:
    return AlarmEventsApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that AlarmEventsApi api is registered in the sdk client."""
    assert isinstance(waylay_client.alarms.alarm_events, AlarmEventsApi)


def _get_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = NdJsonResponseStreamStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/alarms/v1/events(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_get(service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for get
    Alarm Events
    """
    # set path params
    kwargs = {
        # optionally use GetQuery to validate and reuse parameters
        "query": GetQuery(
            event_format="application/cloudevents+json",
        ),
    }
    _get_set_mock_response(httpx_mock, gateway_url)
    resp = await service.alarm_events.get(**kwargs)
    check_type(resp, Union[NdJsonResponseStream,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_get_without_types(
    service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get with models not installed
    Alarm Events
    """
    # set path params
    kwargs = {
        "query": {
            "eventFormat": "application/cloudevents+json",
        },
    }
    _get_set_mock_response(httpx_mock, gateway_url)
    resp = await service.alarm_events.get(**kwargs)
    check_type(resp, Model)
