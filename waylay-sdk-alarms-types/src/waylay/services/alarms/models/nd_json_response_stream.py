# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

from ..models.alarm_event import AlarmEvent
from ..models.cloud_alarm_event import CloudAlarmEvent

NdJsonResponseStream = Union[Annotated[AlarmEvent, ""], Annotated[CloudAlarmEvent, ""]]
"""NdJsonResponseStream."""
