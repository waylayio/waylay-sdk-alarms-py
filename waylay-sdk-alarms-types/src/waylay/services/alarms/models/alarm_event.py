"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.alarm_change_record import AlarmChangeRecord
from ..models.alarm_event_alarm import AlarmEventAlarm
from ..models.alarm_event_type import AlarmEventType


class AlarmEvent(WaylayBaseModel):
    """AlarmEvent."""

    eventtype: AlarmEventType
    eventtime: datetime
    alarm: AlarmEventAlarm
    changes: list[AlarmChangeRecord] | None = Field(
        default=None,
        description="Describes the changes that where done  Will only be there if `eventtype` is `io.waylay.alarm.AlarmUpdated`",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
