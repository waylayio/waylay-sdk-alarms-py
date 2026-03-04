"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_alarm_entity import BatchAlarmEntity
from ..models.batch_delete_action import BatchDeleteAction
from ..models.batch_delete_query import BatchDeleteQuery


class BatchDeleteAlarm(WaylayBaseModel):
    """BatchDeleteAlarm."""

    entity: BatchAlarmEntity
    action: BatchDeleteAction
    query: BatchDeleteQuery

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
