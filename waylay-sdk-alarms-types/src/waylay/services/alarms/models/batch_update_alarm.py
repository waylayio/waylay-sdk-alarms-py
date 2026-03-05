"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.alarm_update import AlarmUpdate
from ..models.batch_alarm_entity import BatchAlarmEntity
from ..models.batch_update_action import BatchUpdateAction
from ..models.bulk_query_ids import BulkQueryIds


class BatchUpdateAlarm(WaylayBaseModel):
    """BatchUpdateAlarm."""

    entity: BatchAlarmEntity
    action: BatchUpdateAction
    query: BulkQueryIds
    action_parameters: AlarmUpdate = Field(alias="actionParameters")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
