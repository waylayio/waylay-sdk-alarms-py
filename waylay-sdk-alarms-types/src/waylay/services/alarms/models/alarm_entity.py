"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Any

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.alarm_audit_record import AlarmAuditRecord
from ..models.alarm_severity import AlarmSeverity
from ..models.alarm_status import AlarmStatus
from ..models.id_object import IdObject


class AlarmEntity(WaylayBaseModel):
    """AlarmEntity."""

    id: StrictStr = Field(description="Unique alarm identifier.")
    creation_time: datetime = Field(alias="creationTime")
    last_update_time: datetime = Field(alias="lastUpdateTime")
    last_triggered_time: datetime = Field(alias="lastTriggeredTime")
    type: StrictStr = Field(description="Type of the alarm.")
    text: StrictStr = Field(description="Description of the alarm.")
    timestamp: datetime
    source: IdObject
    severity: AlarmSeverity
    status: AlarmStatus
    count: Annotated[int, Field(strict=True, ge=1)] = Field(
        description="The number of times this alarm has been sent"
    )
    assignee: StrictStr | None = Field(
        default=None, description="String field to indicate an assignee for the alarm."
    )
    history: Annotated[list[AlarmAuditRecord], Field(min_length=1)] | None = None
    var_self: StrictStr | None = Field(default=None, alias="self")
    additional_properties: dict[str, Any] | None = Field(
        default=None,
        description="Additional properties that were present in the creation payload",
        alias="additionalProperties",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
