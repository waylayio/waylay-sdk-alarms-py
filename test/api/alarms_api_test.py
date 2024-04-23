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
from urllib.parse import quote

import pytest
from pytest_httpx import HTTPXMock
from typeguard import check_type
from waylay.sdk import ApiClient, WaylayClient
from waylay.sdk.api._models import Model
from waylay.services.alarms.api import AlarmsApi
from waylay.services.alarms.service import AlarmsService

from ..types.alarm_entity_stub import AlarmEntityStub
from ..types.alarm_update_stub import AlarmUpdateStub
from ..types.alarms_query_result_stub import AlarmsQueryResultStub
from ..types.create_alarm_stub import CreateAlarmStub

MODELS_AVAILABLE = (
    True if find_spec("waylay.services.alarms.models") is not None else False
)

if MODELS_AVAILABLE:
    from waylay.services.alarms.models import (
        AlarmEntity,
        AlarmsQueryResult,
    )
    from waylay.services.alarms.queries.alarms_api import ListQuery


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def alarms_api(waylay_api_client: ApiClient) -> AlarmsApi:
    return AlarmsApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that AlarmsApi api is registered in the sdk client."""
    assert isinstance(waylay_client.alarms.alarms, AlarmsApi)


def _create_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = AlarmEntityStub.create_json()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": re.compile(f"^{gateway_url}/alarms/v1/alarms(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_create(service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for create
    Create Alarm
    """
    # set path params
    kwargs = {
        "json": CreateAlarmStub.create_instance(),
    }
    _create_set_mock_response(httpx_mock, gateway_url)
    resp = await service.alarms.create(**kwargs)
    check_type(resp, Union[AlarmEntity,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_create_without_types(
    service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for create with models not installed
    Create Alarm
    """
    # set path params
    kwargs = {
        "json": CreateAlarmStub.create_json(),
    }
    _create_set_mock_response(httpx_mock, gateway_url)
    resp = await service.alarms.create(**kwargs)
    check_type(resp, Model)


def _delete_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, alarmId: str):
    mock_response = None
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": re.compile(f"^{gateway_url}/alarms/v1/alarms/{alarmId}(\\?.*)?"),
        "content": mock_response,
        "status_code": 204,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_delete(service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for delete
    Delete Alarm
    """
    # set path params
    alarmId = "alarm_id_example"

    kwargs = {}
    _delete_set_mock_response(httpx_mock, gateway_url, quote(str(alarmId)))
    resp = await service.alarms.delete(alarmId, **kwargs)
    assert not resp


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_delete_without_types(
    service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for delete with models not installed
    Delete Alarm
    """
    # set path params
    alarmId = "alarm_id_example"

    kwargs = {}
    _delete_set_mock_response(httpx_mock, gateway_url, quote(str(alarmId)))
    resp = await service.alarms.delete(alarmId, **kwargs)
    assert not resp


def _get_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, alarmId: str):
    mock_response = AlarmEntityStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/alarms/v1/alarms/{alarmId}(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_get(service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for get
    Get Alarm
    """
    # set path params
    alarmId = "alarm_id_example"

    kwargs = {}
    _get_set_mock_response(httpx_mock, gateway_url, quote(str(alarmId)))
    resp = await service.alarms.get(alarmId, **kwargs)
    check_type(resp, Union[AlarmEntity,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_get_without_types(
    service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get with models not installed
    Get Alarm
    """
    # set path params
    alarmId = "alarm_id_example"

    kwargs = {}
    _get_set_mock_response(httpx_mock, gateway_url, quote(str(alarmId)))
    resp = await service.alarms.get(alarmId, **kwargs)
    check_type(resp, Model)


def _list_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = AlarmsQueryResultStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/alarms/v1/alarms(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_list(service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for list
    Query Multiple Alarms
    """
    # set path params
    kwargs = {
        # optionally use ListQuery to validate and reuse parameters
        "query": ListQuery(
            type=["io.waylay.alarm.test"],
            status=[],
            severity=[],
            source=[],
            date_from=56,
            date_to=56,
            var_from=56,
            to=56,
            creation_time_from=56,
            creation_time_to=56,
            last_updated_from=56,
            last_updated_to=56,
            last_triggered_from=56,
            last_triggered_to=56,
            sort="timestamp",
            order="asc",
            page=1,
            size=50,
            additional_query_params={},
        ),
    }
    _list_set_mock_response(httpx_mock, gateway_url)
    resp = await service.alarms.list(**kwargs)
    check_type(resp, Union[AlarmsQueryResult,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_list_without_types(
    service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list with models not installed
    Query Multiple Alarms
    """
    # set path params
    kwargs = {
        "query": {
            "type": ["io.waylay.alarm.test"],
            "status": [],
            "severity": [],
            "source": [],
            "dateFrom": 56,
            "dateTo": 56,
            "from": 56,
            "to": 56,
            "creationTimeFrom": 56,
            "creationTimeTo": 56,
            "lastUpdatedFrom": 56,
            "lastUpdatedTo": 56,
            "lastTriggeredFrom": 56,
            "lastTriggeredTo": 56,
            "sort": "timestamp",
            "order": "asc",
            "page": 1,
            "size": 50,
            "additionalQueryParams": {},
        },
    }
    _list_set_mock_response(httpx_mock, gateway_url)
    resp = await service.alarms.list(**kwargs)
    check_type(resp, Model)


def _update_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, alarmId: str):
    mock_response = AlarmEntityStub.create_json()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": re.compile(f"^{gateway_url}/alarms/v1/alarms/{alarmId}(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_update(service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for update
    Update Alarm
    """
    # set path params
    alarmId = "alarm_id_example"

    kwargs = {
        "json": AlarmUpdateStub.create_instance(),
    }
    _update_set_mock_response(httpx_mock, gateway_url, quote(str(alarmId)))
    resp = await service.alarms.update(alarmId, **kwargs)
    check_type(resp, Union[AlarmEntity,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_update_without_types(
    service: AlarmsService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for update with models not installed
    Update Alarm
    """
    # set path params
    alarmId = "alarm_id_example"

    kwargs = {
        "json": AlarmUpdateStub.create_json(),
    }
    _update_set_mock_response(httpx_mock, gateway_url, quote(str(alarmId)))
    resp = await service.alarms.update(alarmId, **kwargs)
    check_type(resp, Model)
