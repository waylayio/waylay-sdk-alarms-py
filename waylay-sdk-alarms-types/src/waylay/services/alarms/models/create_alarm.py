# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.alarm_severity import AlarmSeverity
from ..models.alarm_status import AlarmStatus
from ..models.id_object import IdObject
from ..models.so8601_timestamp_or_millis import SO8601TimestampOrMillis


class CreateAlarm(WaylayBaseModel):
    """To create an alarm, you need to provide the following mandatory inputs.."""

    type: StrictStr = Field(description="Type of the alarm.")
    text: StrictStr = Field(description="Description of the alarm.")
    severity: AlarmSeverity
    source: IdObject
    status: AlarmStatus | None = AlarmStatus.ACTIVE
    timestamp: SO8601TimestampOrMillis | None = None
    assignee: StrictStr | None = Field(
        default=None, description="String field to indicate an assignee for the alarm."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
