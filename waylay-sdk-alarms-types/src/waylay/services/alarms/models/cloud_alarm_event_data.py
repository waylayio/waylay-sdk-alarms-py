"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import (
    ConfigDict,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.alarm_event import AlarmEvent
from ..models.cloud_alarm_event_type import CloudAlarmEventType


class CloudAlarmEventData(WaylayBaseModel):
    """CloudAlarmEventData."""

    id: Any | None = None
    source: Any | None = None
    subject: StrictStr | None = None
    type: CloudAlarmEventType | None = None
    data: AlarmEvent | None = None
    time: datetime | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
