"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.alarm_severity import AlarmSeverity
from ..models.alarm_status import AlarmStatus
from ..models.id_object import IdObject


class AlarmEventAlarm(WaylayBaseModel):
    """Summary representation of an alarm.."""

    id: StrictStr = Field(description="Unique alarm identifier.")
    tenant_id: StrictStr = Field(alias="tenantId")
    creation_time: datetime = Field(alias="creationTime")
    type: StrictStr = Field(description="Type of the alarm.")
    text: StrictStr = Field(description="Description of the alarm.")
    timestamp: datetime
    source: IdObject
    severity: AlarmSeverity
    status: AlarmStatus
    count: Annotated[int, Field(strict=True, ge=1)]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
