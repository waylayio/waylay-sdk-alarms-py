"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_alarm_entity import BatchAlarmEntity


class BatchAlarm(WaylayBaseModel):
    """BatchAlarm."""

    entity: BatchAlarmEntity | None = None
    action: StrictStr | None = None
    query: dict[str, Any] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
