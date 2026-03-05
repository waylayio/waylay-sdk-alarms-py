"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_alarm_entity import BatchAlarmEntity
from ..models.batch_operation_summary_action import BatchOperationSummaryAction


class BatchOperationSummary(WaylayBaseModel):
    """Summary of the batch operation."""

    entity: BatchAlarmEntity
    action: BatchOperationSummaryAction
    description: StrictStr = Field(description="Description of the operation")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
