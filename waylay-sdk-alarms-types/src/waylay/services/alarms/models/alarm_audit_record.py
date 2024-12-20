# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.alarm_event_type import AlarmEventType


class AlarmAuditRecord(WaylayBaseModel):
    """AlarmAuditRecord."""

    id: StrictStr
    type: AlarmEventType
    text: StrictStr = Field(description="Text describing the change")
    timestamp: Any

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
